.. include:: <isonum.txt>

# FRC Control System Hardware Overview

This page summarizes every major hardware component in the FRC\ |reg| control system.
Use it as a reference when wiring or troubleshooting your robot.

.. note::

   **FRC + FTC:** This page covers the FRC control system.
   FTC teams using Systemcore and Motioncore (2027-2028+) share the same
   WPILib programming model — see the :doc:`FTC section <../../ftc/index>`
   for hardware specifics.

.. rubric:: Main Controller

.. card:: Systemcore
   :class-card: sw-card-frc

   **FRC 2027+ / FTC 2027-2028+**
   ^^^
   The primary robot controller for FRC (2027+) and FTC (2027-2028+).
   Runs robot code in Java, C++, or Python. Supports CAN, PWM, DIO,
   and analog I/O. Connects over Ethernet or USB for deployment and
   supports the full WPILib simulation framework.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Spec
     - Systemcore
   * - Languages
     - Java, C++, Python
   * - CAN bus
     - Yes
   * - PWM outputs
     - Yes
   * - DIO
     - Yes
   * - Analog inputs
     - Yes
   * - Connectivity
     - Ethernet, USB
   * - Deploy method
     - USB or Wi-Fi via VS Code / OnBot
   * - Simulation
     - Full desktop simulation support
   * - Programs
     - FRC (2027+) and FTC via Motioncore (2027-2028+)

.. rubric:: Power Distribution

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Power Distribution Hub (PDH)
      :class-card: sw-card-frc

      **REV Robotics**
      ^^^
      20 switchable high-current ports (40 A max each), 3 low-current
      ports, and a main breaker slot. CAN-connected for per-channel
      current monitoring. Rectangular form factor.

   .. grid-item-card:: Power Distribution Panel (PDP)
      :class-card: sw-card-frc

      **CTRE**
      ^^^
      16 high-current ports (40 A max each) plus 8 lower-current ports.
      CAN-connected for current monitoring. Oval form factor.
      Legal but older; PDH is preferred for new builds.

.. list-table::
   :header-rows: 1
   :widths: 34 33 33

   * - Feature
     - PDH (REV)
     - PDP (CTRE)
   * - High-current ports
     - 20 (40 A each)
     - 16 (40 A each)
   * - Low-current ports
     - 3 (20 A each)
     - 8 (20 A each)
   * - Main breaker slot
     - Yes (120 A SB)
     - Yes (120 A SB)
   * - CAN monitoring
     - Yes (per channel)
     - Yes (aggregate)
   * - Switchable outputs
     - Yes (software)
     - No

.. rubric:: Robot Radio

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Vivid VH109
      :class-card: sw-card-frc

      **FRC Standard**
      ^^^
      The standard FRC robot radio. Must be programmed annually with the
      FRC Radio Configuration Utility to set team number, SSID, and
      firmware. Powered via VRM barrel connector.

   .. grid-item-card:: OpenMesh OM5P-AC
      :class-card: sw-card-frc

      **FRC Legal**
      ^^^
      Updated version of the OM5P-AN with the same FRC configuration
      process. 802.11ac support. Preferred for new builds.

.. rubric:: Motor Controllers

.. list-table::
   :header-rows: 1
   :widths: 20 15 18 18 29

   * - Controller
     - Vendor
     - Interface
     - Max current
     - Notes
   * - **SPARK MAX**
     - REV
     - CAN or PWM
     - 40 A
     - Brushed and brushless (NEO). Most common for new teams.
   * - **SPARK Flex**
     - REV
     - CAN or PWM
     - 60 A
     - Higher current; NEO Vortex motor.
   * - **Talon FX**
     - CTRE
     - CAN
     - 120 A peak
     - Integrated with Falcon 500 and Kraken X60 motors.
   * - **Victor SPX**
     - CTRE
     - CAN or PWM
     - 40 A
     - Lower cost. Brushed only.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: CAN bus (recommended)

      Two-wire daisy-chain. Enables telemetry (current, temperature,
      velocity), firmware updates over the wire, and advanced
      closed-loop control on the controller itself. Requires correct
      termination at both ends of the chain.

   .. grid-item-card:: PWM (simpler fallback)

      Three-wire (signal, +5 V, GND) from Systemcore PWM port.
      No telemetry. Easier to debug. Acceptable for rookie builds
      or when CAN is not supported.

.. rubric:: Pneumatics

.. list-table::
   :header-rows: 1
   :widths: 24 14 22 18 22

   * - Module
     - Vendor
     - Solenoid channels
     - Pressure switch
     - Notes
   * - **Pneumatic Hub (PH)**
     - REV
     - 16 (CAN)
     - Analog + digital
     - Preferred for new builds. Analog pressure sensing.
   * - **PCM**
     - CTRE
     - 8 (CAN)
     - Digital only
     - Older module, still legal.

.. rubric:: Common Sensors

.. list-table::
   :header-rows: 1
   :widths: 28 20 34 18

   * - Sensor
     - Interface
     - Use case
     - Program
   * - **Quadrature encoder**
     - DIO (2 channels)
     - Wheel distance and velocity
     - FRC + XRP
   * - **NavX / Pigeon 2 IMU**
     - SPI / CAN
     - Heading, gyro, accelerometer
     - FRC
   * - **Limit switch**
     - DIO
     - Hard stop detection
     - FRC
   * - **Ultrasonic (ping-echo)**
     - DIO (2 channels)
     - Distance measurement
     - FRC + XRP
   * - **AprilTag camera**
     - USB / Ethernet
     - Field localization and pose estimation
     - FRC
   * - **Color sensor (REV)**
     - I2C
     - Game piece detection
     - FRC

.. rubric:: Other Components

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Voltage Regulator Module (VRM)
      :class-card: sw-card-frc

      **FRC**
      ^^^
      Powers the radio (12 V / 2 A) and other 5 V accessories.
      Plugs into a dedicated PDH/PDP port. Required for radio power
      on most builds.

   .. grid-item-card:: Driver Station Laptop
      :class-card: sw-card-frc

      **FRC**
      ^^^
      Windows 11 required (2027+). Runs the FRC Driver Station
      software to communicate with and enable the robot.
      Connected to robot radio over Wi-Fi at competition.

.. rubric:: What's Next

.. grid:: 1 1 2 3
   :gutter: 3

   .. grid-item-card:: Wiring Guide
      :link: ../../zero-to-robot/step-1/intro-to-frc-robot-wiring
      :link-type: doc
      :class-card: sw-card-frc

      Step-by-step control system wiring with diagrams.

   .. grid-item-card:: Image the Systemcore
      :link: ../../zero-to-robot/step-3/imaging-your-systemcore
      :link-type: doc
      :class-card: sw-card-frc

      Required every season before deploying code.

   .. grid-item-card:: Status Light Reference
      :link: status-lights-ref
      :link-type: doc
      :class-card: sw-card-frc

      Decode LED patterns on the Systemcore, radio, and motor
      controllers.
