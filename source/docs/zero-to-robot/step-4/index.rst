# Step 4: Write and Drive

.. raw:: html

   <style>
   :root { --frc:#009CD7; --frc-light:#e6f6fc; --shared:#2e7d32; --shared-light:#f1f8f1; }
   .sw-label { display:inline-block; font-size:0.7rem; font-weight:700; text-transform:uppercase;
     letter-spacing:0.06em; padding:2px 8px; border-radius:4px; margin-bottom:10px; }
   .sw-label-frc { background:var(--frc); color:#fff; }
   .sw-label-shared { background:var(--shared); color:#fff; }
   .sw-section-h { font-size:0.85rem; font-weight:700; text-transform:uppercase;
     letter-spacing:0.06em; color:var(--color-foreground-secondary,#555);
     border-bottom:1px solid var(--color-background-border,#ddd);
     padding-bottom:7px; margin:28px 0 14px; }
   .sw-grid { display:grid; gap:12px; margin-bottom:24px; }
   .sw-grid-2 { grid-template-columns:repeat(2,1fr); }
   .sw-card { padding:18px 20px; border-radius:8px;
     border:2px solid var(--color-background-border,#ddd);
     background:var(--color-background-primary,#fff);
     text-decoration:none; color:inherit; display:block;
     transition:border-color 0.2s, box-shadow 0.2s; }
   a.sw-card:hover { box-shadow:0 2px 8px rgba(0,0,0,0.08);
     text-decoration:none; color:inherit; }
   a.sw-card:visited { color:inherit; text-decoration:none; }
   .sw-card-frc { border-color:rgba(0,156,215,0.3); }
   a.sw-card-frc:hover { border-color:var(--frc);
     box-shadow:0 2px 10px rgba(0,156,215,0.15); }
   .sw-card-err { border-color:rgba(211,47,47,0.3); background:#fff5f5; }
   .sw-card-title { font-weight:700; font-size:0.97rem; margin-bottom:4px; }
   .sw-card-desc { font-size:0.85rem; color:var(--color-foreground-secondary,#555);
     line-height:1.55; }
   .sw-step-badge { display:flex; align-items:center; gap:14px;
     background:var(--frc-light); border:2px solid var(--frc);
     border-radius:8px; padding:14px 20px; margin-bottom:28px; }
   .sw-step-n { font-size:2.2rem; font-weight:800; color:var(--frc);
     font-family:monospace; line-height:1; flex-shrink:0; }
   .sw-step-info-title { font-size:1rem; font-weight:700; margin-bottom:2px; }
   .sw-step-info-sub { font-size:0.85rem; color:var(--color-foreground-secondary,#555); }
   .sw-tip { background:var(--shared-light);
     border:1px solid rgba(46,125,50,0.3); border-radius:6px;
     padding:14px 18px; font-size:0.875rem; line-height:1.6;
     margin-bottom:20px; }
   .sw-warn { background:#fff8e1; border:1px solid rgba(255,160,0,0.4);
     border-radius:6px; padding:14px 18px; font-size:0.875rem;
     line-height:1.6; margin-bottom:20px; }
   .sw-success { background:var(--shared-light);
     border:2px solid var(--shared); border-radius:8px;
     padding:20px 24px; margin-top:28px; }
   .sw-success-h { font-size:1.1rem; font-weight:700;
     color:var(--shared); margin:0 0 8px; }
   .sw-success-p { font-size:0.875rem; line-height:1.6; margin:0; }
   .sw-nav { display:flex; justify-content:space-between;
     margin-top:32px; padding-top:16px;
     border-top:1px solid var(--color-background-border,#ddd); }
   .sw-nav-btn { padding:9px 20px; border-radius:6px; font-size:0.875rem;
     font-weight:600; text-decoration:none; border:2px solid var(--frc);
     color:var(--frc); background:var(--color-background-primary,#fff);
     transition:all 0.2s; }
   .sw-nav-btn:hover { background:var(--frc); color:#fff; text-decoration:none; }
   .sw-nav-btn:visited { color:var(--frc); }
   ul.sw-list { font-size:0.875rem; line-height:1.8; margin:8px 0 0;
     padding-left:20px; }
   @media(max-width:700px) { .sw-grid-2 { grid-template-columns:1fr; } }
   </style>

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
