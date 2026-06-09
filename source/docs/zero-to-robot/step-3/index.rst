# Step 3: Configure Your Control System

.. raw:: html


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
