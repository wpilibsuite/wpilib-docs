"""Tests for source/_extensions/rtd_search_ignore.py.

Run with: uv run python -m unittest discover -s tests -v
"""

import io
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "source"))

from _extensions import rtd_search_ignore as rsi  # noqa: E402

BASE_CONFIG = textwrap.dedent("""\
    version: 2

    formats:
      - pdf
    """)


class TempDirTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, name, text):
        path = self.tmp / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(text), encoding="utf-8")
        return path


class RedirectHtmlPathTest(unittest.TestCase):
    def test_maps_rst_to_html(self):
        self.assertEqual(
            rsi.redirect_html_path("docs/software/old-page.rst"),
            "docs/software/old-page.html",
        )

    def test_index_stays_index_html(self):
        self.assertEqual(
            rsi.redirect_html_path("docs/software/old/index.rst"),
            "docs/software/old/index.html",
        )

    def test_windows_separators_are_normalized(self):
        self.assertEqual(
            rsi.redirect_html_path("docs\\software\\old.rst"),
            "docs/software/old.html",
        )


class SearchIgnorePatternsTest(TempDirTestCase):
    def test_defaults_then_redirects_in_file_order(self):
        redirects = self.write(
            "redirects.txt",
            """\
            # comment lines and blank lines are skipped

            "docs/b/old.rst" "docs/b/new.rst"
            docs/a/old.rst docs/a/new.rst
            'docs/c/index.rst' 'docs/d/index.rst'
            """,
        )
        self.assertEqual(
            rsi.search_ignore_patterns(redirects),
            list(rsi.RTD_DEFAULT_IGNORES)
            + [
                "docs/b/old.html",
                "docs/a/old.html",
                "docs/c/index.html",
            ],
        )

    def test_chained_redirects_ignore_every_hop(self):
        redirects = self.write(
            "redirects.txt",
            """\
            "docs/one.rst" "docs/two.rst"
            "docs/two.rst" "docs/three.rst"
            """,
        )
        patterns = rsi.search_ignore_patterns(redirects)
        self.assertIn("docs/one.html", patterns)
        self.assertIn("docs/two.html", patterns)
        self.assertNotIn("docs/three.html", patterns)

    def test_glob_characters_are_escaped(self):
        redirects = self.write(
            "redirects.txt",
            """\
            "docs/odd[1]?.rst" "docs/new.rst"
            "docs/c++-java.rst" "docs/new.rst"
            """,
        )
        patterns = rsi.search_ignore_patterns(redirects)
        self.assertIn("docs/odd[[]1][?].html", patterns)
        self.assertIn("docs/c++-java.html", patterns)


class UpdateConfigTextTest(unittest.TestCase):
    patterns = ["search.html", "docs/old.html"]

    def test_appends_block_when_missing(self):
        updated = rsi.update_config_text(BASE_CONFIG, self.patterns)
        self.assertTrue(updated.startswith(BASE_CONFIG + "\n"))
        self.assertTrue(updated.endswith(rsi.render_block(self.patterns)))

    def test_replaces_existing_block_and_keeps_surroundings(self):
        stale = (
            "version: 2\n\n"
            + rsi.render_block(["stale.html"])
            + "\nformats:\n  - pdf\n"
        )
        updated = rsi.update_config_text(stale, self.patterns)
        self.assertNotIn("stale.html", updated)
        self.assertTrue(updated.startswith("version: 2\n\n" + rsi.BEGIN_MARKER))
        self.assertTrue(updated.endswith(rsi.END_MARKER + "\n\nformats:\n  - pdf\n"))

    def test_is_idempotent(self):
        once = rsi.update_config_text(BASE_CONFIG, self.patterns)
        self.assertEqual(rsi.update_config_text(once, self.patterns), once)

    def test_quotes_are_yaml_escaped(self):
        block = rsi.render_block(["docs/robot's.html"])
        self.assertIn("    - 'docs/robot''s.html'\n", block)

    def test_rejects_hand_written_search_section(self):
        with self.assertRaises(ValueError):
            rsi.update_config_text(
                BASE_CONFIG + "search:\n  ignore:\n    - x.html\n", self.patterns
            )

    def test_rejects_unbalanced_markers(self):
        with self.assertRaises(ValueError):
            rsi.update_config_text(BASE_CONFIG + rsi.BEGIN_MARKER + "\n", self.patterns)


