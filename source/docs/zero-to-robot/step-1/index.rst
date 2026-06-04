# Step 1: Build Your Robot

.. raw:: html

   <style>
   :root { --frc:#009CD7; --frc-light:#e6f6fc; --ftc:#e07000; --ftc-light:#fff3e0; --shared:#2e7d32; --shared-light:#f1f8f1; }
   .sw-label { display:inline-block; font-size:0.7rem; font-weight:700; text-transform:uppercase;
     letter-spacing:0.06em; padding:2px 8px; border-radius:4px; margin-bottom:10px; }
   .sw-label-frc { background:var(--frc); color:#fff; }
   .sw-label-ftc { background:var(--ftc); color:#fff; }
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
   .sw-card-ftc { border-color:rgba(224,112,0,0.3); background:var(--ftc-light);
     opacity:0.65; cursor:default; }
   a.sw-card-ftc:hover { border-color:var(--ftc);
     box-shadow:0 2px 10px rgba(224,112,0,0.15); }
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
   .sw-order { counter-reset:wiring-step; list-style:none;
     padding:0; margin:0 0 24px; }
   .sw-order li { counter-increment:wiring-step; display:flex;
     align-items:flex-start; gap:14px; margin-bottom:10px;
     padding:12px 16px; border-radius:6px;
     border:1px solid var(--color-background-border,#ddd);
     background:var(--color-background-primary,#fff);
     font-size:0.875rem; line-height:1.55; }
   .sw-order li::before { content:counter(wiring-step);
     font-size:0.8rem; font-weight:800; color:#fff;
     background:var(--frc); border-radius:50%;
     width:22px; height:22px; display:flex; align-items:center;
     justify-content:center; flex-shrink:0; font-family:monospace; }
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
   @media(max-width:700px) { .sw-grid-2 { grid-template-columns:1fr; } }
   </style>

   <!-- Step badge -->
   <div class="sw-step-badge">
     <span class="sw-step-n">01</span>
     <div>
       <div class="sw-step-info-title">Build Your Robot</div>
       <div class="sw-step-info-sub">Step 1 of 4</div>
     </div>
   </div>

   <p style="font-size:0.9rem;margin-bottom:20px;color:var(--color-foreground-secondary,#444);">
     Choose the wiring guide for your program below.
   </p>

   <p style="font-size:0.8rem;font-weight:700;text-transform:uppercase;
      letter-spacing:0.05em;color:var(--frc);margin:0 0 10px;">
     FRC
   </p>

   <div class="sw-grid sw-grid-2" style="margin-bottom:20px;">

     <a class="sw-card sw-card-frc"
        href="basic-robot-wiring.html">
       <div class="sw-label sw-label-frc">FRC</div>
       <div class="sw-card-title">Basic Robot Wiring</div>
       <div class="sw-card-desc">
         Simplified wiring reference for drivetrain-only builds.
         Good starting point for rookie teams.
       </div>
     </a>

     <a class="sw-card sw-card-frc"
        href="intro-to-frc-robot-wiring.html">
       <div class="sw-label sw-label-frc">FRC</div>
       <div class="sw-card-title">FRC Robot Wiring Overview</div>
       <div class="sw-card-desc">
         Full walkthrough of control system wiring with diagrams:
         PDH, Systemcore, radio, motor controllers, and pneumatics.
       </div>
     </a>

   </div>

   <div class="sw-tip">
     <strong>Not sure which PDH or PDP you have?</strong>
     The <strong>Power Distribution Hub (PDH)</strong> is the REV Robotics unit
     (rectangular, 20 slots). The older
     <strong>Power Distribution Panel (PDP)</strong> is the Cross The Road
     Electronics unit (oval shape, 16 slots). Both are legal &mdash; wiring
     diagrams for each are in the wiring overview above.
   </div>

   <p style="font-size:0.8rem;font-weight:700;text-transform:uppercase;
      letter-spacing:0.05em;color:var(--ftc);margin:0 0 10px;">
     FTC
   </p>

   <div class="sw-grid sw-grid-2" style="margin-bottom:20px;">

     <div class="sw-card sw-card-ftc">
       <div class="sw-label sw-label-ftc">FTC &mdash; Coming Soon</div>
       <div class="sw-card-title">Basic FTC Robot Wiring</div>
       <div class="sw-card-desc">
         Simplified wiring guide for Systemcore and Motioncore.
         Good starting point for rookie FTC teams.
       </div>
     </div>

     <div class="sw-card sw-card-ftc">
       <div class="sw-label sw-label-ftc">FTC &mdash; Coming Soon</div>
       <div class="sw-card-title">FTC Robot Wiring Overview</div>
       <div class="sw-card-desc">
         Full walkthrough of FTC control system wiring with diagrams:
         Systemcore, Motioncore, motor controllers, and power.
       </div>
     </div>

   </div>

   

   <!-- Nav -->
   <div class="sw-nav">
     <a class="sw-nav-btn" href="../introduction.html">&larr; Introduction</a>
     <a class="sw-nav-btn sw-next" href="../step-2/index.html">
       Step 2: Install Your Tools &rarr;</a>
   </div>

.. toctree::
   :maxdepth: 1
   :hidden:

   FRC Robot Wiring Overview <intro-to-frc-robot-wiring>
   Basic Robot Wiring <basic-robot-wiring>
