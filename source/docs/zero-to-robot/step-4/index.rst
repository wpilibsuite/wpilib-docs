# Step 4: Write and Drive

.. container:: sw-step-badge

   .. container:: sw-step-n

      04

   .. container::

      .. container:: sw-step-info-title

         Write and Drive

      .. container:: sw-step-info-sub

         Step 4 of 4

Create or open a drivetrain project, deploy it to Systemcore, and test it
with the drive wheels off the floor. Use the editor and language you set up
in Step 2.

.. note::

   FRC KitBot example code will be available after the 2027 kickoff.

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

Choose your environment below. The VS Code card opens the full drivetrain
walkthrough; the Blocks card opens the project-creation guide. OnBot and
LabVIEW walkthroughs are still being completed.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Java, C++, or Python in VS Code
      :link: creating-test-drivetrain-program-cpp-java-python
      :link-type: doc
      :class-card: sw-card-shared

      Create a project, configure the motor controllers, and deploy using
      the full drivetrain walkthrough. C++ uses desktop development only.

   .. grid-item-card:: Blocks
      :link: create_blocks_project
      :link-type: ref
      :class-card: sw-card-shared

      Start with a drivetrain sample in the Blocks editor. Choose the sample
      for your hardware, make an editable copy, and check its configuration.
      More drivetrain examples for Blocks are coming soon.

   .. grid-item-card:: Java or Python in OnBot
      :class-card: sw-card-shared

      Open the editor hosted by Systemcore. The detailed project-creation
      and deployment walkthroughs are still being completed.

   .. grid-item-card:: LabVIEW: OnBot or Desktop
      :class-card: sw-card-shared

      Use the LabVIEW environment you selected in Step 2. The Systemcore
      project-creation and deployment walkthroughs for both environments
      are still being completed.

.. rubric:: Desktop / VS Code Path

For **Java, C++, or Python in VS Code**, follow Parts 1 through 5 below.

For **Blocks**, create your project from a drivetrain sample, then
continue with :ref:`deployment <first-drive-deploy>` in Part 4.

For **OnBot**, save and deploy in your browser editor, then continue with
:ref:`the driving checks <first-drive-enable>` in Part 5.

For **desktop LabVIEW**, save and deploy your code from LabVIEW, then continue
with :ref:`the driving checks <first-drive-enable>` in Part 5.

.. rubric:: Desktop Part 1: Create Your Robot Project

Open WPILib VS Code. Use the linked walkthrough for the complete project;
the checklist below summarizes the setup steps.

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

Vendor libraries provide code for motor controllers and sensors, as well as
software features such as autonomous path following and vision processing.

Add the libraries your project uses each time you create or import it.
See :doc:`Managing Vendor Dependencies
</docs/software/vscode-overview/3rd-party-libraries>` for installation and
update instructions.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Common Vendor Libraries

      - **REVLib**: SPARK MAX, SPARK Flex, and the 2027 A301 on Motioncore
      - **Phoenix 6**: Talon FX, CANcoder, Pigeon 2
      - **Choreo**: autonomous trajectories
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

A minimal drivetrain has three objects: the two motor controllers
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

.. _first-drive-deploy:

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

   Connect the Driver Station and controller, check that robot code
   is running, and test teleop with the drive wheels off the floor.

.. _first-drive-enable:

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

   **Something not working?** See :doc:`Troubleshooting </docs/software/support/troubleshooting>`.

.. container:: sw-success

   .. container:: sw-success-h

      ✓ First drive test complete.

   Use the
   :doc:`Command-Based framework <../../software/commandbased/index>`
   to organize code for more mechanisms,
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
