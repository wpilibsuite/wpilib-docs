.. include:: <isonum.txt>

.. meta::
   :google-site-verification: POR_nG8b56eXGxmUIutST7jcA_Vl58ypSdJTzJ1g0zg

WPILib Documentation
====================

.. raw:: html

   <div style="text-align:center;padding:36px 0 32px;">
     <h1 style="font-size:2rem;font-weight:800;margin:0 0 12px;
        color:var(--color-foreground-primary,#1a1a1a);">
       Welcome!
     </h1>
     <p style="font-size:1rem;color:var(--color-foreground-secondary,#555);
        max-width:560px;margin:0 auto 20px;line-height:1.6;">
       WPILib is the standard programming library for <em>FIRST</em> Robotics,
       supporting teams in
       <strong style="color:#009CD7;">FRC</strong>
       and
       <strong style="color:#e07000;">FTC</strong>.
     </p>
     <div style="display:flex;justify-content:center;gap:10px;flex-wrap:wrap;">
       <span style="background:#009CD7;color:#fff;font-size:0.8rem;font-weight:700;
          text-transform:uppercase;letter-spacing:0.06em;
          padding:5px 16px;border-radius:20px;">
         FRC &mdash; FIRST Robotics Competition
       </span>
       <span style="background:#e07000;color:#fff;font-size:0.8rem;font-weight:700;
          text-transform:uppercase;letter-spacing:0.06em;
          padding:5px 16px;border-radius:20px;">
         FTC &mdash; FIRST Tech Challenge
       </span>
     </div>
   </div>

   <div id="landing-tab-root">

     <!-- ── TAB SELECTOR ──────────────────────────── -->
     <div class="wl-tab-selector">
       <p class="wl-tab-prompt">Where are you starting from?</p>
       <div class="wl-tab-buttons">
         <button class="wl-tab-btn" id="btn-new" onclick="wlSelectTab('new')">New to FIRST Programming</button>
         <button class="wl-tab-btn" id="btn-returning" onclick="wlSelectTab('returning')">Returning Team</button>
       </div>
     </div>

     <!-- ── NEW USER PANEL ────────────────────────── -->
     <div class="wl-panel" id="panel-new">

       <!-- Screen 1: Experience level -->
       <div id="new-s1">
         <div class="wl-welcome">
           <h2 class="wl-welcome-h">Let us help you find the right starting point.</h2>
           <p class="wl-welcome-p">WPILib is the standard programming library for FIRST robotics &mdash; supporting both FRC and FTC teams. Built through a partnership between WPI, FIRST, and volunteer developers, it has everything you need to write, test, and deploy robot code.</p>
         </div>
         <h3 class="wl-sh">How familiar are you with programming?</h3>
         <div class="wl-grid">
           <button class="wl-card wl-card-shared wl-btn" onclick="wlShow('new-s2')">
             <span class="wl-num wl-shared-text">0</span>
             <div>
               <div class="wl-card-title">Brand new to programming</div>
               <div class="wl-card-desc">Never written code before, or just starting out. We will point you to beginner resources and walk you through every step.</div>
             </div>
           </button>
           <button class="wl-card wl-card-shared wl-btn" onclick="wlShow('new-s2')">
             <span class="wl-num wl-shared-text">1</span>
             <div>
               <div class="wl-card-title">I know some programming basics</div>
               <div class="wl-card-desc">You have written code before and are ready to jump into robot programming. Let us get your tools installed and your robot moving.</div>
             </div>
           </button>
         </div>
       </div>

       <!-- Screen 1 continued: 4 steps preview -->
       <div id="new-s1-steps">
         <h3 class="wl-sh">Here is What the Steps Look Like</h3>
         <div class="wl-grid">
           <div class="wl-card wl-card-frc">
             <span class="wl-num wl-frc-text">01</span>
             <div>
               <div class="wl-card-title">Install and Choose Your Tools</div>
               <div class="wl-card-desc">WPILib, VS Code, Choose Java, C++, or Python.</div>
             </div>
           </div>
           <div class="wl-card wl-card-frc">
             <span class="wl-num wl-frc-text">02</span>
             <div>
               <div class="wl-card-title">Set Up Your Hardware</div>
               <div class="wl-card-desc">Wire the control system, image the roboRIO, and configure the radio.</div>
             </div>
           </div>
           <div class="wl-card wl-card-frc">
             <span class="wl-num wl-frc-text">03</span>
             <div>
               <div class="wl-card-title">Write and Deploy Code</div>
               <div class="wl-card-desc">Create your first project, write drive code, and deploy it to the robot.</div>
             </div>
           </div>
           <div class="wl-card wl-card-frc">
             <span class="wl-num wl-frc-text">04</span>
             <div>
               <div class="wl-card-title">Drive and Test</div>
               <div class="wl-card-desc">Connect the Driver Station, plug in a joystick, and enable the robot for the first time.</div>
             </div>
           </div>
         </div>
         <div class="wl-tip wl-tip-shared" style="margin-bottom:8px;">
           <strong>Want to just focus on code?</strong>
           The <a href="docs/xrp-robot/index.html">XRP Robot Platform</a> lets you write and test real WPILib code on a low-cost robot. The robot runs off of a Rasberry Pi, so no control system required.
         </div>
       </div>

       <!-- Screen 2: Which program -->
       <div id="new-s2" style="display:none;">
         <div class="wl-welcome">
           <h2 class="wl-welcome-h">Which FIRST program are you in?</h2>
           <p class="wl-welcome-p">WPILib supports multiple FIRST programs. Your setup steps differ slightly depending on which one you are in.</p>
         </div>
         <h3 class="wl-sh">Choose your program</h3>
         <div class="wl-grid">
           <button class="wl-card wl-card-frc wl-btn" onclick="wlShow('new-s3-frc')">
             <span class="wl-num wl-frc-text">FRC</span>
             <div>
               <div class="wl-card-title">FIRST Robotics Competition</div>
               <div class="wl-card-desc">Industrial sized robots, Built to play a court sized game. High school program. Now uses Systemcore (as of 2027) and supports Java, C++, or Python.</div>
             </div>
           </button>
           <button class="wl-card wl-card-ftc wl-btn" onclick="wlShow('new-s3-ftc')">
             <span class="wl-num wl-ftc-text">FTC</span>
             <div>
               <div class="wl-card-title">FIRST Tech Challenge</div>
               <div class="wl-card-desc">Smaller robots. WPILib support is now available via the Systemcore controller. REV Duo teams can still program with the FTC SDK.</div>
             </div>
           </button>
         </div>
         <button class="wl-back" onclick="wlBack('new-s1','new-s2')">Back</button>
       </div>

       <!-- Screen 3a: FRC steps -->
       <div id="new-s3-frc" style="display:none;">
         <div class="wl-welcome wl-welcome-frc">
           <h2 class="wl-welcome-h">FRC : Four steps to a running robot.</h2>
           <p class="wl-welcome-p">Follow these in order. You will have a driveable robot by the end of Step 4.</p>
         </div>
         <h3 class="wl-sh">Start Here</h3>
         <div class="wl-grid">
           <a class="wl-card wl-card-frc" href="docs/zero-to-robot/step-1/index.html">
             <span class="wl-num wl-frc-text">01</span>
             <div>
               <div class="wl-card-title">Install Your Tools</div>
               <div class="wl-card-desc">WPILib, VS Code, and FRC Game Tools. Choose Java, C++, or Python.</div>
             </div>
           </a>
           <a class="wl-card wl-card-frc" href="docs/zero-to-robot/step-2/index.html">
             <span class="wl-num wl-frc-text">02</span>
             <div>
               <div class="wl-card-title">Set Up Your Hardware</div>
               <div class="wl-card-desc">Wire the control system and configure your devices.</div>
             </div>
           </a>
           <a class="wl-card wl-card-frc" href="docs/zero-to-robot/step-3/index.html">
             <span class="wl-num wl-frc-text">03</span>
             <div>
               <div class="wl-card-title">Write and Deploy Code</div>
               <div class="wl-card-desc">Create your first project, write drive code, and deploy it to the robot.</div>
             </div>
           </a>
           <a class="wl-card wl-card-frc" href="docs/zero-to-robot/step-4/index.html">
             <span class="wl-num wl-frc-text">04</span>
             <div>
               <div class="wl-card-title">Drive</div>
               <div class="wl-card-desc">Connect the Driver Station, plug in a joystick, and enable the robot for the first time.</div>
             </div>
           </a>
         </div>
         <h3 class="wl-sh">Helpful Background Reading</h3>
         <div class="wl-quicklinks">
           <a class="wl-ql wl-ql-frc" href="docs/zero-to-robot/introduction.html">Zero-to-Robot Introduction</a>
           <a class="wl-ql wl-ql-frc" href="docs/hardware/hardware-basics/hardware-overview.html">Hardware Overview</a>
           <a class="wl-ql wl-ql-frc" href="docs/software/what-is-wpilib.html">What is WPILib?</a>
           <a class="wl-ql wl-ql-shared" href="docs/xrp-robot/index.html">Practice with the XRP</a>
         </div>
         <div class="wl-tip wl-tip-shared">
           <strong>Not ready for a full robot?</strong>
           The <a href="docs/xrp-robot/index.html">XRP Robot Platform</a> lets you write and test real WPILib code on a low-cost desktop robot : no roboRIO or wiring required.
         </div>
         <button class="wl-back" onclick="wlBack('new-s2','new-s3-frc')">Back to program select</button>
       </div>

       <!-- Screen 3b: FTC paths -->
       <div id="new-s3-ftc" style="display:none;">
         <div class="wl-welcome wl-welcome-ftc">
           <h2 class="wl-welcome-h">FTC : Two paths depending on your hardware.</h2>
           <p class="wl-welcome-p">WPILib is expanding to FIRST Tech Challenge, but your options today depend on which control system your team uses.</p>
         </div>
         <h3 class="wl-sh">Choose your path</h3>
         <div class="wl-grid">
           <div class="wl-card wl-card-shared">
             <span class="wl-num wl-shared-text" style="font-size:0.85rem;">NOW</span>
             <div>
               <div class="wl-card-title">REV Control Hub / Expansion Hub (REV Duo)</div>
               <div class="wl-card-desc">The current standard FTC control system. Program today using the FTC SDK with Java or Blocks. Fully supported for the current season.</div>
               <a href="https://ftc-docs.firstinspires.org" class="wl-card-link wl-shared-text" style="margin-top:10px;display:inline-block;">FTC SDK Docs (ftc-docs.firstinspires.org)</a>
             </div>
           </div>
           <div class="wl-card wl-card-ftc">
             <span class="wl-num wl-ftc-text" style="font-size:0.85rem;">NOW</span>
             <div>
               <div class="wl-card-title">Systemcore + Motioncore (WPILib)</div>
               <div class="wl-card-desc">The new controllers bring full WPILib support to FTC: Now available for the 2027-2028 season.</div>
               <a href="docs/ftc/index.html" class="wl-card-link wl-ftc-text" style="margin-top:10px;display:inline-block;">WPILib FTC Overview</a>
             </div>
           </div>
         </div>
         <div class="wl-tip wl-tip-shared">
           <strong>Getting a head start on WPILib?</strong>
           The <a href="docs/xrp-robot/index.html">XRP Robot Platform</a> lets you learn WPILib programming on real hardware today : the same skills carry straight over now that Systemcore is available.
         </div>
         <button class="wl-back" onclick="wlBack('new-s2','new-s3-ftc')">Back to program select</button>
       </div>

     </div>

     <!-- ── RETURNING PANEL ────────────────────────── -->
     <div class="wl-panel" id="panel-returning">

       <div class="wl-welcome">
         <h2 class="wl-welcome-h">Welcome back. Here is what has changed for 2027.</h2>
         <p class="wl-welcome-p">Run through the checklist below before your first practice session. Several tools were removed in 2027 : check the deprecations section if you have not yet migrated.</p>
       </div>

       <div class="wl-ret-grid">

         <div class="wl-ret-card wl-ret-frc">
           <div class="wl-ret-label wl-frc-label">FRC</div>
           <h3 class="wl-ret-h">Pre-Season Checklist</h3>
           <ul>
             <li>Download and run the <strong>2027 WPILib installer</strong></li>
             <li>Flash your Systemcore using <strong>FRC 2027 Game Tools</strong></li>
             <li>Use <strong>Import Project</strong> in VS Code to migrate your 2026 code</li>
             <li>Re-add all vendor libraries : they do not carry over on import</li>
             <li>Check for vendor library updates in the Dependency Manager</li>
             <li>Test with the simulator before deploying to hardware</li>
           </ul>
         </div>

         <div class="wl-ret-card wl-ret-frc">
           <div class="wl-ret-label wl-frc-label">FRC</div>
           <h3 class="wl-ret-h">Removed in 2027 : No Longer Available</h3>
           <p style="font-size:0.875rem;margin-bottom:8px;">These tools were <strong>removed in the 2027 season</strong>. If you have not yet migrated, you need to do so now.</p>
           <ul>
             <li><strong>Shuffleboard</strong> : migrate to <a href="https://github.com/Gold872/elastic-dashboard">Elastic</a> or AdvantageScope</li>
             <li><strong>SmartDashboard</strong> : migrate to Glass or Elastic (uses deprecated NT v3)</li>
             <li><strong>PathWeaver</strong> : migrate to <a href="https://github.com/mjansen4857/pathplanner">PathPlanner</a> or <a href="https://sleipnirgroup.github.io/Choreo/">Choreo</a></li>
             <li><strong>RobotBuilder</strong> : will be removed with control system change in 2027</li>
           </ul>
         </div>

         <div class="wl-ret-card wl-ret-frc">
           <div class="wl-ret-label wl-frc-label">FRC</div>
           <h3 class="wl-ret-h">What is New for 2027</h3>
           <ul>
             <li>FRC now uses Systemcore: see the hardware migration guide</li>
             <li>2027 field images and AprilTag layout data included in WPILib</li>
             <li>Windows 10 is no longer supported: Windows 11 is required</li>
             <li>Vendor library updates required: check the Dependency Manager</li>
           </ul>
           <a href="docs/yearly-overview/index.html" class="wl-frc-text" style="font-size:0.875rem;">Full 2027 changelog</a>
         </div>

         <div class="wl-ret-card wl-ret-shared">
           <div class="wl-ret-label wl-shared-label">FRC + FTC</div>
           <h3 class="wl-ret-h">Looking Ahead to 2028</h3>
           <ul>
             <li>Continued improvements to <strong>Systemcore</strong> and <strong>Motioncore</strong> toolchains</li>
             <li>Expanded <strong>FTC</strong> WPILib documentation and library support</li>
             <li>Watch the WPILib blog for 2028 season previews</li>
           </ul>
           <a href="https://wpilib.org/blog" class="wl-shared-text" style="font-size:0.875rem;">Follow the WPILib blog for previews</a>
         </div>

         <div class="wl-ret-card wl-ret-ftc" style="grid-column:1/-1;">
           <div class="wl-ret-label wl-ftc-label">FTC</div>
           <h3 class="wl-ret-h">FTC Teams : Your Options Right Now</h3>
           <p style="font-size:0.875rem;margin-bottom:12px;">WPILib FTC support is now available with Systemcore. Here is where things stand for the 2027-2028 season:</p>
           <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
             <div>
               <strong style="font-size:0.875rem;">Using REV Control Hub / Expansion Hub (REV Duo)?</strong>
               <ul style="font-size:0.82rem;margin-top:6px;">
                 <li>Continue programming with the <strong>FTC SDK</strong> as normal : Java or Blocks</li>
                 <li>Full documentation at <a href="https://ftc-docs.firstinspires.org">ftc-docs.firstinspires.org</a></li>
                 <li>REV Duo hardware remains legal and fully supported for the current season</li>
               </ul>
             </div>
             <div>
               <strong style="font-size:0.875rem;">Using Systemcore with WPILib?</strong>
               <ul style="font-size:0.82rem;margin-top:6px;">
                 <li>Systemcore and Motioncore bring full WPILib support to FTC</li>
                 <li>Same Java / C++ / Python toolchain as FRC : skills transfer directly</li>
                 <li>Try the <a href="docs/xrp-robot/index.html">XRP Platform</a> to start learning WPILib today</li>
                 <li><a href="docs/ftc/index.html">WPILib FTC overview</a></li>
               </ul>
             </div>
           </div>
         </div>

       </div>
     </div>

   </div>

   <style>
   /* ── COLOR TOKENS ── */
   :root {
     --frc:        #009CD7;   /* FIRST Process Blue */
     --frc-light:  #e6f6fc;
     --ftc:        #e07000;   /* FTC orange */
     --ftc-light:  #fff3e0;
     --shared:     #2e7d32;   /* shared green */
     --shared-light: #f1f8f1;
   }

   /* ── TAB SELECTOR ── */
   #landing-tab-root { max-width: 900px; }
   .wl-tab-selector { text-align:center; padding:36px 0 28px; }
   .wl-tab-prompt { font-size:1.1rem; font-weight:600; margin-bottom:16px; }
   .wl-tab-buttons { display:flex; justify-content:center; gap:12px; flex-wrap:wrap; }
   .wl-tab-btn {
     padding:11px 26px; font-size:0.95rem; font-weight:600;
     border-radius:6px; border:2px solid #ccc;
     background:var(--color-background-secondary,#f8f8f8);
     cursor:pointer; transition:all 0.2s;
     color:var(--color-foreground-primary,#1a1a1a);
   }
   .wl-tab-btn:hover { border-color:var(--frc); color:var(--frc); }
   .wl-tab-btn.active { background:var(--frc); border-color:var(--frc); color:#fff; }
   .wl-tab-btn:visited { color: inherit; }

   /* ── PANELS ── */
   .wl-panel { display:none; padding-bottom:40px; }
   .wl-panel.active { display:block; }

   /* ── WELCOME BLOCK ── */
   .wl-welcome {
     background:var(--color-background-secondary,#f8f8f8);
     border-left:4px solid var(--frc);
     border-radius:6px; padding:20px 24px; margin-bottom:28px;
   }
   .wl-welcome-frc { border-left-color:var(--frc); }
   .wl-welcome-ftc { border-left-color:var(--ftc); }
   .wl-welcome-h { font-size:1.35rem; font-weight:700; margin:0 0 8px; border:none; }
   .wl-welcome-p { font-size:0.95rem; margin:0; line-height:1.6; color:var(--color-foreground-secondary,#444); }

   /* ── SECTION HEADING ── */
   .wl-sh {
     font-size:0.9rem; font-weight:700; text-transform:uppercase;
     letter-spacing:0.06em; color:var(--color-foreground-secondary,#555);
     border-bottom:1px solid var(--color-background-border,#ddd);
     padding-bottom:7px; margin:24px 0 14px;
   }

   /* ── CARDS GRID ── */
   .wl-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:12px; margin-bottom:24px; }

   .wl-card {
     display:flex; align-items:flex-start; gap:14px;
     padding:18px 20px; border-radius:8px;
     border:2px solid var(--color-background-border,#ddd);
     text-decoration:none; color:inherit;
     background:var(--color-background-primary,#fff);
     transition:border-color 0.2s, box-shadow 0.2s;
   }
   .wl-btn { cursor:pointer; text-align:left; width:100%; }
   .wl-card:hover { box-shadow:0 2px 8px rgba(0,0,0,0.08); text-decoration:none; color:inherit; }
   .wl-card:visited,
   .wl-prog-card:visited,
   .wl-core-card:visited,
   .wl-xrp-blurb:visited,
   .wl-ql:visited { color: inherit; text-decoration: none; }




   .wl-card-frc  { border-color:rgba(0,48,135,0.25); }
   .wl-card-frc:hover  { border-color:var(--frc);  box-shadow:0 2px 10px rgba(0,48,135,0.12); }
   .wl-card-ftc  { border-color:rgba(224,112,0,0.3); background:var(--ftc-light); }
   .wl-card-ftc:hover  { border-color:var(--ftc);  box-shadow:0 2px 10px rgba(224,112,0,0.15); }
   .wl-card-shared { border-color:rgba(46,125,50,0.25); }
   .wl-card-shared:hover { border-color:var(--shared); box-shadow:0 2px 10px rgba(46,125,50,0.12); }

   .wl-num { font-size:1.4rem; font-weight:800; line-height:1; flex-shrink:0; font-family:monospace; }
   .wl-frc-text    { color:var(--frc); }
   .wl-ftc-text    { color:var(--ftc); }
   .wl-shared-text { color:var(--shared); }

   .wl-card-title { font-weight:700; font-size:0.95rem; margin-bottom:4px; }
   .wl-card-desc  { font-size:0.85rem; color:var(--color-foreground-secondary,#555); line-height:1.5; }
   .wl-card-link  { font-size:0.82rem; font-weight:600; text-decoration:none; }
   .wl-card-link:hover { text-decoration:underline; }

   /* ── QUICK LINKS ── */
   .wl-quicklinks { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:20px; }
   .wl-ql {
     padding:7px 14px; border-radius:20px; font-size:0.85rem; font-weight:500;
     text-decoration:none; border:1px solid; transition:all 0.2s;
     background:var(--color-background-primary,#fff);
   }
   .wl-ql-frc    { color:var(--frc);    border-color:rgba(0,48,135,0.3); }
   .wl-ql-frc:hover    { background:var(--frc);    color:#fff; border-color:var(--frc); text-decoration:none; }
   .wl-ql-shared { color:var(--shared); border-color:rgba(46,125,50,0.3); }
   .wl-ql-shared:hover { background:var(--shared); color:#fff; border-color:var(--shared); text-decoration:none; }

   /* ── TIP BLOCK ── */
   .wl-tip { border-radius:6px; padding:13px 17px; font-size:0.875rem; line-height:1.6; }
   .wl-tip-shared { background:var(--shared-light); border:1px solid rgba(46,125,50,0.3); }
   .wl-tip-shared a { color:var(--shared); }

   /* ── BACK BUTTON ── */
   .wl-back {
     background:none; border:none; cursor:pointer;
     font-size:0.85rem; margin-top:12px; padding:0;
     color:var(--color-foreground-secondary,#666);
     text-decoration:underline;
   }
   .wl-back:hover { color:var(--frc); }

   /* ── RETURNING GRID ── */
   .wl-ret-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:14px; }

   .wl-ret-card {
     border-radius:8px; padding:18px 20px;
     border:2px solid var(--color-background-border,#ddd);
     background:var(--color-background-primary,#fff);
     position:relative;
   }
   .wl-ret-card ul { font-size:0.875rem; line-height:1.7; margin:0; padding-left:18px; }
   .wl-ret-card li { margin-bottom:2px; }

   .wl-ret-frc   { border-color:var(--frc);    background:var(--frc-light); }
   .wl-ret-ftc   { border-color:var(--ftc);    background:var(--ftc-light); }
   .wl-ret-shared { border-color:var(--shared); background:var(--shared-light); }

   .wl-ret-label {
     display:inline-block; font-size:0.7rem; font-weight:700;
     text-transform:uppercase; letter-spacing:0.06em;
     padding:2px 8px; border-radius:4px; margin-bottom:8px;
   }
   .wl-frc-label    { background:var(--frc);    color:#fff; }
   .wl-ftc-label    { background:var(--ftc);    color:#fff; }
   .wl-shared-label { background:var(--shared); color:#fff; }

   .wl-ret-h { font-size:0.95rem; font-weight:700; margin:0 0 10px; border:none; }

   /* ── PROGRAM + CORE GRIDS (below tabs) ── */
   .wl-program-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:14px; margin-bottom:14px; }
   .wl-prog-card {
     display:block; border-radius:8px; padding:20px 22px;
     text-decoration:none; color:inherit;
     border:2px solid var(--color-background-border,#ddd);
     background:var(--color-background-primary,#fff);
     transition:border-color 0.2s, box-shadow 0.2s;
   }
   .wl-prog-card:hover { text-decoration:none; color:inherit; box-shadow:0 2px 8px rgba(0,0,0,0.08); }
   .wl-prog-frc { border-color:rgba(0,48,135,0.25); }
   .wl-prog-frc:hover { border-color:var(--frc); }
   .wl-prog-ftc { border-color:rgba(224,112,0,0.3); background:var(--ftc-light); }
   .wl-prog-ftc:hover { border-color:var(--ftc); }
   .wl-prog-tag {
     display:inline-block; font-size:0.72rem; font-weight:700;
     text-transform:uppercase; letter-spacing:0.05em;
     padding:2px 8px; border-radius:4px; margin-bottom:9px;
   }
   .wl-prog-title { font-size:1rem; font-weight:700; margin-bottom:5px; }
   .wl-prog-desc  { font-size:0.875rem; color:var(--color-foreground-secondary,#555); line-height:1.5; }

   .wl-core-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:11px; margin-bottom:32px; }
   .wl-core-card {
     display:block; border-radius:8px; padding:15px 17px;
     text-decoration:none; color:inherit;
     border:1px solid var(--color-background-border,#ddd);
     background:var(--color-background-primary,#fff);
     transition:border-color 0.2s;
   }
   .wl-core-card:hover { border-color:var(--frc); text-decoration:none; color:inherit; }
   .wl-core-title { font-size:0.88rem; font-weight:700; margin-bottom:4px; }
   .wl-core-desc  { font-size:0.78rem; color:var(--color-foreground-secondary,#555); line-height:1.5; }

   .wl-xrp-blurb {
     display:flex; align-items:center; gap:16px;
     padding:13px 18px; border-radius:8px; margin-bottom:14px;
     border:1px solid rgba(46,125,50,0.3); background:var(--shared-light);
     text-decoration:none; color:inherit; transition:border-color 0.2s;
   }
   .wl-xrp-blurb:hover { border-color:var(--shared); text-decoration:none; color:inherit; }
   .wl-xrp-tag {
     font-size:0.72rem; font-weight:700; text-transform:uppercase;
     letter-spacing:0.05em; padding:2px 8px; border-radius:4px;
     background:var(--shared); color:#fff; flex-shrink:0;
   }
   .wl-xrp-text { font-size:0.875rem; line-height:1.5; }
   .wl-xrp-link { margin-left:auto; font-size:0.85rem; font-weight:600; color:var(--shared); flex-shrink:0; }

   /* ── RESPONSIVE ── */
   @media (max-width:700px) {
     .wl-grid         { grid-template-columns:1fr; }
     .wl-ret-grid     { grid-template-columns:1fr; }
     .wl-program-grid { grid-template-columns:1fr; }
     .wl-core-grid    { grid-template-columns:repeat(2,1fr); }
   }
   @media (max-width:460px) {
     .wl-core-grid { grid-template-columns:1fr; }
   }
   </style>

   <script>
   function wlSelectTab(tab) {
     document.querySelectorAll('.wl-panel').forEach(p => p.classList.remove('active'));
     document.querySelectorAll('.wl-tab-btn').forEach(b => b.classList.remove('active'));
     document.getElementById('panel-' + tab).classList.add('active');
     document.getElementById('btn-' + tab).classList.add('active');
     try { localStorage.setItem('wpilib-tab', tab); } catch(e) {}
   }
   function wlShow(id) {
     ['new-s1','new-s1-steps','new-s2','new-s3-frc','new-s3-ftc'].forEach(function(s) {
       var el = document.getElementById(s);
       if (el) el.style.display = (s === id) ? 'block' : 'none';
     });
   }
   function wlBack(showId, hideId) {
     document.getElementById(hideId).style.display = 'none';
     document.getElementById(showId).style.display  = 'block';
     if (showId === 'new-s1') {
       document.getElementById('new-s1-steps').style.display = 'block';
     }
   }
   (function() {
     var saved; try { saved = localStorage.getItem('wpilib-tab'); } catch(e) {}
     wlSelectTab(saved || 'new');
   })();
   </script>

.. raw:: html

   <hr style="margin:32px 0 28px;"/>
   <h2 style="font-size:1rem;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:var(--color-foreground-secondary,#555);border-bottom:1px solid var(--color-background-border,#ddd);padding-bottom:7px;margin-bottom:16px;">Choose Your Program</h2>

   <div class="wl-program-grid">
     <a class="wl-prog-card wl-prog-frc" href="docs/zero-to-robot/introduction.html">
       <div class="wl-prog-tag wl-frc-label">FRC</div>
       <div class="wl-prog-title">FIRST Robotics Competition</div>
       <div class="wl-prog-desc">Industrial sized robots, Built to play a court sized game. High school program. Now uses Systemcore (as of 2027) and supports Java, C++, or Python.</div>
     </a>
     <a class="wl-prog-card wl-prog-ftc" href="docs/ftc/index.html">
       <div class="wl-prog-tag wl-ftc-label">FTC</div>
       <div class="wl-prog-title">FIRST Tech Challenge</div>
       <div class="wl-prog-desc">WPILib is expanding to FTC via the Systemcore and Motioncore controllers. REV Duo teams can program today using the FTC SDK.</div>
     </a>
   </div>

   <a class="wl-xrp-blurb" href="docs/xrp-robot/index.html">
     <span class="wl-xrp-tag">XRP</span>
     <span class="wl-xrp-text"><strong>Practicing before build season?</strong> The XRP Robot Platform lets you write and test real WPILib code on a low-cost desktop robot : no roboRIO required.</span>
     <span class="wl-xrp-link">XRP docs &rarr;</span>
   </a>

   <hr style="margin:28px 0;"/>
   <h2 style="font-size:1rem;font-weight:700;text-transform:uppercase;letter-spacing:0.06em;color:var(--color-foreground-secondary,#555);border-bottom:1px solid var(--color-background-border,#ddd);padding-bottom:7px;margin-bottom:6px;">Core Documentation</h2>
   <p style="font-size:0.85rem;color:var(--color-foreground-secondary,#555);margin-bottom:14px;">Shared across all supported programs.</p>

   <div class="wl-core-grid">
     <a class="wl-core-card" href="docs/hardware/hardware-basics/hardware-overview.html"><div class="wl-core-title">Hardware Overview</div><div class="wl-core-desc">Motors, sensors, pneumatics, cameras, and FRC-legal components.</div></a>
     <a class="wl-core-card" href="docs/software/what-is-wpilib.html"><div class="wl-core-title">Software Overview</div><div class="wl-core-desc">WPILib tools, VS Code extensions, vendor libraries, and the full software ecosystem.</div></a>
     <a class="wl-core-card" href="docs/software/commandbased/index.html"><div class="wl-core-title">Robot Programming</div><div class="wl-core-desc">Command-based framework, subsystems, triggers, and drive code patterns.</div></a>
     <a class="wl-core-card" href="docs/software/pathplanning/index.html"><div class="wl-core-title">Path Planning</div><div class="wl-core-desc">Autonomous trajectories with PathPlanner, Choreo, and WPILib built-in tools.</div></a>
     <a class="wl-core-card" href="docs/software/dashboards/index.html"><div class="wl-core-title">Dashboards</div><div class="wl-core-desc">Elastic, AdvantageScope, Glass, and NetworkTables for real-time telemetry.</div></a>
     <a class="wl-core-card" href="docs/software/advanced-controls/index.html"><div class="wl-core-title">Advanced Controls</div><div class="wl-core-desc">PID, feedforward, state-space, kinematics, and system identification.</div></a>
     <a class="wl-core-card" href="docs/software/wpilib-tools/robot-simulation/index.html"><div class="wl-core-title">Simulation</div><div class="wl-core-desc">Test robot code on your laptop : no hardware required.</div></a>
     <a class="wl-core-card" href="https://github.wpilib.org/allwpilib/docs/release/java/index.html"><div class="wl-core-title">API Reference</div><div class="wl-core-desc">Java, C++, and Python class and method documentation.</div></a>
   </div>

   <div style="margin-top:8px;padding:14px 18px;
      background:var(--color-background-secondary,#f8f8f8);
      border:1px solid var(--color-background-border,#ddd);
      border-radius:6px;font-size:0.85rem;line-height:1.6;
      color:var(--color-foreground-secondary,#555);">
     <strong>Still using a roboRIO?</strong>
     This site covers the 2027 Systemcore-based control system.
     For roboRIO documentation, visit the
     <a href="https://docs.wpilib.org/en/stable/index.html"
        style="font-weight:600;">2026 WPILib docs (docs.wpilib.org)</a>.
   </div>

----

.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :hidden:

   docs/zero-to-robot/introduction
   docs/zero-to-robot/step-1/index
   docs/zero-to-robot/step-2/index
   docs/zero-to-robot/step-3/index
   docs/zero-to-robot/step-4/index

.. toctree::
   :maxdepth: 1
   :caption: FTC and FRC Notes
   :hidden:

   docs/ftc/index

.. toctree::
   :maxdepth: 1
   :caption: What's New for 2027
   :hidden:

   docs/yearly-overview/index

.. toctree::
   :maxdepth: 1
   :caption: FRC Robot Hardware
   :hidden:

   docs/controls-overviews/control-system-hardware
   docs/hardware/hardware-basics/hardware-overview
   docs/hardware/hardware-basics/status-lights-ref

.. toctree::
   :maxdepth: 1
   :caption: Writing Robot Code
   :hidden:

   docs/controls-overviews/control-system-software
   docs/software/what-is-wpilib
   docs/software/vscode-overview/index
   docs/software/vscode-overview/3rd-party-libraries
   docs/software/dashboards/index
   docs/software/telemetry/index
   docs/software/hardware-apis/index
   docs/software/can-devices/index
   docs/software/basic-programming/index
   docs/software/python/index
   docs/software/examples-tutorials/wpilib-examples
   docs/software/examples-tutorials/third-party-examples
   docs/software/support/support-resources
   docs/software/frc-glossary

.. toctree::
   :maxdepth: 1
   :caption: Controls and Autonomy
   :hidden:

   docs/software/commandbased/index
   docs/software/pathplanning/index
   docs/software/advanced-controls/index
   docs/software/wpilib-tools/robot-simulation/index

.. toctree::
   :maxdepth: 1
   :caption: Tools and Dashboards
   :hidden:

   docs/software/driverstation/index
   docs/software/wpilib-tools/outlineviewer/index
   docs/software/wpilib-tools/wpical/index
   docs/networking/networking-introduction/index
   docs/networking/networking-utilities/index

.. toctree::
   :maxdepth: 1
   :caption: Practice with XRP
   :hidden:

   docs/xrp-robot/index
   docs/romi-robot/index

.. toctree::
   :maxdepth: 1
   :caption: API Reference
   :hidden:

   WPILib Java API Docs <https://github.wpilib.org/allwpilib/docs/release/java/index.html>
   WPILib C++ API Docs <https://github.wpilib.org/allwpilib/docs/release/cpp/index.html>
   WPILib Python API Docs <https://robotpy.readthedocs.io/projects/robotpy/en/stable/>

.. toctree::
   :maxdepth: 1
   :caption: Contributing
   :hidden:

   docs/contributing/wpilib-docs/index
   docs/contributing/wpilib/index
   docs/legal/privacy-policy

.. toctree::
   :maxdepth: 1
   :caption: Report an Issue
   :hidden:

   Report an Issue <https://github.com/wpilibsuite/frc-docs/issues>