class CommandLineTest(TempDirTestCase):
    def run_main(self, *args):
        out, err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = out, err
        try:
            code = rsi.main(list(args))
        finally:
            sys.stdout, sys.stderr = old_out, old_err
        return code, out.getvalue() + err.getvalue()

    def test_check_fails_then_write_fixes_it(self):
        redirects = self.write("redirects.txt", '"docs/old.rst" "docs/new.rst"\n')
        config = self.write("readthedocs.yml", BASE_CONFIG)
        common = ("--redirects", str(redirects), "--config", str(config))

        code, output = self.run_main("--check", *common)
        self.assertEqual(code, 1)
        self.assertIn("out of date", output)

        self.assertEqual(self.run_main(*common)[0], 0)
        self.assertIn("    - 'docs/old.html'\n", config.read_text(encoding="utf-8"))
        self.assertEqual(self.run_main("--check", *common)[0], 0)

        # Appending a redirect makes the committed config stale again.
        with redirects.open("a", encoding="utf-8") as f:
            f.write('"docs/older.rst" "docs/new.rst"\n')
        self.assertEqual(self.run_main("--check", *common)[0], 1)


class SphinxBuildTest(TempDirTestCase):
    """Build a tiny project with rediraffe to check the paths really match."""

    def build(self, config_text):
        src = self.tmp / "proj" / "source"
        self.write(
            "proj/source/conf.py",
            """\
            extensions = ["sphinxext.rediraffe", "_extensions.rtd_search_ignore"]
            rediraffe_redirects = "redirects.txt"
            """,
        )
        self.write(
            "proj/source/index.rst",
            """\
            Index
            =====

            .. toctree::

               docs/new
               docs/sub/index
            """,
        )
        self.write("proj/source/docs/new.rst", "New\n===\n")
        self.write("proj/source/docs/sub/index.rst", "Sub\n===\n")
        self.write(
            "proj/source/redirects.txt",
            """\
            "docs/old.rst" "docs/new.rst"
            "docs/older.rst" "docs/old.rst"
            "docs/moved/index.rst" "docs/sub/index.rst"
            """,
        )
        config = self.write("proj/readthedocs.yml", config_text)

        from sphinx.application import Sphinx

        out = self.tmp / "out"
        warnings = io.StringIO()
        app = Sphinx(
            srcdir=str(src),
            confdir=str(src),
            outdir=str(out),
            doctreedir=str(self.tmp / "doctrees"),
            buildername="html",
            status=io.StringIO(),
            warning=warnings,
            freshenv=True,
        )
        app.build()
        return src, config, out, warnings.getvalue()

    def test_ignore_list_matches_rediraffe_output(self):
        src, config, out, warnings = self.build(BASE_CONFIG)
        self.assertIn("search.ignore in readthedocs.yml is out of date", warnings)

        rsi.write_config(src / "redirects.txt", config)
        patterns = rsi.search_ignore_patterns(src / "redirects.txt")
        redirect_pages = [p for p in patterns if p not in rsi.RTD_DEFAULT_IGNORES]
        self.assertEqual(
            redirect_pages,
            ["docs/old.html", "docs/older.html", "docs/moved/index.html"],
        )
        for page in redirect_pages:
            self.assertTrue((out / page).is_file(), f"rediraffe did not write {page}")
        # Real pages are not ignored.
        self.assertTrue((out / "docs/new.html").is_file())
        self.assertNotIn("docs/new.html", patterns)

        self.assertNotIn(
            "rtd_search_ignore", self.build(config.read_text(encoding="utf-8"))[3]
        )


class RepositoryConfigTest(unittest.TestCase):
    def test_committed_readthedocs_yml_is_up_to_date(self):
        self.assertTrue(
            rsi.is_up_to_date(rsi.DEFAULT_REDIRECTS, rsi.DEFAULT_RTD_CONFIG),
            f"readthedocs.yml is stale; run '{rsi.REGENERATE_COMMAND}'",
        )


if __name__ == "__main__":
    unittest.main()
