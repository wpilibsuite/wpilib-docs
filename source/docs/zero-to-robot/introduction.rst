.. include:: <isonum.txt>

# Zero to Robot

Welcome to WPILib, the standard programming library for *FIRST*\ |reg| Robotics Competition
(FRC\ |reg|) and FIRST Tech Challenge (FTC).
This guide gets you from parts on a table to a driving robot.

.. important::

   **Release timeline:** Systemcore launches for the **2027 FRC season in
   January 2027**. FTC support launches in **fall 2027** for the **2027-2028
   FTC season**. Alpha and Beta teams may be able to use the hardware earlier,
   but those testing workflows are not the production competition release.

.. rubric:: Choose How You Will Program
   :class: wl-shared-text

Make two choices before installing anything. First choose where you want to
write code, then choose one of the languages available there. Both environments
work for FRC and FTC.

**Choice 1: Programming environment**

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: OnBot: Program in a Browser
      :class-card: sw-card-shared

      **Nothing to install for coding**
      ^^^
      Open the editor hosted by Systemcore from a browser. Choose Java,
      Blocks, Python, or LabVIEW.

   .. grid-item-card:: Desktop: Program in VS Code
      :class-card: sw-card-shared

      **Full desktop development tools**
      ^^^
      Install WPILib and write code on your computer. Choose Java, Blocks,
      C++, or Python.

**Choice 2: Programming language**

Every listed language is a supported team choice. Pick the style that fits
your team; you can change later without changing the robot hardware.

.. list-table::
   :header-rows: 1
   :widths: 13 18 13 13 22 21

   * - Language
     - Style
     - OnBot
     - Desktop
     - Best for
     - Notes
   * - **Java**
     - Text, statically typed
     - ✓
     - ✓
     - New teams, most teams
     - Most community examples
   * - **Blocks (Blockly)**
     - Graphical blocks
     - ✓
     - ✓
     - Teams that prefer visual programming
     - Outputs Python under the hood
   * - **C++**
     - Text, statically typed
     - ✗
     - ✓
     - Teams that already know C++
     - Highest performance; manual memory management adds
       complexity for beginners
   * - **Python**
     - Text, dynamically typed
     - ✓
     - ✓
     - Teams already using Python
     - Easiest syntax; growing set of community examples
   * - **LabVIEW**
     - Graphical (dataflow)
     - ✓
     - ✗
     - Teams with a LabVIEW background
     - Graphical dataflow programming

The table describes the planned 2027 Systemcore workflow. Until that
workflow is released, FTC teams using the REV Control Hub should follow
the `current FTC programming-tool guide
<https://ftc-docs.firstinspires.org/en/latest/programming_resources/shared/choosing_program_lang/choosing-program-lang.html>`_.
It supports Blocks, OnBot Java, and Android Studio; its instructions are
not interchangeable with the Systemcore instructions in this guide.

On Systemcore, LabVIEW is available through OnBot only, while C++ is available
through desktop development only. Step 2 gives setup instructions for the
environment you choose.

.. tip::

   **New to programming entirely?** No programming experience is required.
   This guide introduces variables, objects, methods, and control flow as you
   build and test the robot. If you want a full course alongside the guide, try
   `Codecademy Java <https://www.codecademy.com/learn/learn-java>`_ or
   `Python learning guides <http://docs.python-guide.org/en/latest/intro/learning/>`_.

