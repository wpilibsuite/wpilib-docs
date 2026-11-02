.. include:: <isonum.txt>

# What is WPILib?

.. figure:: /assets/wpilib-generic.svg
   :alt: The logo for the WPI Robotics Library.
   :target: http://wpilib.org
   :width: 500

The WPI Robotics Library ([WPILib](https://wpilib.org)) is the standard :term:`software library` provided for teams to write code for their FRC\ |reg| or FTC\ |reg| robots. WPILib contains a set of useful classes and subroutines for interfacing with various parts of the FIRST\ |reg| control system (such as sensors, motor controllers, and the driver station), as well as an assortment of other utility functions.

.. image:: /assets/wpi-logo.png
   :alt: The Worcester Polytechnic Institute (WPI) logo.
   :target: http://wpi.edu
   :width: 500

## Supported languages

There are three officially-supported text-based languages for WPILib: Java, C++, and Python. A considerable effort is made to maintain feature-parity between these languages, but WPILib may make features available to specific languages in cases where the feature represents a significant benefit to teams but cannot be implemented across all languages. When possible, class and method names are kept identical or highly-similar. Java, C++, and Python were chosen for the officially-supported languages due to their appropriate level-of-abstraction and broad use in both industry and education.

In general, C++ offers better high-end performance, at the cost of increased user effort (memory must be handled manually, and the C++ compiler does not do much to ensure user code will not crash at runtime). Java and Python offer lesser performance, but much greater convenience. Python users should take care to test their program to ensure that typos and other issues don't cause robot crashes, as Python is interpreted. New/inexperienced users are encouraged to use Java or Python.

## Source code and documentation

Detailed API documentation can be found on the official documentation pages for each language:

- [Java documentation](https://github.wpilib.org/allwpilib/docs/beta/java/)

- [C++ documentation](https://github.wpilib.org/allwpilib/docs/beta/cpp/)

- [Python documentation](https://robotpy.readthedocs.io/projects/robotpy/en/stable/)

WPILib is an open-source library - the majority of the library source code is in the [allwpilib](https://github.com/wpilibsuite/allwpilib) mono-repo. Python source code is in the [mostrobotpy](https://github.com/robotpy/mostrobotpy) mono-repo. Various other tooling and infrastructure code is in other repositories under the [wpilibsuite](https://github.com/wpilibsuite) organization on GitHub.

## Development Timeline

WPILib development happens on branches for individual years, as opposed to one main branch. Development and support for both FRC and FTC happen during different periods to support both FRC and FTC needs. These periods overlap with each other between years, so the following timeline visualizes these overlapping periods to make it easy to understand.

.. image:: /assets/dev_timeline.svg
  :alt: A timeline showing the different periods of WPILib's development for the next 4 years and how the different periods overlap between different, starting with development from FRC Kickoff to September, FRC beta from September to the next FRC Kickoff, FRC Support from FRC Kickoff to Champs, Updates/FTC Beta from Champs to FTC Kickoff, and FTC Support from FTC Kickoff to the next Champs.

For year N, WPILib will create a branch during year N - 1, and actively do development on it until around October of year N - 1, when it enters the beta testing period for FRC, which continues until FRC Kickoff for year N, which is when the first stable release is published. FRC will receive active support until the FIRST Championship ends, which then begins the FTC beta testing period, which lasts until FTC Kickoff in September of year N. FTC will then receive active support until the next FIRST Championship ends of year N + 1, and then the branch will no longer be supported.

## Platform Support

As a broad rule, WPILib only supports OSes that the OS developer still supports. In general, OS requirements are driven by OS developer support and C++ compiler feature support. Per [the WPILib roadmap](https://static1.squarespace.com/static/5d4b06a67cd3580001ded283/t/6631527dd3db35012eebacb3/1714508413721/WPILib+2024+Long+Term+Roadmap.pdf), we want to closely track future evolution of the supported languages, which often means new C++ features are adopted as soon as all supported platforms have compilers that support it. WPILib *may* continue to build for unsupported platforms, but no official support will be guaranteed, and if newer C++ features are only available in newer OSes, we can choose to adopt them and older OSes with compilers that lack support will no longer be able to build WPILib.

### Windows Support

Only 64-bit Windows 11 versions still in support by Microsoft will be supported.

### macOS Support

Apple generally keeps the last three macOS versions in support, and releases a new version annually, so WPILib also only supports the last three macOS versions.

### Linux Support

For Linux, we follow the [Debian release cycle](https://wiki.debian.org/DebianReleases#Release_statistics). Debian releases a new version every two years. The version released two summers before a year's release will become the minimum required OS for that year. This also aligns with Ubuntu LTS releases, so only the last Ubuntu LTS will be supported at a given time.

### Minimum required OS versions

+----------+--------+-------------------------+-------+-------+-------+
| OS       | 2027   | 2028                    | 2029  | 2030  | 2031  |
+==========+========+=========================+=======+=======+=======+
| Windows  | 11     | 11                      | 11    | 11    | 11    |
+----------+--------+-------------------------+-------+-------+-------+
| Debian   | Trixie | Trixie                  | Forky | Forky | Duke  |
+----------+--------+-------------------------+-------+-------+-------+
| Ubuntu   | 26.04  | 26.04                   | 28.04 | 28.04 | 30.04 |
+----------+--------+-------------------------+-------+-------+-------+
| macOS    | 15     | 26 (Last Intel release) | 27    | 28    | 29    |
+----------+--------+-------------------------+-------+-------+-------+
