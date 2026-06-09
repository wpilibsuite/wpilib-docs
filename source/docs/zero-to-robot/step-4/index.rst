# Step 4: Write and Drive

.. raw:: html


   <div class="sw-step-badge">
     <span class="sw-step-n">04</span>
     <div>
       <div class="sw-step-info-title">Write and Drive</div>
       <div class="sw-step-info-sub">
         Step 4 of 4 &mdash; Estimated time: 45 min
       </div>
     </div>
   </div>

   <p class="sw-section-h">Part 1 &mdash; Create Your Robot Project</p>
   <p style="font-size:0.875rem;margin-bottom:14px;
      color:var(--color-foreground-secondary,#555);">
     Open the WPILib VS Code and create a new project from the template.
   </p>

   <div class="sw-grid sw-grid-2">
     <a class="sw-card sw-card-frc"
        href="creating-test-drivetrain-program-cpp-java-python.html">
       <div class="sw-label sw-label-frc">Java / C++ / Python</div>
       <div class="sw-card-title">Create a Drivetrain Program</div>
       <div class="sw-card-desc">
         Step-by-step guide: new project, vendor libraries, arcade drive
         code, and deploy to the robot.
       </div>
     </a>
     <div class="sw-card">
       <div class="sw-label sw-label-frc">Quick reference</div>
       <div class="sw-card-title">New Project Checklist</div>
       <ul class="sw-list">
         <li>Open WPILib VS Code (not system VS Code)</li>
         <li>Press <strong>Ctrl+Shift+P</strong> &rarr;
           <em>WPILib: Create a new project</em></li>
         <li>Choose <strong>Template &rarr; TimedRobot</strong></li>
         <li>Set team number and project folder</li>
         <li>Add vendor libraries via
           <em>Manage Vendor Libraries</em></li>
       </ul>
     </div>
   </div>

   <p class="sw-section-h">Part 2 &mdash; Install Vendor Libraries</p>
   <p style="font-size:0.875rem;margin-bottom:14px;
      color:var(--color-foreground-secondary,#555);">
     Vendor libraries add support for motor controllers and sensors.
     They are per-project and must be added each time you create or import a project.
   </p>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card">
       <div class="sw-card-title">Common Vendor Libraries</div>
       <ul class="sw-list">
         <li><strong>REVLib</strong> &mdash; SPARK MAX and SPARK Flex</li>
         <li><strong>Phoenix 6</strong> &mdash; Talon FX, CANcoder, Pigeon 2</li>
         <li><strong>PathplannerLib</strong> &mdash; autonomous trajectories</li>
         <li><strong>PhotonLib</strong> &mdash; PhotonVision camera support</li>
       </ul>
     </div>
     <div class="sw-card">
       <div class="sw-card-title">How to Add a Library</div>
       <ul class="sw-list">
         <li><strong>Ctrl+Shift+P</strong> &rarr;
           <em>WPILib: Manage Vendor Libraries</em></li>
         <li>Select <em>Install new libraries (online)</em></li>
         <li>Paste the vendor JSON URL from their docs</li>
         <li>Build the project to download dependencies</li>
       </ul>
     </div>
   </div>

   <p class="sw-section-h">Part 3 &mdash; Basic Arcade Drive (Java)</p>
   <p style="font-size:0.875rem;margin-bottom:10px;
      color:var(--color-foreground-secondary,#555);">
     A minimal working drivetrain. Replace
     <code>PWMSparkMax</code> with your actual controller class.
   </p>

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

.. raw:: html

   <a class="sw-card sw-card-frc" style="margin-bottom:24px;"
      href="creating-test-drivetrain-program-cpp-java-python.html">
     <div class="sw-card-title">Full drivetrain walkthrough &rarr;</div>
     <div class="sw-card-desc">
       Complete guide: project setup, motor controller configuration,
       and deploy steps for Java, C++, and Python.
     </div>
   </a>

   <p class="sw-section-h">Part 4 &mdash; Deploy to the Robot</p>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card">
       <div class="sw-card-title">Deploy over Wi-Fi</div>
       <div class="sw-card-desc">
         Connect to the robot Wi-Fi network (XXXX_Robot), then press
         <strong>Ctrl+Shift+P &rarr; WPILib: Deploy Robot Code</strong>.
       </div>
     </div>
     <div class="sw-card">
       <div class="sw-card-title">Deploy over USB</div>
       <div class="sw-card-desc">
         Connect USB-A to USB-B from laptop to Systemcore.
         WPILib auto-detects USB and deploys without Wi-Fi.
       </div>
     </div>
   </div>

   <a class="sw-card sw-card-frc" style="margin-bottom:24px;"
      href="running-test-program.html">
     <div class="sw-card-title">Running and testing your program &rarr;</div>
     <div class="sw-card-desc">
       Connect Driver Station, plug in joystick, verify robot code
       is running, and enable teleop for the first time.
     </div>
   </a>

   <p class="sw-section-h">Part 5 &mdash; Enable and Drive</p>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card">
       <div class="sw-card-title">Pre-enable checklist</div>
       <ul class="sw-list">
         <li>Robot on floor or safely elevated</li>
         <li>All team members clear of moving parts</li>
         <li>Driver Station shows &ldquo;Robot Code&rdquo; (green)</li>
         <li>Joystick connected and recognized in DS</li>
         <li>Battery voltage above 12.0&thinsp;V</li>
       </ul>
     </div>
     <div class="sw-card">
       <div class="sw-card-title">Enable steps</div>
       <ul class="sw-list">
         <li>Open FRC Driver Station</li>
         <li>Select <strong>TeleOperated</strong> mode</li>
         <li>Click <strong>Enable</strong> (or press Enter)</li>
         <li>Move joystick &mdash; robot should respond</li>
         <li>Press <strong>Disable</strong> (or Spacebar) to stop</li>
       </ul>
     </div>
   </div>

   <p class="sw-section-h">Troubleshooting</p>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card sw-card-err">
       <div class="sw-card-title">&ldquo;No Robot Communication&rdquo;</div>
       <div class="sw-card-desc">Check Wi-Fi connection to robot network.
         Verify Systemcore and radio are powered. Try USB deploy cable as a
         fallback.</div>
     </div>
     <div class="sw-card sw-card-err">
       <div class="sw-card-title">&ldquo;No Robot Code&rdquo;</div>
       <div class="sw-card-desc">Code was not deployed or crashed on startup.
         Re-deploy from VS Code. Check the Driver Station log for
         exceptions.</div>
     </div>
     <div class="sw-card sw-card-err">
       <div class="sw-card-title">Robot does not move</div>
       <div class="sw-card-desc">Verify joystick axis mapping in Driver
         Station USB tab. Confirm motor controller wiring and correct PWM
         port numbers in code.</div>
     </div>
     <div class="sw-card sw-card-err">
       <div class="sw-card-title">Robot moves in wrong direction</div>
       <div class="sw-card-desc">Invert one motor controller in code
         (<code>motor.setInverted(true)</code>) or flip the motor power
         leads on the controller.</div>
     </div>
   </div>

   <div class="sw-success">
     <div class="sw-success-h">&#10003; You have a driving robot.</div>
     <p class="sw-success-p">
       Explore the
       <a href="../../software/commandbased/index.html">Command-Based
       framework</a> for structured programs,
       <a href="../../software/pathplanning/index.html">path planning</a>
       for autonomous, and
       <a href="../../software/wpilib-tools/robot-simulation/index.html">
       simulation</a> to test code without hardware.
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
