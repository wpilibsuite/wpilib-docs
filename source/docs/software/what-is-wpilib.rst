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

.. raw:: html


   <!-- ── PATH SELECTOR ── -->
   <p class="sw-section-h">Which path are you on?</p>

   <div class="sw-grid sw-grid-3">

     <div class="sw-card sw-card-frc">
       <div class="sw-label sw-label-frc">FRC</div>
       <div class="sw-card-title">FIRST Robotics Competition</div>
       <div class="sw-card-desc">
         Full WPILib support. Java, C++, Python. Deploys to Systemcore.
         Driver Station on Windows required for competition.
       </div>
     </div>

     <div class="sw-card sw-card-shared">
       <div class="sw-label sw-label-shared">FRC + FTC</div>
       <div class="sw-card-title">XRP Practice Robot</div>
       <div class="sw-card-desc">
         Same WPILib code on a $75 desktop robot. No control system
         hardware required. Great for off-season learning and
         FTC Systemcore prep.
       </div>
     </div>

     <div class="sw-card sw-card-ftc">
       <div class="sw-label sw-label-ftc">FTC 2027-2028+</div>
       <div class="sw-card-title">FTC Systemcore</div>
       <div class="sw-card-desc">
         WPILib now supports FTC via Systemcore and Motioncore.
         Same Java/C++/Python toolchain as FRC &mdash; skills
         transfer directly.
       </div>
     </div>

   </div>

   <!-- ── WHAT WPILIB INCLUDES ── -->
   <p class="sw-section-h">What WPILib Includes</p>

   <table class="sw-tbl">
     <thead>
       <tr><th>Component</th><th>Description</th><th>FRC</th><th>FTC</th></tr>
     </thead>
     <tbody>
       <tr><td><strong>Robot library</strong></td>
         <td>Motor control, sensors, drive classes, kinematics</td>
         <td>&#10003;</td><td>&#10003; (Systemcore)</td></tr>
       <tr><td><strong>VS Code extension</strong></td>
         <td>Project templates, deploy, build, vendor manager</td>
         <td>&#10003;</td><td>&#10003;</td></tr>
       <tr><td><strong>Simulation framework</strong></td>
         <td>Run robot code on laptop without hardware</td>
         <td>&#10003;</td><td>&#10003; (XRP)</td></tr>
       <tr><td><strong>Glass dashboard</strong></td>
         <td>Real-time telemetry and field visualization</td>
         <td>&#10003;</td><td>&#10003;</td></tr>
       <tr><td><strong>Elastic dashboard</strong></td>
         <td>Configurable driver dashboard (replaces Shuffleboard)</td>
         <td>&#10003;</td><td>Planned</td></tr>
       <tr><td><strong>PathPlanner / Choreo</strong></td>
         <td>GUI path planning for autonomous</td>
         <td>&#10003;</td><td>Planned</td></tr>
       <tr><td><strong>OutlineViewer</strong></td>
         <td>NetworkTables browser</td>
         <td>&#10003;</td><td>&#10003;</td></tr>
       <tr><td><strong>Shuffleboard</strong></td>
         <td>Older dashboard
           <span class="sw-dep">Removed 2027</span></td>
         <td>&#10007;</td><td>&#10007;</td></tr>
     </tbody>
   </table>

   <!-- ── LANGUAGE COMPARISON ── -->
   <p class="sw-section-h">Language Comparison</p>

   <table class="sw-tbl">
     <thead>
       <tr>
         <th>Language</th><th>Recommended for</th>
         <th>Performance</th><th>Community examples</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <td><strong>Java</strong>
           <span class="sw-label sw-label-rec" style="margin:0 0 0 6px;">
             Recommended</span></td>
         <td>New teams, most teams</td>
         <td>Good</td><td>Most abundant</td></tr>
       <tr><td><strong>C++</strong></td>
         <td>Teams with C++ experience</td>
         <td>Best</td><td>Abundant</td></tr>
       <tr><td><strong>Python</strong></td>
         <td>Teams already using Python</td>
         <td>Good</td><td>Growing</td></tr>
     </tbody>
   </table>

   <div class="sw-tip">
     <strong>All three languages share the same API design.</strong>
     Class names and method names are kept identical or very close across
     Java, C++, and Python. Switching languages later is straightforward.
   </div>

   <!-- ── DEV ENVIRONMENT ── -->
   <p class="sw-section-h">Development Environments</p>

   <p style="font-size:0.875rem;margin-bottom:20px;
      color:var(--color-foreground-secondary,#555);">
     WPILib supports two families of development environment: a full
     <strong>desktop IDE</strong> and browser-based <strong>OnBot</strong>
     environments that run directly on the Systemcore with no local install.
   </p>

   <!-- Desktop -->
   <p style="font-size:0.8rem;font-weight:700;text-transform:uppercase;
      letter-spacing:0.05em;color:var(--frc);margin:0 0 10px;">
     Desktop Environment &mdash; Java, C++, Python
   </p>

   <div class="sw-card sw-card-frc" style="margin-bottom:8px;">
     <div class="sw-label sw-label-frc">Desktop</div>
     <div class="sw-card-title">Visual Studio Code + WPILib Extension</div>
     <div class="sw-card-desc" style="margin-bottom:12px;">
       All three languages use VS Code as the IDE, with the WPILib extension
       providing project templates, build tools, simulation, and vendor library
       management. Works on Windows, macOS, and Linux.
     </div>
     <table class="sw-tbl" style="margin-bottom:0;">
       <thead>
         <tr><th>Feature</th><th>Java</th><th>C++</th><th>Python</th></tr>
       </thead>
       <tbody>
         <tr><td><strong>IDE</strong></td>
           <td>VS Code</td><td>VS Code</td><td>VS Code</td></tr>
         <tr><td><strong>Build system</strong></td>
           <td>GradleRIO</td>
           <td>GradleRIO (open to change)</td>
           <td>More integrated experience</td></tr>
         <tr><td><strong>Desktop simulation</strong></td>
           <td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
         <tr><td><strong>Offline install</strong></td>
           <td>&#10003;</td><td>&#10003;</td><td>&#10003;</td></tr>
         <tr><td><strong>Deploy</strong></td>
           <td colspan="3">USB or Wi-Fi to Systemcore</td></tr>
       </tbody>
     </table>
   </div>

   <div class="sw-tip" style="margin-bottom:20px;">
     <strong>Python install experience:</strong> WPILib is actively working to
     provide a more integrated Python setup &mdash; reducing the number of
     separate steps compared to Java/C++.
     <strong>C++ build system:</strong> GradleRIO is the baseline; transitioning
     to an alternative build system is possible depending on community contributions.
   </div>

   <!-- OnBot -->
   <p style="font-size:0.8rem;font-weight:700;text-transform:uppercase;
      letter-spacing:0.05em;color:var(--frc);margin:0 0 10px;">
     OnBot Environments &mdash; Java, Python, Blockly, LabVIEW
   </p>

   <div class="sw-card sw-card-frc" style="margin-bottom:8px;">
     <div class="sw-label sw-label-frc">OnBot (Browser-based)</div>
     <div class="sw-card-title">VS Code-derived editor hosted on Systemcore</div>
     <div class="sw-card-desc" style="margin-bottom:12px;">
       OnBot environments run entirely in the browser &mdash; no local
       installation required. Code is written, saved, and deployed directly
       on the Systemcore. Supports multiple saved Workspaces with a Deploy
       button to choose which one runs.
     </div>
     <table class="sw-tbl" style="margin-bottom:0;">
       <thead>
         <tr><th>Feature</th><th>Java</th><th>Python</th><th>Blockly</th><th>LabVIEW</th></tr>
       </thead>
       <tbody>
         <tr><td><strong>Editor</strong></td>
           <td>VS Code-derived</td>
           <td>VS Code-derived</td>
           <td>Block visual editor</td>
           <td>Graphical (browser)</td></tr>
         <tr><td><strong>Backed by</strong></td>
           <td>Java</td><td>Python</td>
           <td>Python</td><td>LabVIEW</td></tr>
         <tr><td><strong>Beginner friendly</strong></td>
           <td>&mdash;</td><td>&mdash;</td>
           <td>&#10003; No syntax needed</td>
           <td>&#10003; Graphical</td></tr>
         <tr><td><strong>Desktop install</strong></td>
           <td colspan="4">None required</td></tr>
         <tr><td><strong>Simulation</strong></td>
           <td colspan="4">&#10007; Not planned</td></tr>
         <tr><td><strong>Multi-user</strong></td>
           <td colspan="4">Single-user (under investigation)</td></tr>
       </tbody>
     </table>
   </div>

   <div class="sw-warn" style="margin-bottom:20px;">
     <strong>C++ is not supported in OnBot environments.</strong>
     The browser-based toolchain does not provide a good enough C++ experience
     to ship. Use the desktop VS Code environment for C++ development.
     <br><br>
     <strong>OnBot notes:</strong> Currently planned as single-user access
     (multi-user being investigated). Supports multiple saved
     <em>Workspaces</em> with a Deploy button to select which one runs on
     the Systemcore. Simulation is not planned for OnBot environments.
   </div>

   <p style="font-size:0.8rem;font-weight:700;text-transform:uppercase;
      letter-spacing:0.05em;color:var(--ftc);margin:0 0 10px;">
     FTC REV Duo
   </p>
   <div class="sw-grid sw-grid-2" style="margin-bottom:24px;">
     <div class="sw-card sw-card-ftc">
       <div class="sw-label sw-label-ftc">FTC (REV Duo)</div>
       <div class="sw-card-title">OnBot Java / Android Studio</div>
       <div class="sw-card-desc">
         REV Duo teams use the FTC SDK with OnBot Java (browser-based)
         or Android Studio. Documented at
         <a href="https://ftc-docs.firstinspires.org">
         ftc-docs.firstinspires.org</a>.
       </div>
     </div>
     <div class="sw-card sw-card-ftc">
       <div class="sw-label sw-label-ftc">FTC (REV Duo)</div>
       <div class="sw-card-title">Blocks (FTC SDK)</div>
       <div class="sw-card-desc">
         Visual block-based programming via the FTC SDK OnBot interface.
         Documented at
         <a href="https://ftc-docs.firstinspires.org">
         ftc-docs.firstinspires.org</a>.
       </div>
     </div>
   </div>

   <!-- ── BUILD AND DEPLOY ── -->
   <p class="sw-section-h">Build and Deploy Comparison</p>

   <table class="sw-tbl">
     <thead>
       <tr>
         <th>Feature</th>
         <th>Desktop (VS Code)</th>
         <th>OnBot (Java / Python / Blockly / LabVIEW)</th>
         <th>FTC REV Duo</th>
       </tr>
     </thead>
     <tbody>
       <tr><td><strong>Languages</strong></td>
         <td>Java, C++, Python</td>
         <td>Java, Python, Blockly, LabVIEW</td>
         <td>Java, Blocks</td></tr>
       <tr><td><strong>C++ support</strong></td>
         <td>&#10003;</td>
         <td>&#10007; Not supported</td>
         <td>&#10007;</td></tr>
       <tr><td><strong>Build system</strong></td>
         <td>GradleRIO</td>
         <td>On-device (browser)</td>
         <td>FTC SDK / Gradle</td></tr>
       <tr><td><strong>Deploy</strong></td>
         <td>USB or Wi-Fi to Systemcore</td>
         <td>Deploy button in browser (Workspace-based)</td>
         <td>ADB over USB or Wi-Fi</td></tr>
       <tr><td><strong>Simulation</strong></td>
         <td>&#10003; Full desktop sim</td>
         <td>&#10007; Not planned</td>
         <td>&#10007; None</td></tr>
       <tr><td><strong>Offline install</strong></td>
         <td>&#10003;</td>
         <td>N/A &mdash; runs on Systemcore</td>
         <td>&#10003;</td></tr>
       <tr><td><strong>Multi-user</strong></td>
         <td>N/A</td>
         <td>Single-user (under investigation)</td>
         <td>N/A</td></tr>
       <tr><td><strong>Driver Station</strong></td>
         <td>FRC DS (Windows)</td>
         <td>FRC DS (Windows)</td>
         <td>Driver Hub / phone</td></tr>
     </tbody>
   </table>

   <!-- ── DASHBOARDS ── -->
   <p class="sw-section-h">Dashboards</p>

   <table class="sw-tbl">
     <thead>
       <tr>
         <th>Dashboard</th><th>Status</th><th>Best for</th>
       </tr>
     </thead>
     <tbody>
       <tr><td><strong>Elastic</strong></td>
         <td>&#10003; Current &mdash; recommended</td>
         <td>Competition driver dashboard. Highly configurable.</td></tr>
       <tr><td><strong>AdvantageScope</strong></td>
         <td>&#10003; Current &mdash; recommended</td>
         <td>Log review, 3D field visualization, mechanism replay.</td></tr>
       <tr><td><strong>Glass</strong></td>
         <td>&#10003; Current</td>
         <td>Built-in simulation UI and lightweight telemetry.</td></tr>
       <tr><td><strong>SmartDashboard</strong></td>
         <td><span class="sw-dep">Removed 2027</span></td>
         <td>Use Elastic instead.</td></tr>
       <tr><td><strong>Shuffleboard</strong></td>
         <td><span class="sw-dep">Removed 2027</span></td>
         <td>Use Elastic instead.</td></tr>
     </tbody>
   </table>

   <!-- ── VENDOR LIBRARIES ── -->
   <p class="sw-section-h">Vendor Libraries</p>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card">
       <div class="sw-card-title">What are vendor libraries?</div>
       <div class="sw-card-desc">
         Hardware vendors (REV, CTRE, etc.) ship WPILib extension
         libraries that add support for their specific motor controllers,
         sensors, and accessories. They are installed
         <strong>per project</strong> via the VS Code Dependency Manager
         and do not carry over on project import.
       </div>
     </div>
     <div class="sw-card">
       <div class="sw-card-title">Common libraries</div>
       <ul style="font-size:0.875rem;line-height:1.8;
          margin:8px 0 0;padding-left:20px;">
         <li><strong>REVLib</strong> &mdash; SPARK MAX, SPARK Flex</li>
         <li><strong>Phoenix 6</strong> &mdash; Talon FX, CANcoder</li>
         <li><strong>PathplannerLib</strong> &mdash; auto trajectories</li>
         <li><strong>PhotonLib</strong> &mdash; PhotonVision cameras</li>
         <li><strong>Limelight</strong> &mdash; Limelight cameras</li>
       </ul>
     </div>
   </div>

   <!-- ── PATH PLANNING ── -->
   <p class="sw-section-h">Path Planning</p>

   <div class="sw-grid sw-grid-2">
     <a class="sw-card sw-card-frc"
        href="../software/pathplanning/index.html">
       <div class="sw-label sw-label-frc">FRC</div>
       <div class="sw-card-title">PathPlanner / Choreo</div>
       <div class="sw-card-desc">
         GUI tools for drawing autonomous paths. Both generate
         trajectory commands that slot into command-based robot programs.
         PathPlanner is more beginner-friendly; Choreo optimizes
         for time.
       </div>
     </a>
     <div class="sw-card sw-card-ftc">
       <div class="sw-label sw-label-ftc">FTC REV Duo</div>
       <div class="sw-card-title">Road Runner</div>
       <div class="sw-card-desc">
         The standard FTC path planning library for REV Duo teams.
         Separate from WPILib. FTC Systemcore teams will use
         PathPlanner/Choreo (planned for 2028).
       </div>
     </div>
   </div>

   <!-- ── SHARED CONCEPTS ── -->
   <p class="sw-section-h">Shared Concepts Across Programs</p>
   <p style="font-size:0.875rem;margin-bottom:14px;
      color:var(--color-foreground-secondary,#555);">
     These programming concepts are identical whether you are writing FRC,
     FTC Systemcore, or XRP code.
   </p>

   <div class="sw-grid sw-grid-6">
     <div class="sw-card sw-card-shared">
       <div class="sw-card-title">PID Control</div>
       <div class="sw-card-desc">
         Proportional-Integral-Derivative feedback loop for precise
         motor velocity and position control.
       </div>
     </div>
     <div class="sw-card sw-card-shared">
       <div class="sw-card-title">Odometry</div>
       <div class="sw-card-desc">
         Track robot position on the field using encoder and gyro data.
         Used for autonomous navigation.
       </div>
     </div>
     <div class="sw-card sw-card-shared">
       <div class="sw-card-title">State Machines</div>
       <div class="sw-card-desc">
         Command-based programming uses a state machine model:
         subsystems, commands, and triggers.
       </div>
     </div>
     <div class="sw-card sw-card-shared">
       <div class="sw-card-title">AprilTags</div>
       <div class="sw-card-desc">
         WPILib includes built-in AprilTag detection for field
         localization and target tracking.
       </div>
     </div>
     <div class="sw-card sw-card-shared">
       <div class="sw-card-title">Motor Control</div>
       <div class="sw-card-desc">
         DifferentialDrive, MecanumDrive, and swerve kinematics
         classes work identically across all platforms.
       </div>
     </div>
     <div class="sw-card sw-card-shared">
       <div class="sw-card-title">Java Fundamentals</div>
       <div class="sw-card-desc">
         WPILib Java code uses standard Java: classes, interfaces,
         lambdas. No framework-specific syntax to learn separately.
       </div>
     </div>
   </div>

   <!-- ── SOURCE + DOCS ── -->
   <p class="sw-section-h">Source Code and API Docs</p>

   <div class="sw-grid sw-grid-3">
     <a class="sw-card sw-card-frc"
        href="https://github.wpilib.org/allwpilib/docs/release/java/">
       <div class="sw-card-title">Java API Reference</div>
       <div class="sw-card-desc">
         Full Javadoc for WPILibJ classes and methods.
       </div>
     </a>
     <a class="sw-card sw-card-frc"
        href="https://github.wpilib.org/allwpilib/docs/release/cpp/">
       <div class="sw-card-title">C++ API Reference</div>
       <div class="sw-card-desc">
         Doxygen documentation for WPILibC.
       </div>
     </a>
     <a class="sw-card sw-card-frc"
        href="https://robotpy.readthedocs.io/projects/robotpy/en/stable/">
       <div class="sw-card-title">Python API Reference</div>
       <div class="sw-card-desc">
         RobotPy documentation for Python-based robot programs.
       </div>
     </a>
   </div>
