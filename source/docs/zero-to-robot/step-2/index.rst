# Step 2: Install Your Tools

.. raw:: html

   <style>
   :root { --frc:#2e7d32; --frc-light:#f1f8f1; --shared:#2e7d32; --shared-light:#f1f8f1; }
   .sw-label { display:inline-block; font-size:0.7rem; font-weight:700; text-transform:uppercase;
     letter-spacing:0.06em; padding:2px 8px; border-radius:4px; margin-bottom:10px; }
   .sw-label-shared { background:var(--shared); color:#fff; }
   .sw-label-win { background:#0078d4; color:#fff; }
   .sw-label-any { background:#555; color:#fff; }
   .sw-section-h { font-size:0.85rem; font-weight:700; text-transform:uppercase;
     letter-spacing:0.06em; color:var(--color-foreground-secondary,#555);
     border-bottom:1px solid var(--color-background-border,#ddd);
     padding-bottom:7px; margin:28px 0 14px; }
   .sw-grid { display:grid; gap:12px; margin-bottom:24px; }
   .sw-grid-2 { grid-template-columns:repeat(2,1fr); }
   .sw-grid-3 { grid-template-columns:repeat(3,1fr); }
   .sw-card { padding:18px 20px; border-radius:8px;
     border:2px solid var(--color-background-border,#ddd);
     background:var(--color-background-primary,#fff);
     text-decoration:none; color:inherit; display:block;
     transition:border-color 0.2s, box-shadow 0.2s; }
   a.sw-card:hover { box-shadow:0 2px 8px rgba(0,0,0,0.08);
     text-decoration:none; color:inherit; }
   a.sw-card:visited { color:inherit; text-decoration:none; }
   .sw-card-shared { border-color:rgba(46,125,50,0.3); background:var(--shared-light); }
   a.sw-card-shared:hover { border-color:var(--shared);
     box-shadow:0 2px 10px rgba(46,125,50,0.15); }
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
   .sw-part-num { display:inline-block; font-size:0.7rem; font-weight:700;
     text-transform:uppercase; letter-spacing:0.04em;
     padding:2px 9px; border-radius:4px; margin-bottom:8px;
     background:var(--frc); color:#fff; }
   .sw-tip { background:var(--shared-light);
     border:1px solid rgba(46,125,50,0.3); border-radius:6px;
     padding:14px 18px; font-size:0.875rem; line-height:1.6;
     margin-bottom:20px; }
   .sw-warn { background:#fff8e1; border:1px solid rgba(255,160,0,0.4);
     border-radius:6px; padding:14px 18px; font-size:0.875rem;
     line-height:1.6; margin-bottom:20px; }
   .sw-nav { display:flex; justify-content:space-between;
     margin-top:32px; padding-top:16px;
     border-top:1px solid var(--color-background-border,#ddd); }
   .sw-nav-btn { padding:9px 20px; border-radius:6px; font-size:0.875rem;
     font-weight:600; text-decoration:none; border:2px solid var(--frc);
     color:var(--frc); background:var(--color-background-primary,#fff);
     transition:all 0.2s; }
   .sw-nav-btn:hover { background:var(--frc); color:#fff;
     text-decoration:none; }
   .sw-nav-btn:visited { color:var(--frc); }
   .sw-nav-btn.sw-next { background:var(--frc); color:#fff; }
   .sw-nav-btn.sw-next:hover { background:#1b5e20; border-color:#1b5e20; }
   .sw-nav-btn.sw-next:visited { color:#fff; }
   ul.sw-list { font-size:0.875rem; line-height:1.8; margin:8px 0 0;
     padding-left:20px; }
   @media(max-width:700px) {
     .sw-grid-2,.sw-grid-3 { grid-template-columns:1fr; } }
   </style>

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
