![Documentation Status](https://readthedocs.org/projects/frc-docs/badge/?version=latest)
[![CI](https://github.com/wpilibsuite/wpilib-docs/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/wpilibsuite/wpilib-docs/actions/workflows/CI.yml?query=branch:main)
[![Link Check](https://github.com/wpilibsuite/wpilib-docs/actions/workflows/link-check.yml/badge.svg)](https://github.com/wpilibsuite/wpilib-docs/actions/workflows/link-check.yml)

# wpilib-docs
Welcome to wpilib-docs! This repository contains the various source articles for the wpilib-docs website. wpilib-docs is licensed under Creative Commons, with assets such as the *FIRST* logo under trademark and copyright of [FIRST](https://www.firstinspires.org/).

The website is available under the following domains, it is preferred to use the WPILib domain URL:
- https://docs.wpilib.org/en/latest/
- https://frcdocs.wpi.edu/en/latest/
- https://frc-docs.readthedocs.io/en/latest/

# WPILib Mission
The WPILib Mission is to enable FIRST Robotics Competition (FRC) and FIRST Tech Challenge (FTC) teams to focus on writing game-specific software rather than focusing on hardware details - "raise the floor, don't lower the ceiling". We work to enable teams with limited programming knowledge and/or mentor experience to be as successful as possible, while not hampering the abilities of teams with more advanced programming capabilities. We support the FRC Kit of Parts/FTC control system components directly in the library. We also strive to keep parity between major features of each language (Java, C++, and Python), so that teams aren't at a disadvantage for choosing a specific programming language. WPILib is an open source project, licensed under the BSD 3-clause license. You can find a copy of the license [here](https://github.com/wpilibsuite/allwpilib/blob/main/LICENSE.md).

# Contributing to wpilib-docs

We're happy to have you contributing to wpilib-docs, whether it's writing articles, fixing code, new extensions, or adding translations!

All the information needed to contribute to wpilib-docs is located in the [contributing](https://docs.wpilib.org/en/latest/docs/contributing/wpilib-docs/index.html) section on wpilib-docs. Additionally, please ensure that all contributions follow the WPILib [Code of Conduct](https://github.com/wpilibsuite/allwpilib/blob/main/CODE_OF_CONDUCT.md).

## Links to FRC Docs

FRC Docs is maintained as a separate repository and site. Cross-site links use
`{{ frc_docs_url }}` in source articles. The Sphinx `frc_docs_url` setting supplies
the site root, including any language/version prefix.

The default is the hosted FRC draft,
`https://amanda-frc-docs.readthedocs.io/en/latest/`. Push FRC Docs and confirm its
Read the Docs build succeeds before publishing WPILib links to newly added pages.
For local previews, set `FRC_DOCS_URL=http://127.0.0.1:8001/` or pass
`-D frc_docs_url=http://127.0.0.1:8001/` to Sphinx. The same settings can select
a permanent public site root later, including its language/version prefix.

To check the links between both local HTML builds, including section anchors:

```sh
python3 scripts/check_cross_site_links.py /private/tmp/wpilib-docs-preview /private/tmp/frc-docs-preview
```

Build WPILib with `-D frc_docs_url=http://127.0.0.1:8001/` and FRC Docs with
`-D wpilib_docs_url=http://127.0.0.1:8000/` first. The checker reads the HTML
directly; preview servers do not need to be running. Use `--wpilib-url` and
`--frc-url` if the builds use different site roots. This checks cross-site
destinations only; run each site's Sphinx checks separately.
