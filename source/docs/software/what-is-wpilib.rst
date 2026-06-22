.. include:: <isonum.txt>

# What is WPILib?

.. figure:: /assets/wpilib-generic.svg
   :alt: The WPI Robotics Library logo.
   :target: http://wpilib.org
   :width: 400

WPILib is the standard software library for programming
*FIRST*\ |reg| robots.
It provides the classes and tools needed to control motors, read sensors,
communicate with the Driver Station, and run autonomous routines — across
FRC\ |reg| and (from 2027-2028) FTC\ |reg| via Systemcore.

.. image:: /assets/wpi-logo.png
   :alt: Worcester Polytechnic Institute (WPI) logo.
   :target: http://wpi.edu
   :width: 300
   :align: center

WPILib is developed and maintained by a partnership between
`Worcester Polytechnic Institute (WPI) <http://wpi.edu>`_,
FIRST\ |reg|, and volunteer developers from the community.

.. rubric:: Which path are you on?

.. grid:: 1 1 3 3
   :gutter: 3

   .. grid-item-card:: FIRST Robotics Competition
      :class-card: sw-card-frc

      **FRC**
      ^^^
      Full WPILib support. Java, C++, Python. Deploys to Systemcore.
      Driver Station on Windows required for competition.

   .. grid-item-card:: XRP Practice Robot
      :class-card: sw-card-shared

      **FRC + FTC**
      ^^^
      Same WPILib code on a $75 desktop robot. No control system
      hardware required. Great for off-season learning and
      FTC Systemcore prep.

   .. grid-item-card:: FTC Systemcore
      :class-card: sw-card-ftc

      **FTC 2027-2028+**
      ^^^
      WPILib now supports FTC via Systemcore and Motioncore.
      Same Java/C++/Python toolchain as FRC.

.. rubric:: What WPILib Includes

.. list-table::
   :header-rows: 1
   :widths: 22 46 10 22

   * - Component
     - Description
     - FRC
     - FTC
   * - **Robot library**
     - Motor control, sensors, drive classes, kinematics
     - ✓
     - ✓ (Systemcore)
   * - **VS Code extension**
     - Project templates, deploy, build, vendor manager
     - ✓
     - ✓
   * - **Simulation framework**
     - Run robot code on laptop without hardware
     - ✓
     - ✓ (XRP)
   * - **Glass dashboard**
     - Real-time telemetry and field visualization
     - ✓
     - ✓
   * - **Elastic dashboard**
     - Configurable driver dashboard (replaces Shuffleboard)
     - ✓
     - Planned
   * - **PathPlanner / Choreo**
     - GUI path planning for autonomous
     - ✓
     - Planned
   * - **OutlineViewer**
     - NetworkTables browser
     - ✓
     - ✓
   * - **Shuffleboard**
     - Older dashboard *(Removed 2027)*
     - ✗
     - ✗

.. rubric:: Language Comparison

.. list-table::
   :header-rows: 1
   :widths: 20 30 20 30

   * - Language
     - Recommended for
     - Performance
     - Community examples
   * - **Java** *(Recommended)*
     - New teams, most teams
     - Good
     - Most abundant
   * - **C++**
     - Teams with C++ experience
     - Best
     - Abundant
   * - **Python**
     - Teams already using Python
     - Good
     - Growing

.. tip::

   **All three languages share the same API design.**
   Class names and method names are kept identical or very close across
   Java, C++, and Python.

.. rubric:: Development Environments

WPILib supports two families of development environment: a full
**desktop IDE** and browser-based **OnBot** environments that run
directly on the Systemcore with no local install.

**Desktop Environment — Java, C++, Python**

