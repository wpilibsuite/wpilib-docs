# Step 3: Configure Your Control System

.. raw:: html

   <!-- Step badge -->
   <div class="sw-step-badge">
     <span class="sw-step-n">03</span>
     <div>
       <div class="sw-step-info-title">Configure Your Control System</div>
       <div class="sw-step-info-sub">Step 3 of 4</div>
     </div>
   </div>

Before you can deploy code, the Systemcore must be configured with the
current season's software and the radio must be programmed for your
team number. Both tasks require a Windows computer with FRC Game Tools installed.

.. warning::

   **Re-configure every season.**
   The Systemcore image is season-specific. A robot that worked last year will
   not accept code deploys until the Systemcore is updated with the current
   year's image.

.. rubric:: Part 1 — Configure the Systemcore

Use the FRC Game Tools to flash the current season's image to your Systemcore.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Configure Systemcore
      :link: imaging-your-systemcore
      :link-type: doc
      :class-card: sw-card-frc

      **Systemcore**
      ^^^
      Use the FRC Game Tools imaging utility to flash the current
      season's image. Connect via USB or Ethernet.

   .. grid-item-card:: Using a roboRIO?
      :link: https://docs.wpilib.org/en/stable/index.html
      :link-type: url

      **Legacy**
      ^^^
      Teams still running a roboRIO should refer to the
      `2026 WPILib docs <https://docs.wpilib.org/en/stable/index.html>`_
      for imaging instructions.

.. rubric:: Part 2 — Configure the Radio

The Vivid VH109 radio must be programmed with your team number
and the correct firmware before the robot can communicate wirelessly.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Radio Programming
      :link: radio-programming
      :link-type: doc
      :class-card: sw-card-frc

      **Standard**
      ^^^
      Program the Vivid VH109 using the FRC Radio Configuration
      Utility. Sets team number, SSID, and firmware.

   .. grid-item-card:: Legacy OpenMesh Radios
      :link: openmesh
      :link-type: doc
      :class-card: sw-card-frc

      **Reference**
      ^^^
      Hardware specs, indicator LED meanings, and troubleshooting.

.. rubric:: Part 3 — Verify Power-Up

- Systemcore boots and status light cycles
- Radio powers on
- Radio SSID appears as <TEAM>_Robot in Wi-Fi list
- Connect laptop to robot Wi-Fi — Driver Station shows "Robot Communication" in green

.. raw:: html

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
