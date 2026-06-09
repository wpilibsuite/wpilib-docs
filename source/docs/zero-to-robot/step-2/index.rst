# Step 2: Install Your Tools

.. raw:: html


   <!-- Step badge -->
   <div class="sw-step-badge">
     <span class="sw-step-n">02</span>
     <div>
       <div class="sw-step-info-title">Install Your Tools</div>
       <div class="sw-step-info-sub">
         Step 2 of 4
       </div>
     </div>
   </div>

   <!-- System requirements -->
   <p class="sw-section-h">System Requirements</p>

   <div class="sw-grid sw-grid-2">

     <div class="sw-card">
       <div class="sw-label sw-label-win">Windows</div>
       <div class="sw-card-title">Required for Driver Station</div>
       <ul class="sw-list">
         <li>Windows 11 (required for 2027+)</li>
         <li>8 GB RAM minimum, 16 GB recommended</li>
         <li>Driver Station and roboRIO Imaging Tool</li>
         <li>All WPILib tools available</li>
       </ul>
     </div>

     <div class="sw-card">
       <div class="sw-label sw-label-any">macOS / Linux</div>
       <div class="sw-card-title">Coding and Simulation Only</div>
       <ul class="sw-list">
         <li>macOS 12+ or modern Linux distro</li>
         <li>WPILib + VS Code for writing and simulating code</li>
         <li>Cannot run Driver Station or image roboRIO</li>
         <li>Deploy code over USB or Wi-Fi (needs network access)</li>
       </ul>
     </div>

   </div>

   <div class="sw-warn">
     <strong>Windows 10 is no longer supported as of 2027.</strong>
     Upgrade to Windows 11 before installing FRC Game Tools.
   </div>

   <!-- Installation parts -->
   <p class="sw-section-h">Installation Steps</p>

   <div class="sw-grid sw-grid-2">

     <a class="sw-card sw-card-shared" href="wpilib-setup.html">
       <div class="sw-part-num">Part 1</div>
       <div class="sw-card-title">WPILib Installer</div>
       <div class="sw-card-desc">
         Installs Visual Studio Code, WPILib extensions, and all
         desktop tools (Glass, Elastic, Shuffleboard, OutlineViewer).
         Required for Java, C++, and Python teams.
       </div>
     </a>

     <a class="sw-card sw-card-shared" href="frc-game-tools.html">
       <div class="sw-part-num">Part 2: Windows only</div>
       <div class="sw-card-title">FRC Game Tools</div>
       <div class="sw-card-desc">
         Installs the FRC Driver Station
         Required on the laptop that will drive the robot at competition.
       </div>
     </a>

     <a class="sw-card sw-card-shared" href="python-setup.html">
       <div class="sw-part-num">Part 3: Python teams only</div>
       <div class="sw-card-title">RobotPy Setup</div>
       <div class="sw-card-desc">
         Install RobotPy and the required Python packages.
         Java and C++ teams can skip this part.
       </div>
     </a>

     <a class="sw-card sw-card-shared" href="offline-installation-preparations.html">
       <div class="sw-part-num">Optional</div>
       <div class="sw-card-title">Offline Installation</div>
       <div class="sw-card-desc">
         Preparing to install without internet access?
         Download the offline installer packages in advance.
       </div>
     </a>

   </div>

   <!-- Verify -->
   <p class="sw-section-h">Verify Your Installation</p>
   <p style="font-size:0.875rem;margin-bottom:16px;
      color:var(--color-foreground-secondary,#555);">
     After completing all parts above, confirm the installation is working:
   </p>

   <div class="sw-grid sw-grid-3">

     <div class="sw-card">
       <div class="sw-card-title">Open VS Code</div>
       <div class="sw-card-desc">
         Launch the WPILib VS Code shortcut (not the system VS Code).
         You should see the WPILib icon (W) in the activity bar.
       </div>
     </div>

     <div class="sw-card">
       <div class="sw-card-title">Run WPILib Command</div>
       <div class="sw-card-desc">
         Press <strong>Ctrl+Shift+P</strong> (or Cmd+Shift+P on Mac)
         and type <em>WPILib</em>. You should see WPILib commands in
         the palette.
       </div>
     </div>

     <div class="sw-card">
       <div class="sw-card-title">Check Driver Station</div>
       <div class="sw-card-desc">
         Open the FRC Driver Station (Windows only). It should launch
         without errors. Robot Communication will show
         &ldquo;No Robot Communication&rdquo; - that is expected.
       </div>
     </div>

   </div>

   <div class="sw-tip">
     <strong>Vendor libraries are not installed here.</strong>
     Libraries like REVLib and Phoenix 6 are added per-project in Step 4
     using the WPILib Dependency Manager. You do not need them yet.
   </div>

   <!-- Nav -->
   <div class="sw-nav">
     <a class="sw-nav-btn" href="../step-1/index.html">
       &larr; Step 1: Build Your Robot</a>
     <a class="sw-nav-btn sw-next" href="../step-3/index.html">
       Step 3: Configure Your Control System &rarr;</a>
   </div>

.. toctree::
   :maxdepth: 1
   :hidden:

   offline-installation-preparations
   first-driver-station
   wpilib-setup
   python-setup
   step-2-next-steps
