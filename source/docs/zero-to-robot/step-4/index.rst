# Step 4: Write and Drive

.. container:: sw-step-badge

   .. container:: sw-step-n

      04

   .. container::

      .. container:: sw-step-info-title

         Write and Drive

      .. container:: sw-step-info-sub

         Step 4 of 4

**By the end of this step:** you will create or open a drivetrain project in
your selected environment, put code on the robot, enable it safely, and drive.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Control System Ready
      :class-card: sw-card-shared

      - Step 3 is complete
      - Driver Station communication is green
      - Your controller is connected to the driver computer

   .. grid-item-card:: Test Area Ready
      :class-card: sw-card-shared

      - The drivetrain is securely supported with every wheel off the floor
      - People, tools, hair, and loose clothing are clear of moving parts
      - Someone is ready to turn off robot power

.. rubric:: Continue with Your Programming Choice

Use the same environment and language you selected on the Zero to Robot page
and set up in Step 2. Both environments are supported for FRC and FTC with
Systemcore.

.. tab-set::

   .. tab-item:: OnBot
      :sync: onbot

      OnBot runs in a browser hosted by Systemcore. Open the editor, then use
      the row for your language.

      .. list-table::
         :header-rows: 1
         :widths: 18 22 60

         * - Language
           - Availability
           - Next action
         * - **Java**
           - Available
           - Create a Java project in OnBot. The Systemcore-specific guided
             walkthrough is in progress.
         * - **Blocks**
           - Available
           - Open :ref:`blocks-drivetrain-samples`, then create an editable
             copy from :guilabel:`Samples...` in the Blocks interface.
         * - **C++**
           - Desktop only
           - Select the **Desktop / VS Code** tab.
         * - **Python**
           - Available
           - Create a Python project in OnBot. The Systemcore-specific guided
             walkthrough is in progress.
         * - **LabVIEW**
           - Available
           - Create a LabVIEW project in OnBot. The Systemcore-specific guided
             walkthrough is in progress.

      .. note::

         Current FTC Control Hub users should follow the
         `official FTC programming tutorials
         <https://ftc-docs.firstinspires.org/en/latest/programming_resources/index.html>`_.
         Those connection and deployment steps do not apply to Systemcore.

   .. tab-item:: Desktop / VS Code
      :sync: vscode

      The desktop path uses WPILib VS Code and the tools installed in Step 2.

      .. list-table::
         :header-rows: 1
         :widths: 18 22 60

         * - Language
           - Availability
           - Next action
         * - **Java**
           - Available
           - Follow the :doc:`drivetrain walkthrough
             <creating-test-drivetrain-program-cpp-java-python>` below.
         * - **Blocks**
           - Available
           - Open :ref:`blocks-drivetrain-samples`, then create an editable
             copy from :guilabel:`Samples...` in the Blocks interface.
         * - **C++**
           - Available
           - Follow the :doc:`drivetrain walkthrough
             <creating-test-drivetrain-program-cpp-java-python>` below.
         * - **Python**
           - Available
           - Follow the :doc:`drivetrain walkthrough
             <creating-test-drivetrain-program-cpp-java-python>` below.
         * - **LabVIEW**
           - OnBot only
           - Select the **OnBot** tab.

.. rubric:: Desktop / VS Code Path

The five parts below apply to desktop Java, C++, and Python projects. Desktop
Blocks teams should start from a drivetrain sample, then rejoin at Part 4 to
deploy. OnBot teams should use their editor's save and deploy workflow, then
rejoin at Part 5 for the shared safety and driving checks.

.. rubric:: Desktop Part 1: Create Your Robot Project

Open the WPILib VS Code and create a new project from the template.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Create a Drivetrain Program
      :link: creating-test-drivetrain-program-cpp-java-python
      :link-type: doc
      :class-card: sw-card-shared

      **FRC + FTC: Java / C++ / Python**
      ^^^
      Step-by-step guide: new project, vendor libraries, arcade drive
      code, and deploy to the robot.

   .. grid-item-card:: New Project Checklist

      **Quick reference**
      ^^^
      - Open WPILib VS Code (not system VS Code)
      - Press :kbd:`Ctrl+Shift+P` → *WPILib: Create a new project*
      - Choose **Template → TimedRobot**
      - Set team number and project folder
      - Add vendor libraries via *Manage Vendor Libraries*

.. rubric:: Desktop Part 2: Install Vendor Libraries

Vendor libraries add support for motor controllers and sensors.
They are per-project and must be added each time you create or import a
project.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Common Vendor Libraries

      - **REVLib**: SPARK MAX, SPARK Flex, and the 2027 A301 on Motioncore
      - **Phoenix 6**: Talon FX, CANcoder, Pigeon 2
      - **PathplannerLib**: autonomous trajectories
      - **PhotonLib**: PhotonVision camera support

   .. grid-item-card:: How to Add a Library

      - :kbd:`Ctrl+Shift+P` → *WPILib: Manage Vendor Libraries*
      - Select *Install new libraries (online)*
      - Paste the vendor JSON URL from their docs
      - Build the project to download dependencies

.. note::

   **Using an A301 with Motioncore?** Keep its firmware and REVLib versions
   compatible, and identify the Motioncore channel with ``CANBusMap`` rather
   than a raw integer. Motioncore channel D0 is not the same bus as Systemcore
   bus 0. See the current `A301 testing guide
   <https://github.com/wpilibsuite/SystemcoreTesting/blob/main/A301.md>`_
   for the required version pair and channel examples.

