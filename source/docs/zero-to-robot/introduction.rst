.. include:: <isonum.txt>

# Zero to Robot: Introduction

Welcome to WPILib — the standard programming library for *FIRST*\ |reg| Robotics Competition
(FRC\ |reg|) and FIRST Tech Challenge (FTC).
This guide walks you through everything you need to start driving a robot.

.. raw:: html

   <style>
   :root { --frc:#009CD7; --frc-light:#e6f6fc; --ftc:#e07000; --ftc-light:#fff3e0; --shared:#2e7d32; --shared-light:#f1f8f1; }

   .sw-label { display:inline-block; font-size:0.7rem; font-weight:700; text-transform:uppercase; letter-spacing:0.06em; padding:2px 8px; border-radius:4px; margin-bottom:10px; }
   .sw-label-frc    { background:var(--frc);    color:#fff; }
   .sw-label-ftc    { background:var(--ftc);    color:#fff; }
   .sw-label-rec    { background:#1a1a1a;        color:#fff; }
   .sw-label-shared { background:var(--shared);  color:#fff; }

   .sw-section-h {
     font-size:0.85rem; font-weight:700; text-transform:uppercase; letter-spacing:0.06em;
     color:var(--color-foreground-secondary,#555);
     border-bottom:1px solid var(--color-background-border,#ddd);
     padding-bottom:7px; margin:32px 0 14px;
   }

   /* ── GRID ── */
   .sw-grid   { display:grid; gap:12px; margin-bottom:24px; }
   .sw-grid-2 { grid-template-columns:repeat(2,1fr); }
   .sw-grid-3 { grid-template-columns:repeat(3,1fr); }
   .sw-grid-4 { grid-template-columns:repeat(4,1fr); }

   /* ── CARDS ── */
   .sw-card {
     padding:18px 20px; border-radius:8px;
     border:2px solid var(--color-background-border,#ddd);
     background:var(--color-background-primary,#fff);
     text-decoration:none; color:inherit; display:block;
     transition:border-color 0.2s, box-shadow 0.2s;
   }
   a.sw-card:hover         { box-shadow:0 2px 8px rgba(0,0,0,0.08); text-decoration:none; color:inherit; }
   a.sw-card:visited       { color:inherit; text-decoration:none; }
   .sw-card-frc            { border-color:rgba(0,156,215,0.3); }
   a.sw-card-frc:hover     { border-color:var(--frc); box-shadow:0 2px 10px rgba(0,156,215,0.15); }
   .sw-card-ftc            { border-color:rgba(224,112,0,0.3); background:var(--ftc-light); }
   a.sw-card-ftc:hover     { border-color:var(--ftc); box-shadow:0 2px 10px rgba(224,112,0,0.15); }
   .sw-card-rec            { border-color:var(--frc); background:var(--frc-light); }
   .sw-card-shared         { border-color:rgba(46,125,50,0.3); background:var(--shared-light); }
   a.sw-card-shared:hover  { border-color:var(--shared); }

   .sw-card-title { font-weight:700; font-size:0.97rem; margin-bottom:4px; }
   .sw-card-desc  { font-size:0.85rem; color:var(--color-foreground-secondary,#555); line-height:1.55; }
   .sw-card-time  { font-size:0.78rem; color:var(--frc); font-weight:600; margin-bottom:6px; }
   .sw-step-num   { font-size:2rem; font-weight:800; color:var(--frc); font-family:monospace; line-height:1; margin-bottom:10px; display:block; }

   /* ── TIP / WARN ── */
   .sw-tip  { background:var(--shared-light); border:1px solid rgba(46,125,50,0.3); border-radius:6px; padding:14px 18px; font-size:0.875rem; line-height:1.6; margin-bottom:24px; }
   .sw-warn { background:#fff8e1; border:1px solid rgba(255,160,0,0.4); border-radius:6px; padding:14px 18px; font-size:0.875rem; line-height:1.6; margin-bottom:24px; }
   .sw-tip a, .sw-warn a { font-weight:600; }

   ul.sw-list { font-size:0.875rem; line-height:1.8; margin:8px 0 0; padding-left:20px; }

   @media(max-width:700px) { .sw-grid-2,.sw-grid-3,.sw-grid-4 { grid-template-columns:1fr; } }
   </style>

   <!-- ── LANGUAGE CHOICE ── -->
   <p class="sw-section-h">Choose Your Programming Language</p>
   <p style="font-size:0.9rem;margin-bottom:14px;color:var(--color-foreground-secondary,#444);">
     WPILib supports multiple languages. Pick one: your tools and steps are the same regardless of choice.
   </p>

   <div class="sw-grid sw-grid-5">

     <div class="sw-card sw-card-rec">
       <div class="sw-label sw-label-rec">Recommended &mdash; FRC + FTC</div>
       <div class="sw-card-title">Java</div>
       <div class="sw-card-desc">Statically typed, and has the most community examples. Best choice if you are unsure.</div>
     </div>

     <div class="sw-card sw-card-shared">
       <div class="sw-label sw-label-shared">FRC + FTC</div>
       <div class="sw-card-title">C++</div>
       <div class="sw-card-desc">Highest performance. Good choice if your team already knows C++. Memory management adds complexity for beginners.</div>
     </div>

     <div class="sw-card sw-card-shared">
       <div class="sw-label sw-label-shared">FRC + FTC</div>
       <div class="sw-card-title">Python</div>
       <div class="sw-card-desc">Easiest syntax. Growing community examples. Best if your team already programs in Python and wants a gentle start.</div>
     </div>

     <div class="sw-card sw-card-shared">
       <div class="sw-label sw-label-shared">FRC + FTC</div>
       <div class="sw-card-title">Blockly</div>
       <div class="sw-card-desc">Graphical interface, runs OnBot, outputs Python. Great for beginners with no prior syntax knowledge.</div>
     </div>

     <div class="sw-card sw-card-shared">
       <div class="sw-label sw-label-shared">FRC + FTC</div>
       <div class="sw-card-title">LabVIEW</div>
       <div class="sw-card-desc">Graphical dataflow programming, runs OnBot. Familiar to teams with a LabVIEW background.</div>
     </div>

   </div>

   <div class="sw-tip">
     <strong>New to programming entirely?</strong> Check out
     <a href="https://www.codecademy.com/learn/learn-java">Codecademy Java</a> or
     <a href="http://docs.python-guide.org/en/latest/intro/learning/">Python learning guides</a>
     before continuing. You can wire and configure your robot first (Steps 1 and 3) while learning to code in parallel.
   </div>

   <!-- ── WHAT YOU NEED ── -->
   <p class="sw-section-h">What You Need</p>

   <div class="sw-grid sw-grid-2" style="margin-bottom:12px;">

     <div class="sw-card sw-card-frc">
       <div class="sw-label sw-label-frc">FRC Hardware</div>
       <div class="sw-card-title">FRC Robot Components</div>
       <ul class="sw-list">
         <li>Systemcore controller</li>
         <li>Power Distribution Hub (PDH) or Panel (PDP)</li>
         <li>Vivid VH-109 Radio</li>
         <li>Voltage Regulator Module (VRM) &mdash; for radio power</li>
         <li>Motor controllers (SPARK MAX, Talon FX, etc.)</li>
         <li>Drive motors and wheels</li>
         <li>12 V robot battery and fuse</li>
         <li>Ethernet cable and USB-A cable</li>
       </ul>
     </div>

     <div class="sw-card sw-card-ftc">
       <div class="sw-label sw-label-ftc">FTC Hardware</div>
       <div class="sw-card-title">FTC Robot Components</div>
       <ul class="sw-list">
         <li>Systemcore + Motioncore controllers</li>
         <li>FTC legal motor controllers</li>
         <li>Drive motors and wheels</li>
         <li>12 V robot battery</li>
         <li>USB-C cable for programming</li>
         <li>Wi-Fi for wireless deploy</li>
       </ul>
     </div>

   </div>

   <div class="sw-grid sw-grid-2">

     <div class="sw-card">
       <div class="sw-label sw-label-shared">Software &mdash; All Teams</div>
       <div class="sw-card-title">What Gets Installed</div>
       <ul class="sw-list">
         <li><strong>WPILib</strong> &mdash; robot programming library + VS Code</li>
         <li><strong>FRC Game Tools</strong> &mdash; Driver Station <em>(Windows only)</em></li>
         <li><strong>RobotPy</strong> &mdash; Python framework <em>(Python teams only)</em></li>
         <li>Vendor libraries (REVLib, Phoenix 6, etc.) &mdash; installed per project</li>
       </ul>
       <div style="margin-top:12px;font-size:0.82rem;
          color:var(--color-foreground-secondary,#555);">
         <strong>OS note:</strong> Driver Station requires Windows.
         Coding and simulation work on macOS and Linux.
       </div>
     </div>

     <div class="sw-card sw-card-shared">
       <div class="sw-label sw-label-shared">No Full Robot? No Problem.</div>
       <div class="sw-card-title">Practice with the XRP</div>
       <div class="sw-card-desc" style="margin-bottom:10px;">
         The XRP is a desktop robot that runs real WPILib code.
         Great for learning before build season &mdash; and for FTC teams
         getting a head start on Systemcore programming.
       </div>
       <a href="../xrp-robot/index.html"
          style="font-size:0.85rem;font-weight:600;color:var(--shared);">
         XRP docs &rarr;
       </a>
     </div>

   </div>

   <!-- ── FOUR STEPS ── -->
   <p class="sw-section-h">The Four Steps</p>
   <p style="font-size:0.9rem;margin-bottom:16px;color:var(--color-foreground-secondary,#444);">
     Complete these in order. You will have a driving robot by the end of Step 4.
   </p>

   <div class="sw-grid sw-grid-4">

     <a class="sw-card sw-card-frc" href="step-1/index.html">
       <span class="sw-step-num">01</span>
       <div class="sw-card-title">Build Your Robot</div>
       <div class="sw-card-desc">Wire the control system: power distribution, roboRIO, motor controllers, and radio.</div>
     </a>

     <a class="sw-card sw-card-frc" href="step-2/index.html">
       <span class="sw-step-num">02</span>
       <div class="sw-card-title">Install Your Tools</div>
       <div class="sw-card-desc">Install WPILib and Driver Station on your laptop.</div>
     </a>

     <a class="sw-card sw-card-frc" href="step-3/index.html">
       <span class="sw-step-num">03</span>
       <div class="sw-card-title">Configure Your Control System</div>
       <div class="sw-card-desc">Configuire your systemcore and the radio. Required every season before you can deploy code.</div>
     </a>

     <a class="sw-card sw-card-frc" href="step-4/index.html">
       <span class="sw-step-num">04</span>
       <div class="sw-card-title">Write and Drive</div>
       <div class="sw-card-desc">Create your first robot project, deploy code to the robot, and enable it with the Driver Station.</div>
     </a>

   </div>

   <!-- ── TIPS ── -->
   <p class="sw-section-h">Tips for New Teams</p>

   <div class="sw-grid sw-grid-2">

     <div class="sw-tip" style="margin-bottom:0;">
       <strong>A tip</strong><br>
       An example tip
     </div>

     <div class="sw-tip" style="margin-bottom:0;">
       <strong>Another tip</strong><br>
       This is another tip
     </div>


   </div>
