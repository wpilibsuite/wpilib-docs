"""Keep the Read the Docs ``search.ignore`` list in sync with redirects.txt.

Rediraffe writes a small HTML stub for every page listed on the left side of
``redirects.txt``. Read the Docs indexes those stubs like any other page, so
redirected pages show up in search results (wpilibsuite/wpilib-docs#2457).

Read the Docs reads ``readthedocs.yml`` before Sphinx runs, so the ignore list
cannot be generated during the RTD build itself. Instead, the list lives in a
generated block of ``readthedocs.yml``:

* Run this file as a script to regenerate the block::

     uv run python source/_extensions/rtd_search_ignore.py

* Pass ``--check`` to fail (exit 1) without writing when the block is stale.

* As a Sphinx extension it performs the same check at the start of every build
  and emits a warning, which ``-W`` turns into an error, when it is stale.
"""

from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path, PureWindowsPath

from sphinxext.rediraffe import create_graph

BEGIN_MARKER = "# BEGIN GENERATED search.ignore"
END_MARKER = "# END GENERATED search.ignore"
REGENERATE_COMMAND = "uv run python source/_extensions/rtd_search_ignore.py"

# Read the Docs replaces its default ignore list when search.ignore is set,
# so keep the defaults in the generated list.
# https://docs.readthedocs.io/en/stable/config-file/v2.html#search-ignore
RTD_DEFAULT_IGNORES = (
    "search.html",
    "search/index.html",
    "404.html",
    "404/index.html",
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REDIRECTS = REPO_ROOT / "source" / "redirects.txt"
DEFAULT_RTD_CONFIG = REPO_ROOT / "readthedocs.yml"
# Sphinx's default source_suffix; conf.py does not override it. The extension
# uses the live config value, so a mismatch here fails the build check.
DEFAULT_SOURCE_SUFFIXES = (".rst",)


def _remove_suffix(name: str, suffixes) -> str:
    for suffix in suffixes:
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def redirect_html_path(source_path: str, suffixes=DEFAULT_SOURCE_SUFFIXES) -> str:
    """Return the HTML output path rediraffe writes for a redirected source.

    Mirrors ``sphinxext.rediraffe.build_redirects`` for the ``html`` builder,
    which is what Read the Docs uses for the indexed site.
    """
    path = PureWindowsPath(source_path)
    name = _remove_suffix(path.name, suffixes)
    return (path.parent / f"{name}.html").as_posix()


def search_ignore_patterns(
    redirects_file: Path, suffixes=DEFAULT_SOURCE_SUFFIXES
) -> list[str]:
    """Return the search.ignore patterns: RTD defaults, then every redirect.

    Redirects keep the order of ``redirects.txt``. That file is append-only, so
    new redirects only ever append to the generated list.
    """
    patterns = list(RTD_DEFAULT_IGNORES)
    seen = set(patterns)
    # create_graph is rediraffe's own parser, so the quoting/comment rules and
    # duplicate-key errors match what the build actually does.
    for redirect_from in create_graph(Path(redirects_file)):
        # RTD treats *, ? and [ as wildcards.
        pattern = glob.escape(redirect_html_path(redirect_from, suffixes))
        if pattern not in seen:
            seen.add(pattern)
            patterns.append(pattern)
    return patterns


def render_block(patterns: list[str]) -> str:
    """Render the generated readthedocs.yml block, markers included."""
    lines = [
        BEGIN_MARKER,
        "# Generated from source/redirects.txt. Do not edit by hand. Regenerate with:",
        f"#   {REGENERATE_COMMAND}",
        "search:",
        "  ignore:",
    ]
    # Single-quoted YAML scalars: only ' needs escaping (doubled).
    lines += ["    - '{}'".format(p.replace("'", "''")) for p in patterns]
    lines.append(END_MARKER)
    return "\n".join(lines) + "\n"


def update_config_text(config_text: str, patterns: list[str]) -> str:
    """Return ``config_text`` with the generated block replaced or appended."""
    block = render_block(patterns)
    lines = config_text.splitlines(keepends=True)
    begin = [i for i, line in enumerate(lines) if line.rstrip() == BEGIN_MARKER]
    end = [i for i, line in enumerate(lines) if line.rstrip() == END_MARKER]

    if not begin and not end:
        if any(line.startswith("search:") for line in lines):
            raise ValueError(
                "readthedocs.yml has a hand-written 'search:' section; remove it "
                "so the generated block can own search.ignore"
            )
        text = config_text
        if text and not text.endswith("\n"):
            text += "\n"
        if text and not text.endswith("\n\n"):
            text += "\n"
        return text + block

    if len(begin) != 1 or len(end) != 1 or begin[0] > end[0]:
        raise ValueError(
            f"readthedocs.yml must contain exactly one '{BEGIN_MARKER}' line "
            f"followed by one '{END_MARKER}' line"
        )
    return "".join(lines[: begin[0]]) + block + "".join(lines[end[0] + 1 :])


def is_up_to_date(
    redirects_file: Path, config_file: Path, suffixes=DEFAULT_SOURCE_SUFFIXES
) -> bool:
    config_text = Path(config_file).read_text(encoding="utf-8")
    patterns = search_ignore_patterns(redirects_file, suffixes)
    return update_config_text(config_text, patterns) == config_text


def write_config(
    redirects_file: Path, config_file: Path, suffixes=DEFAULT_SOURCE_SUFFIXES
) -> bool:
    """Regenerate the block in place. Return True if the file changed."""
    config_file = Path(config_file)
    config_text = config_file.read_text(encoding="utf-8")
    patterns = search_ignore_patterns(redirects_file, suffixes)
    new_text = update_config_text(config_text, patterns)
    if new_text == config_text:
        return False
    with config_file.open("w", encoding="utf-8", newline="\n") as f:
        f.write(new_text)
    return True


# -- Sphinx extension ---------------------------------------------------------


def _check_on_build(app) -> None:
    from sphinx.util import logging

    logger = logging.getLogger(__name__)
    redirects = app.config.rediraffe_redirects
    if not isinstance(redirects, str):
        return
    redirects_file = Path(app.srcdir) / redirects
    # confdir is frc-docs/source for both this repo and frc-docs-translations.
    config_file = Path(app.confdir).parent / "readthedocs.yml"
    if not redirects_file.is_file() or not config_file.is_file():
        logger.info("rtd_search_ignore: redirects or readthedocs.yml not found")
        return

    suffixes = tuple(app.config.source_suffix)
    try:
        up_to_date = is_up_to_date(redirects_file, config_file, suffixes)
    except ValueError as e:
        logger.warning(f"rtd_search_ignore: {e}", type="rtd_search_ignore")
        return
    if not up_to_date:
        logger.warning(
            "rtd_search_ignore: search.ignore in readthedocs.yml is out of date "
            f"with {redirects}. Run '{REGENERATE_COMMAND}' and commit the result.",
            type="rtd_search_ignore",
        )


def setup(app):
    app.connect("builder-inited", _check_on_build)
    return {"parallel_read_safe": True, "parallel_write_safe": True}


# -- Command line -------------------------------------------------------------


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 if readthedocs.yml is out of date instead of writing it",
    )
    parser.add_argument("--redirects", type=Path, default=DEFAULT_REDIRECTS)
    parser.add_argument("--config", type=Path, default=DEFAULT_RTD_CONFIG)
    args = parser.parse_args(argv)

    if args.check:
        if is_up_to_date(args.redirects, args.config):
            print(f"{args.config} search.ignore is up to date.")
            return 0
        print(
            f"Error: search.ignore in {args.config} is out of date with "
            f"{args.redirects}. Run '{REGENERATE_COMMAND}' and commit the result.",
            file=sys.stderr,
        )
        return 1

    changed = write_config(args.redirects, args.config)
    print(f"{'Updated' if changed else 'No changes to'} {args.config}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