.. rubric:: What You Need
   :class: wl-shared-text

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: FRC Robot Components
      :class-card: sw-card-frc

      **FRC Hardware**
      ^^^
      - Systemcore controller
      - Power Distribution Hub (PDH) or Panel (PDP)
      - Vivid VH-109 Radio (powered directly from robot battery voltage; no VRM required)
      - 18 AWG wire for VH-109 power
      - Motor controllers (SPARK MAX, Talon FX, etc.)
      - Drive motors and wheels
      - 12 V robot battery and fuse
      - Ethernet cable and a USB cable that matches the Systemcore's USB device port

   .. grid-item-card:: FTC Robot Components
      :class-card: sw-card-ftc

      **FTC Hardware**
      ^^^
      - Systemcore + Motioncore controllers
      - FTC legal motor controllers
      - Drive motors and wheels
      - 12 V robot battery
      - USB-C cable for programming
      - Wi-Fi for wireless deploy

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: What Gets Installed
      :class-card: sw-card-shared

      **Software: Only If You Need It**
      ^^^
      OnBot teams don't need to download anything to write code. You only
      need desktop software if you're not using OnBot, or if you're an
      FRC team that needs the Driver Station.

      - **WPILib**: robot programming library + VS Code, for desktop
        development
      - **FRC Driver Station**: required for FRC teams. Runs on Windows,
        macOS, and Linux, but only the Windows version is competition
        legal
      - **RobotPy**: Python framework, for desktop Python teams
      - Vendor libraries (REVLib, Phoenix 6, etc.), installed per project

   .. grid-item-card:: Practice with the XRP
      :link: ../xrp-robot/index
      :link-type: doc
      :class-card: sw-card-shared

      **No Full Robot Yet?**
      ^^^
      The XRP is a desktop robot that runs real WPILib code.
      Great for learning before build season, and for FTC teams
      getting a head start on Systemcore programming.

.. rubric:: The Steps
   :class: wl-shared-text

For the complete **FRC VS Code path**, follow Steps 1 through 4 in order;
you will have a driving robot by the end of Step 4. The separate
Troubleshooting page is available whenever you get stuck. Systemcore
OnBot, Blockly, and FTC-specific paths are still being completed and are
clearly marked where they diverge.

.. note::

   **FTC teams:** Robot assembly and Motioncore-specific wiring arrive with
   the FTC launch in fall 2027 for the 2027-2028 season, but you don't need
   to wait to get started. Powering and connecting to the Systemcore
   (Step 1, Parts 2-3) and installing your tools (Step 2) already apply
   today. Practice with the :doc:`XRP robot <../xrp-robot/index>` in the
   meantime; the same WPILib code runs on Systemcore when your hardware
   is ready.

.. grid:: 1 2 4 4
   :gutter: 3

   .. grid-item-card:: Build and Wire Your Robot
      :link: step-1/index
      :link-type: doc
      :class-card: sw-card-shared

      **01**
      ^^^
      Wire the control system: power distribution, Systemcore,
      motor controllers, and radio.

   .. grid-item-card:: Set Up Your Environment
      :link: step-2/index
      :link-type: doc
      :class-card: sw-card-shared

      **02**
      ^^^
      Choose OnBot or VS Code, and get your Driver Station installed.

   .. grid-item-card:: Configure Your Control System
      :link: step-3/index
      :link-type: doc
      :class-card: sw-card-shared

      **03**
      ^^^
      Configure your Systemcore and radio. Required every season
      before you can deploy code.

   .. grid-item-card:: Write and Drive
      :link: step-4/index
      :link-type: doc
      :class-card: sw-card-shared

      **04**
      ^^^
      Create your first robot project, deploy code to the robot,
      and enable it with the Driver Station.

.. card:: Something not working? Open Troubleshooting →
   :link: step-5/index
   :link-type: doc
   :class-card: sw-card-shared

   Diagnose power, networking, communication, code, controller, and motor
   problems without leaving the Zero to Robot guide.

.. rubric:: Tips for New Teams
   :class: wl-shared-text

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item::

      .. tip::

         **Get driving first**

         Wire one drive motor per side, deploy arcade drive, and make sure
         the robot moves before adding anything else. Every mechanism you add
         before the robot drives is a variable you can't isolate.

   .. grid-item::

      .. tip::

         **Check the Driver Station log**

         When something goes wrong on the robot, open the Driver Station log
         viewer. It records exactly when the robot disconnected, what threw
         an exception, and why the robot disabled.

.. toctree::
   :maxdepth: 1
   :hidden:

   Step 1: Build and Wire Your Robot <step-1/index>
   Step 2: Set Up Your Environment <step-2/index>
   Step 3: Configure Your Control System <step-3/index>
   Step 4: Write and Drive <step-4/index>
   Troubleshooting <step-5/index>
