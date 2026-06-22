.. include:: <isonum.txt>

# Getting Started with XRP

The XRP (eXperimental Robot Platform), powered by
`Worcester Polytechnic Institute <http://wpi.edu>`_, is a small, low-cost robot
designed for learning WPILib programming without full FRC hardware.
The same tools, language, and code patterns used for full FRC robots
work on the XRP.

.. rubric:: Why Use the XRP?

.. grid:: 1 2 2 4
   :gutter: 3

   .. grid-item-card:: Real WPILib Code
      :class-card: sw-card-shared

      **Learn**
      ^^^
      Write the same Java, C++, or Python code you would deploy to
      a full FRC robot.

   .. grid-item-card:: No Control System Required
      :class-card: sw-card-shared

      **Practice**
      ^^^
      No roboRIO, no PDH, no radio programming. Just the XRP,
      a USB cable for initial setup, and your laptop.

   .. grid-item-card:: Off-Season Programming
      :class-card: sw-card-shared

      **Pre-season**
      ^^^
      Learn command-based programming, encoders, PID, and odometry
      before build season starts — on a desk.

   .. grid-item-card:: FTC Prep
      :class-card: sw-card-ftc

      **FTC 2027-2028+**
      ^^^
      Systemcore teams use the same WPILib toolchain. XRP skills
      transfer directly to FTC robot programming.

.. rubric:: How It Works

.. tip::

   XRP code runs on your **laptop as a simulation**, communicating
   with the XRP hardware over Wi-Fi. You use the same
   **WPILib VS Code tools and Driver Station** as FRC —
   the XRP just appears as a simulated robot that drives real motors.

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: Create an XRP project

      Use the WPILib VS Code extension you already installed.
      XRP projects use the same project structure as FRC.

   .. grid-item-card:: Run as simulation

      Launch with **Simulate Robot Code** instead of Deploy.
      The simulation connects to the XRP over Wi-Fi.

   .. grid-item-card:: Drive with Driver Station

      Open the FRC Driver Station (Windows) and enable TeleOp.
      Your joystick controls the XRP just like a full robot.

.. rubric:: Hardware Specifications

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Component
     - Details
   * - **Processor**
     - Raspberry Pi RP2040 dual-core Cortex-M0+ at 133 MHz
   * - **Wireless**
     - Wi-Fi 802.11 b/g/n (2.4 GHz) for host communication
   * - **Drive motors**
     - 2 brushed DC gear motors with integrated quadrature encoders
   * - **IMU**
     - Built-in 6-axis LSM6DS3 (gyro + accelerometer)
   * - **Servo ports**
     - 2 user servo outputs
   * - **User I/O**
     - Reflectance sensor, ultrasonic distance sensor port
   * - **Power**
     - USB-C or 3×AA battery pack
   * - **Cost**
     - ~$75 USD assembled (WPI / SparkFun)

.. rubric:: XRP vs Full FRC Robot

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Feature
     - XRP
     - FRC Robot
   * - WPILib API
     - ✓ Same Java/C++/Python API
     - ✓ Full API
   * - Command-based
     - ✓ Yes
     - ✓ Yes
   * - Encoders
     - ✓ Integrated
     - External (per motor controller)
   * - IMU / gyro
     - ✓ Built-in
     - External (NavX, Pigeon 2)
   * - Driver Station
     - ✓ Same (Windows)
     - ✓ Same (Windows)
   * - Deploy method
     - Simulate (Wi-Fi to laptop)
     - Deploy to Systemcore
   * - CAN bus
     - ✗ Not available
     - ✓ Full CAN support
   * - Vendor libraries
     - Not applicable
     - REVLib, Phoenix 6, etc.
   * - Cost
     - ~$75
     - $3,000–$10,000+

.. rubric:: Prerequisites

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Software (all platforms)

      - :doc:`WPILib installed <../zero-to-robot/step-2/wpilib-setup>`
      - FRC Driver Station (Windows — for enabling)
      - XRP firmware flashed on the board

   .. grid-item-card:: Hardware

      - XRP robot kit (assembled)
      - USB-C cable (for initial firmware flash)
      - 3×AA batteries or USB-C power bank
      - 2.4 GHz Wi-Fi on your laptop

.. rubric:: Getting Started

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: Set Up Hardware
      :link: hardware-and-imaging
      :link-type: doc
      :class-card: sw-card-shared

      **01**
      ^^^
      Flash XRP firmware, insert batteries, and connect to the XRP
      Wi-Fi network.

   .. grid-item-card:: Get to Know the XRP
      :link: getting-to-know-xrp
      :link-type: doc
      :class-card: sw-card-shared

      **02**
      ^^^
      Sensor locations, motor wiring, the web UI, and what each
      I/O port is for.

   .. grid-item-card:: Write and Run Code
      :link: programming-xrp
      :link-type: doc
      :class-card: sw-card-shared

      **03**
      ^^^
      Create an XRP project in WPILib VS Code, run the simulation,
      and drive your robot.

.. rubric:: Example Projects

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: XRP Arcade Drive
      :link: programming-xrp
      :link-type: doc
      :class-card: sw-card-frc

      Basic teleop drive using a joystick. Good first project.

   .. grid-item-card:: Sensors and Encoders
      :link: hardware-support
      :link-type: doc
      :class-card: sw-card-frc

      Read encoder distances, gyro heading, and reflectance sensor.

.. tip::

   **WPI XRP Curriculum available.**
   `WPI XRP Curriculum <https://wp.wpi.edu/xrp/curriculum/>`_
   covers setup, programming, and hands-on activities for the XRP robot.

.. toctree::
   :maxdepth: 1
   :hidden:

   hardware-and-imaging
   getting-to-know-xrp
   hardware-support
   web-ui
   programming-xrp