.. rubric:: Desktop Part 3: Basic Arcade Drive

A minimal drivetrain has three long-lived objects: the two motor controllers
and the ``DifferentialDrive``. Create them once as fields of the robot class
(or in its constructor), not inside ``teleopPeriodic()``. The periodic method
should only read the controller and command the existing drive object.

.. tab-set-code::

   ```java
   // Fields in the Robot class; construct these only once.
   private final PWMSparkMax leftMotor = new PWMSparkMax(0);
   private final PWMSparkMax rightMotor = new PWMSparkMax(1);
   private final DifferentialDrive drive =
       new DifferentialDrive(leftMotor::setThrottle, rightMotor::setThrottle);
   private final Gamepad controller = new Gamepad(0);

   @Override
   public void teleopPeriodic() {
       drive.arcadeDrive(-controller.getLeftY(), -controller.getRightX());
   }
   ```

   ```c++
   // Members of the Robot class; construct these only once.
   wpi::PWMSparkMax leftMotor{0};
   wpi::PWMSparkMax rightMotor{1};
   wpi::DifferentialDrive drive{
       [&](double output) { leftMotor.SetThrottle(output); },
       [&](double output) { rightMotor.SetThrottle(output); }};
   wpi::Gamepad controller{0};

   void Robot::TeleopPeriodic() {
     drive.ArcadeDrive(-controller.GetLeftY(), controller.GetRightX());
   }
   ```

   ```python
   def __init__(self):
       super().__init__()
       # Construct hardware objects only once, during robot startup.
       self.left_motor = wpilib.PWMSparkMax(0)
       self.right_motor = wpilib.PWMSparkMax(1)
       self.drive = wpilib.DifferentialDrive(
           self.left_motor, self.right_motor
       )
       self.controller = wpilib.Gamepad(0)

   def teleopPeriodic(self):
       self.drive.arcadeDrive(
           -self.controller.getLeftY(), -self.controller.getRightX()
       )
   ```

.. card:: Full drivetrain walkthrough →
   :link: creating-test-drivetrain-program-cpp-java-python
   :link-type: doc
   :class-card: sw-card-shared

   Complete guide: project setup, motor controller configuration,
   and deploy steps for Java, C++, and Python.

.. important::

   The snippets above show object placement and control flow, but omit imports,
   class declarations, motor inversion, and safety setup. Start from the tested
   complete example in the full drivetrain walkthrough rather than pasting an
   isolated snippet into an empty file.

.. rubric:: Desktop Part 4: Deploy to the Robot

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Deploy over Wi-Fi

      Connect to the robot Wi-Fi network (XXXX_Robot), then press
      :kbd:`Ctrl+Shift+P` → *WPILib: Deploy Robot Code*.

   .. grid-item-card:: Deploy over USB

      Connect the laptop to the Systemcore's USB device port with the
      appropriate data-capable cable.
      WPILib auto-detects USB and deploys without Wi-Fi.

.. TODO: Add a screenshot of a successful WPILib deploy terminal showing that
   robot code started.

.. card:: Running and testing your program →
   :link: running-test-program
   :link-type: doc
   :class-card: sw-card-frc

   Connect Driver Station, plug in joystick, verify robot code
   is running, and enable teleop for the first time.

.. rubric:: Shared Part 5: Enable and Drive

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Pre-enable checklist

      - First test: robot safely elevated with every drive wheel off the floor
      - All team members clear of moving parts
      - Driver Station shows "Robot Code" (green)
      - Joystick connected and recognized in DS
      - Driver Station reports a plausible robot battery voltage

   .. grid-item-card:: FRC enable steps

      - Open FRC Driver Station
      - Select **TeleOperated** mode
      - Announce that the robot is about to enable, then click **Enable**
      - Move joystick: robot should respond
      - Click **Disable** or press :kbd:`Enter` to stop

   .. grid-item-card:: FTC enable steps

      - Open the FTC Driver Station software
      - Select and initialize your TeleOp program
      - Announce that the robot is about to start, then start the program
      - Move the controller: robot should respond
      - Stop the program before approaching the robot

.. TODO: Add a screenshot showing the controller recognized and the robot ready
   to enable in Driver Station.

.. warning::

   **FRC Driver Station:** the :kbd:`Space` bar triggers **Emergency Stop**;
   it is not the ordinary disable shortcut. An emergency-stopped robot must be
   rebooted before it can be enabled again.

.. tip::

   **Something not working?** See :doc:`Troubleshooting <../step-5/index>`.

.. container:: sw-success

   .. container:: sw-success-h

      ✓ You have a driving robot.

   Explore the
   :doc:`Command-Based framework <../../software/commandbased/index>`
   for structured programs,
   :doc:`path planning <../../software/pathplanning/index>`
   for autonomous, and
   :doc:`simulation <../../software/wpilib-tools/robot-simulation/index>`
   to test code without hardware.

.. container:: sw-nav

   :doc:`← Step 3: Configure Your Control System <../step-3/index>`

.. toctree::
   :maxdepth: 1
   :hidden:

   creating-test-drivetrain-program-cpp-java-python
   running-test-program
