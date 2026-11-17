"""Check links between two Sphinx HTML builds without running web servers."""

import argparse
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a":
            if "name" in attrs:
                self.ids.add(attrs["name"])
            if attrs.get("href"):
                self.links.append(attrs["href"])


@lru_cache(maxsize=None)
def read_page(path):
    return Page(path)


def check(source, destination, destination_url):
    source, destination = source.resolve(), destination.resolve()
    base = urlsplit(destination_url.rstrip("/") + "/")
    count = 0
    errors = []
    for page in sorted(source.rglob("*.html")):
        for href in read_page(page).links:
            link = urlsplit(href)
            if (link.scheme, link.netloc) != (base.scheme, base.netloc):
                continue
            if not link.path.startswith(base.path):
                continue
            count += 1
            relative = unquote(link.path[len(base.path) :])
            target = (destination / relative).resolve()
            if not target.is_relative_to(destination):
                reason = "path escapes destination"
            else:
                if target.is_dir():
                    target /= "index.html"
                if not target.is_file():
                    reason = "missing file"
                elif (
                    link.fragment
                    and target.suffix == ".html"
                    and unquote(link.fragment) not in read_page(target).ids
                ):
                    reason = "missing anchor"
                else:
                    continue
            errors.append(f"{page.relative_to(source)}: {href} ({reason})")
    return count, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wpilib", type=Path, help="WPILib HTML build directory")
    parser.add_argument("frc", type=Path, help="FRC HTML build directory")
    parser.add_argument("--wpilib-url", default="http://127.0.0.1:8000/")
    parser.add_argument("--frc-url", default="http://127.0.0.1:8001/")
    args = parser.parse_args()
    wpilib, frc = args.wpilib.resolve(), args.frc.resolve()
    for root in (wpilib, frc):
        if not (root / "index.html").is_file():
            parser.error(f"No index.html in {root}; build the site first")
    errors = []
    for name, source, destination, url in (
        ("WPILib → FRC", wpilib, frc, args.frc_url),
        ("FRC → WPILib", frc, wpilib, args.wpilib_url),
    ):
        count, failures = check(source, destination, url)
        print(f"{name}: {count} links checked, {len(failures)} failures")
        errors.extend(failures)
        if not count:
            errors.append(
                f"{name}: no cross-site links found; check build URL settings"
            )
    for error in errors:
        print(error)
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
