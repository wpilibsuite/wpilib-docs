# Step 3: Configure Your Control System

.. raw:: html

   <style>
   :root { --frc:#009CD7; --frc-light:#e6f6fc; --shared:#2e7d32; --shared-light:#f1f8f1; }
   .sw-label { display:inline-block; font-size:0.7rem; font-weight:700; text-transform:uppercase;
     letter-spacing:0.06em; padding:2px 8px; border-radius:4px; margin-bottom:10px; }
   .sw-label-frc { background:var(--frc); color:#fff; }
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
   .sw-card-frc { border-color:rgba(0,156,215,0.3); }
   a.sw-card-frc:hover { border-color:var(--frc);
     box-shadow:0 2px 10px rgba(0,156,215,0.15); }
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
   .sw-checklist { list-style:none; padding:0; margin:0 0 20px; }
   .sw-checklist li { display:flex; align-items:baseline; gap:10px;
     font-size:0.875rem; line-height:1.6; padding:7px 0;
     border-bottom:1px solid var(--color-background-border,#eee); }
   .sw-checklist li::before { content:"&#9744;"; font-size:1rem;
     flex-shrink:0; color:var(--frc); }
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
   .sw-nav-btn.sw-next:hover { background:#007ab0; border-color:#007ab0; }
   .sw-nav-btn.sw-next:visited { color:#fff; }
   @media(max-width:700px) {
     .sw-grid-2,.sw-grid-3 { grid-template-columns:1fr; } }
   </style>

   <!-- Step badge -->
   <div class="sw-step-badge">
     <span class="sw-step-n">03</span>
     <div>
       <div class="sw-step-info-title">Configure Your Control System</div>
       <div class="sw-step-info-sub">
         Step 3 of 4
       </div>
     </div>
   </div>

   <p style="font-size:0.9rem;margin-bottom:20px;
      color:var(--color-foreground-secondary,#444);">
     Before you can deploy code, the Systemcore must be configured with the
     current season&rsquo;s software and the radio must be programmed for your
     team number. Both tasks require a Windows computer with FRC Game Tools installed.
   </p>

   <div class="sw-warn">
     <strong>Re-configure every season.</strong>
     The Systemcore image is season-specific. A robot that worked last year will
     not accept code deploys until the Systemcore is updated with the current
     year&rsquo;s image.
   </div>

   <!-- Systemcore -->
   <p class="sw-section-h">Part 1: Configure the Systemcore</p>
   <p style="font-size:0.875rem;margin-bottom:14px;
      color:var(--color-foreground-secondary,#555);">
     Use the FRC Game Tools to flash the current season&rsquo;s image to your Systemcore.
   </p>

   <div class="sw-grid sw-grid-2">

     <a class="sw-card sw-card-frc" href="imaging-your-roborio.html">
       <div class="sw-part-num">Systemcore</div>
       <div class="sw-card-title">Configure Systemcore</div>
       <div class="sw-card-desc">
         Use the FRC Game Tools imaging utility to flash the current
         season&rsquo;s image. Connect via USB or Ethernet.
       </div>
     </a>

     <div class="sw-card">
       <div class="sw-part-num">Legacy</div>
       <div class="sw-card-title">Using a roboRIO?</div>
       <div class="sw-card-desc">
         Teams still running a roboRIO should refer to the
         <a href="https://docs.wpilib.org/en/stable/index.html">2026 WPILib docs</a>
         for imaging instructions.
       </div>
     </div>

   </div>

   <!-- Radio -->
   <p class="sw-section-h">Part 2 &mdash; Configure the Radio</p>
   <p style="font-size:0.875rem;margin-bottom:14px;
      color:var(--color-foreground-secondary,#555);">
     The Vivid VH109 radio must be programmed with your team number
     and the correct firmware before the robot can communicate wirelessly.
   </p>

   <div class="sw-grid sw-grid-2">

     <a class="sw-card sw-card-frc" href="radio-programming.html">
       <div class="sw-part-num">Standard</div>
       <div class="sw-card-title">Radio Programming</div>
       <div class="sw-card-desc">
         Program the Vivid VH109 using the FRC Radio Configuration
         Utility. Sets team number, SSID, and firmware.
       </div>
     </a>

     <a class="sw-card sw-card-frc" href="openmesh.html">
       <div class="sw-part-num">Reference</div>
       <div class="sw-card-title">Legacy OpemMesh Radios</div>
       <div class="sw-card-desc">
         Hardware specs, indicator LED meanings, and troubleshooting
       </div>
     </a>

   </div>

   <!-- Power-up verification -->
   <p class="sw-section-h">Part 3 &mdash; Verify Power-Up</p>

   <ul class="sw-checklist">
     <li>Systemcore boots and status light cycles</li>
     <li>Radio powers on </li>
     <li>Radio SSID appears as < in Wi-Fi list</li>
     <li>Connect laptop to robot Wi-Fi &mdash; Driver Station shows
       &ldquo;Robot Communication&rdquo; in green</li>
   </ul>

   <!-- Nav -->
   <div class="sw-nav">
     <a class="sw-nav-btn" href="../step-2/index.html">
       &larr; Step 2: Install Your Tools</a>
     <a class="sw-nav-btn sw-next" href="../step-4/index.html">
       Step 4: Write and Drive &rarr;</a>
   </div>

.. toctree::
   :maxdepth: 1
   :hidden:

   radio-programming
   openmesh
