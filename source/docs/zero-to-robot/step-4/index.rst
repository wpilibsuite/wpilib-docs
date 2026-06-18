# Step 4: Write and Drive

.. raw:: html

   <div class="sw-step-badge">
     <span class="sw-step-n">04</span>
     <div>
       <div class="sw-step-info-title">Write and Drive</div>
       <div class="sw-step-info-sub">Step 4 of 4 &mdash; Estimated time: 45 min</div>
     </div>
   </div>

.. rubric:: Part 1 — Create Your Robot Project

Open the WPILib VS Code and create a new project from the template.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Create a Drivetrain Program
      :link: creating-test-drivetrain-program-cpp-java-python
      :link-type: doc
      :class-card: sw-card-frc

      **Java / C++ / Python**
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

.. rubric:: Part 2 — Install Vendor Libraries

Vendor libraries add support for motor controllers and sensors.
They are per-project and must be added each time you create or import a project.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Common Vendor Libraries

      - **REVLib** — SPARK MAX and SPARK Flex
      - **Phoenix 6** — Talon FX, CANcoder, Pigeon 2
      - **PathplannerLib** — autonomous trajectories
      - **PhotonLib** — PhotonVision camera support

   .. grid-item-card:: How to Add a Library

      - :kbd:`Ctrl+Shift+P` → *WPILib: Manage Vendor Libraries*
      - Select *Install new libraries (online)*
      - Paste the vendor JSON URL from their docs
      - Build the project to download dependencies

.. rubric:: Part 3 — Basic Arcade Drive (Java)

A minimal working drivetrain. Replace ``PWMSparkMax`` with your actual controller class.

.. code-block:: java

   // In Robot.java — inside teleopPeriodic()
   PWMSparkMax leftMotor  = new PWMSparkMax(0);
   PWMSparkMax rightMotor = new PWMSparkMax(1);
   DifferentialDrive drive = new DifferentialDrive(leftMotor, rightMotor);

   @Override
   public void teleopPeriodic() {
       // left stick Y = speed, right stick X = rotation
       drive.arcadeDrive(-m_stick.getY(), m_stick.getX());
   }

.. card:: Full drivetrain walkthrough →
   :link: creating-test-drivetrain-program-cpp-java-python
   :link-type: doc
   :class-card: sw-card-frc

   Complete guide: project setup, motor controller configuration,
   and deploy steps for Java, C++, and Python.

.. rubric:: Part 4 — Deploy to the Robot

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Deploy over Wi-Fi

      Connect to the robot Wi-Fi network (XXXX_Robot), then press
      :kbd:`Ctrl+Shift+P` → *WPILib: Deploy Robot Code*.

   .. grid-item-card:: Deploy over USB

      Connect USB-A to USB-B from laptop to Systemcore.
      WPILib auto-detects USB and deploys without Wi-Fi.

.. card:: Running and testing your program →
   :link: running-test-program
   :link-type: doc
   :class-card: sw-card-frc

   Connect Driver Station, plug in joystick, verify robot code
   is running, and enable teleop for the first time.

.. rubric:: Part 5 — Enable and Drive

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Pre-enable checklist

      - Robot on floor or safely elevated
      - All team members clear of moving parts
      - Driver Station shows "Robot Code" (green)
      - Joystick connected and recognized in DS
      - Battery voltage above 12.0 V

   .. grid-item-card:: Enable steps

      - Open FRC Driver Station
      - Select **TeleOperated** mode
      - Click **Enable** (or press Enter)
      - Move joystick — robot should respond
      - Press **Disable** (or Spacebar) to stop

.. rubric:: Troubleshooting

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: "No Robot Communication"
      :class-card: sw-card-err

      Check Wi-Fi connection to robot network.
      Verify Systemcore and radio are powered. Try USB deploy cable as a fallback.

   .. grid-item-card:: "No Robot Code"
      :class-card: sw-card-err

      Code was not deployed or crashed on startup.
      Re-deploy from VS Code. Check the Driver Station log for exceptions.

   .. grid-item-card:: Robot does not move
      :class-card: sw-card-err

      Verify joystick axis mapping in Driver Station USB tab.
      Confirm motor controller wiring and correct PWM port numbers in code.

   .. grid-item-card:: Robot moves in wrong direction
      :class-card: sw-card-err

      Invert one motor controller in code (``motor.setInverted(true)``)
      or flip the motor power leads on the controller.

.. raw:: html

   <div class="sw-success">
     <div class="sw-success-h">&#10003; You have a driving robot.</div>
     <p class="sw-success-p">
       Explore the
       <a href="../../software/commandbased/index.html">Command-Based framework</a>
       for structured programs,
       <a href="../../software/pathplanning/index.html">path planning</a>
       for autonomous, and
       <a href="../../software/wpilib-tools/robot-simulation/index.html">simulation</a>
       to test code without hardware.
     </p>
   </div>

   <div class="sw-nav">
     <a class="sw-nav-btn" href="../step-3/index.html">
       &larr; Step 3: Configure Your Control System</a>
   </div>

.. toctree::
   :maxdepth: 1
   :hidden:

   creating-test-drivetrain-program-cpp-java-python
   running-test-program