.. card:: Visual Studio Code + WPILib Extension
   :class-card: sw-card-frc

   **Desktop**

   All three languages use VS Code as the IDE, with the WPILib extension
   providing project templates, build tools, simulation, and vendor library
   management. Works on Windows, macOS, and Linux.

   .. list-table::
      :header-rows: 1

      * - Feature
        - Java
        - C++
        - Python
      * - **IDE**
        - VS Code
        - VS Code
        - VS Code
      * - **Build system**
        - GradleRIO
        - GradleRIO (open to change)
        - More integrated experience
      * - **Desktop simulation**
        - ✓
        - ✓
        - ✓
      * - **Offline install**
        - ✓
        - ✓
        - ✓
      * - **Deploy**
        - USB or Wi-Fi to Systemcore
        - USB or Wi-Fi to Systemcore
        - USB or Wi-Fi to Systemcore

.. tip::

   **Python install experience:** WPILib is actively working to
   provide a more integrated Python setup — reducing the number of
   separate steps compared to Java/C++.
   **C++ build system:** GradleRIO is the baseline; transitioning
   to an alternative build system is possible depending on community contributions.

**OnBot Environments — Blockly, Java, Python, LabVIEW**

.. card:: VS Code-derived editor hosted on Systemcore
   :class-card: sw-card-frc

   **OnBot (Browser-based)**

   OnBot environments run entirely in the browser — no local
   installation required. Code is written, saved, and deployed directly
   on the Systemcore. Supports multiple saved Workspaces with a Deploy
   button to choose which one runs.

   .. list-table::
      :header-rows: 1

      * - Feature
        - Blockly
        - Java
        - Python
        - LabVIEW
      * - **Editor**
        - Block visual editor
        - VS Code-derived
        - VS Code-derived
        - Graphical (browser)
      * - **Backed by**
        - Python
        - Java
        - Python
        - LabVIEW
      * - **Desktop install**
        - None required
        - None required
        - None required
        - None required
      * - **Multi-user**
        - Single-user (under investigation)
        - Single-user (under investigation)
        - Single-user (under investigation)
        - Single-user (under investigation)

.. warning::

   **C++ is not supported in OnBot environments.**
   The browser-based toolchain does not provide a good enough C++ experience
   to ship. Use the desktop VS Code environment for C++ development.

   **OnBot notes:** Currently planned as single-user access
   (multi-user being investigated). Supports multiple saved
   *Workspaces* with a Deploy button to select which one runs on
   the Systemcore. Simulation is not planned for OnBot environments.

**FTC REV Duo**

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: OnBot Java / Android Studio
      :class-card: sw-card-ftc

      **FTC (REV Duo)**
      ^^^
      REV Duo teams use the FTC SDK with OnBot Java (browser-based)
      or Android Studio. Documented at
      `ftc-docs.firstinspires.org <https://ftc-docs.firstinspires.org>`_.

   .. grid-item-card:: Blocks (FTC SDK)
      :class-card: sw-card-ftc

      **FTC (REV Duo)**
      ^^^
      Visual block-based programming via the FTC SDK OnBot interface.
      Documented at
      `ftc-docs.firstinspires.org <https://ftc-docs.firstinspires.org>`_.

.. rubric:: Build and Deploy Comparison

.. list-table::
   :header-rows: 1
   :widths: 22 26 30 22

   * - Feature
     - Desktop (VS Code)
     - OnBot (Java / Python / Blockly / LabVIEW)
     - FTC REV Duo
   * - **Languages**
     - Java, C++, Python
     - Java, Python, Blockly, LabVIEW
     - Java, Blocks
   * - **C++ support**
     - ✓
     - ✗ Not supported
     - ✗
   * - **Build system**
     - GradleRIO
     - On-device (browser)
     - FTC SDK / Gradle
   * - **Deploy**
     - USB or Wi-Fi to Systemcore
     - Deploy button in browser (Workspace-based)
     - ADB over USB or Wi-Fi
   * - **Simulation**
     - ✓ Full desktop sim
     - ✗ Not planned
     - ✗ None
   * - **Offline install**
     - ✓
     - N/A — runs on Systemcore
     - ✓
   * - **Multi-user**
     - N/A
     - Single-user (under investigation)
     - N/A
   * - **Driver Station**
     - FRC DS (Windows)
     - FRC DS (Windows)
     - Driver Hub / phone

