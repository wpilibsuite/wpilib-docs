.. include:: <isonum.txt>

# Zero to Robot: Introduction

Welcome to WPILib — the standard programming library for *FIRST*\ |reg| Robotics Competition
(FRC\ |reg|) and FIRST Tech Challenge (FTC).
This guide walks you through everything you need to start driving a robot.

.. rubric:: Choose Your Programming Language

WPILib supports multiple languages. Pick one: your tools and steps are the same regardless of choice.

.. grid:: 1 2 3 5
   :gutter: 3

   .. grid-item-card:: Java
      :class-card: sw-card-rec

      **Recommended — FRC + FTC**
      ^^^
      Statically typed, and has the most community examples.
      Best choice if you are unsure.

   .. grid-item-card:: C++
      :class-card: sw-card-shared

      **FRC + FTC**
      ^^^
      Highest performance. Good choice if your team already knows C++.
      Memory management adds complexity for beginners.

   .. grid-item-card:: Python
      :class-card: sw-card-shared

      **FRC + FTC**
      ^^^
      Easiest syntax. Growing community examples. Best if your team
      already programs in Python and wants a gentle start.

   .. grid-item-card:: Blockly
      :class-card: sw-card-shared

      **FRC + FTC**
      ^^^
      Graphical interface, runs OnBot, outputs Python. Great for
      beginners with no prior syntax knowledge.

   .. grid-item-card:: LabVIEW
      :class-card: sw-card-shared

      **FRC + FTC**
      ^^^
      Graphical dataflow programming, runs OnBot. Familiar to teams
      with a LabVIEW background.

.. tip::

   **New to programming entirely?** Check out
   `Codecademy Java <https://www.codecademy.com/learn/learn-java>`_ or
   `Python learning guides <http://docs.python-guide.org/en/latest/intro/learning/>`_
   before continuing. You can wire and configure your robot first (Steps 1 and 3)
   while learning to code in parallel.

.. rubric:: What You Need

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: FRC Robot Components
      :class-card: sw-card-frc

      **FRC Hardware**
      ^^^
      - Systemcore controller
      - Power Distribution Hub (PDH) or Panel (PDP)
      - Vivid VH-109 Radio
      - Voltage Regulator Module (VRM) — for radio power
      - Motor controllers (SPARK MAX, Talon FX, etc.)
      - Drive motors and wheels
      - 12 V robot battery and fuse
      - Ethernet cable and USB-A cable

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

      **Software — All Teams**
      ^^^
      - **WPILib** — robot programming library + VS Code
      - **FRC Game Tools** — Driver Station *(Windows only)*
      - **RobotPy** — Python framework *(Python teams only)*
      - Vendor libraries (REVLib, Phoenix 6, etc.) — installed per project

      **OS note:** Driver Station requires Windows. Coding and simulation
      work on macOS and Linux.

   .. grid-item-card:: Practice with the XRP
      :link: ../xrp-robot/index
      :link-type: doc
      :class-card: sw-card-shared

      **No Full Robot? No Problem.**
      ^^^
      The XRP is a desktop robot that runs real WPILib code.
      Great for learning before build season — and for FTC teams
      getting a head start on Systemcore programming.

.. rubric:: The Four Steps

Complete these in order. You will have a driving robot by the end of Step 4.

.. grid:: 1 2 2 4
   :gutter: 3

   .. grid-item-card:: Build Your Robot
      :link: step-1/index
      :link-type: doc
      :class-card: sw-card-frc

      **01**
      ^^^
      Wire the control system: power distribution, Systemcore,
      motor controllers, and radio.

   .. grid-item-card:: Install Your Tools
      :link: step-2/index
      :link-type: doc
      :class-card: sw-card-frc

      **02**
      ^^^
      Install WPILib and Driver Station on your laptop.

   .. grid-item-card:: Configure Your Control System
      :link: step-3/index
      :link-type: doc
      :class-card: sw-card-frc

      **03**
      ^^^
      Configure your Systemcore and radio. Required every season
      before you can deploy code.

   .. grid-item-card:: Write and Drive
      :link: step-4/index
      :link-type: doc
      :class-card: sw-card-frc

      **04**
      ^^^
      Create your first robot project, deploy code to the robot,
      and enable it with the Driver Station.

.. rubric:: Tips for New Teams

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