.. rubric:: Dashboards

.. list-table::
   :header-rows: 1
   :widths: 20 35 45

   * - Dashboard
     - Status
     - Best for
   * - **Elastic**
     - ✓ Current — recommended
     - Competition driver dashboard. Highly configurable.
   * - **AdvantageScope**
     - ✓ Current — recommended
     - Log review, 3D field visualization, mechanism replay.
   * - **Glass**
     - ✓ Current
     - Built-in simulation UI and lightweight telemetry.
   * - **SmartDashboard**
     - *(Removed 2027)*
     - Use Elastic instead.
   * - **Shuffleboard**
     - *(Removed 2027)*
     - Use Elastic instead.

.. rubric:: Vendor Libraries

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: What are vendor libraries?

      Hardware vendors (REV, CTRE, etc.) ship WPILib extension
      libraries that add support for their specific motor controllers,
      sensors, and accessories. They are installed
      **per project** via the VS Code Dependency Manager
      and do not carry over on project import.

   .. grid-item-card:: Common libraries

      - **REVLib** — SPARK MAX, SPARK Flex
      - **Phoenix 6** — Talon FX, CANcoder
      - **PathplannerLib** — auto trajectories
      - **PhotonLib** — PhotonVision cameras
      - **Limelight** — Limelight cameras

.. rubric:: Path Planning

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: PathPlanner / Choreo
      :link: pathplanning/index
      :link-type: doc
      :class-card: sw-card-frc

      **FRC**
      ^^^
      GUI tools for drawing autonomous paths. Both generate
      trajectory commands that slot into command-based robot programs.
      PathPlanner is more beginner-friendly; Choreo optimizes
      for time.

   .. grid-item-card:: Road Runner
      :class-card: sw-card-ftc

      **FTC REV Duo**
      ^^^
      The standard FTC path planning library for REV Duo teams.
      Separate from WPILib. FTC Systemcore teams will use
      PathPlanner/Choreo (planned for 2028).

.. rubric:: Shared Concepts Across Programs

These programming concepts are identical whether you are writing FRC,
FTC Systemcore, or XRP code.

.. grid:: 1 1 1 1
   :gutter: 3

   .. grid-item-card:: PID Control
      :class-card: sw-card-shared

      Proportional-Integral-Derivative feedback loop for precise
      motor velocity and position control.

   .. grid-item-card:: Odometry
      :class-card: sw-card-shared

      Track robot position on the field using encoder and gyro data.
      Used for autonomous navigation.

   .. grid-item-card:: State Machines
      :class-card: sw-card-shared

      Command-based programming uses a state machine model:
      subsystems, commands, and triggers.

   .. grid-item-card:: AprilTags
      :class-card: sw-card-shared

      WPILib includes built-in AprilTag detection for field
      localization and target tracking.

   .. grid-item-card:: Motor Control
      :class-card: sw-card-shared

      DifferentialDrive, MecanumDrive, and swerve kinematics
      classes work identically across all platforms.

   .. grid-item-card:: Java Fundamentals
      :class-card: sw-card-shared

      WPILib Java code uses standard Java: classes, interfaces,
      lambdas. No framework-specific syntax to learn separately.

.. rubric:: Source Code and API Docs

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: Java API Reference
      :link: https://github.wpilib.org/allwpilib/docs/release/java/
      :link-type: url
      :class-card: sw-card-frc

      Full Javadoc for WPILibJ classes and methods.

   .. grid-item-card:: C++ API Reference
      :link: https://github.wpilib.org/allwpilib/docs/release/cpp/
      :link-type: url
      :class-card: sw-card-frc

      Doxygen documentation for WPILibC.

   .. grid-item-card:: Python API Reference
      :link: https://robotpy.readthedocs.io/projects/robotpy/en/stable/
      :link-type: url
      :class-card: sw-card-frc

      RobotPy documentation for Python-based robot programs.
