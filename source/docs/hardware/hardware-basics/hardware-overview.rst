.. include:: <isonum.txt>

# FRC Control System Hardware Overview

This page summarizes every major hardware component in the FRC\ |reg| control system.
Use it as a reference when wiring or troubleshooting your robot.

.. raw:: html


   <div class="sw-note">
     <strong>FRC + FTC:</strong> This page covers the FRC control system.
     FTC teams using Systemcore and Motioncore (2027-2028+) share the same
     WPILib programming model &mdash; see the
     <a href="../../ftc/index.html">FTC section</a> for hardware specifics.
   </div>

   <!-- ── CONTROL HUB ── -->
   <p class="sw-section-h">Main Controller</p>

   <div class="sw-card sw-card-frc" style="margin-bottom:14px;">
     <div class="sw-label sw-label-frc">FRC 2027+ / FTC 2027-2028+</div>
     <div class="sw-card-title">Systemcore</div>
     <div class="sw-card-desc">
       The primary robot controller for FRC (2027+) and FTC (2027-2028+).
       Runs robot code in Java, C++, or Python. Supports CAN, PWM, DIO,
       and analog I/O. Connects over Ethernet or USB for deployment and
       supports the full WPILib simulation framework.
     </div>
   </div>

   <table class="sw-tbl">
     <thead>
       <tr><th>Spec</th><th>Systemcore</th></tr>
     </thead>
     <tbody>
       <tr><td><strong>Languages</strong></td>
         <td>Java, C++, Python</td></tr>
       <tr><td><strong>CAN bus</strong></td>
         <td>Yes</td></tr>
       <tr><td><strong>PWM outputs</strong></td>
         <td>Yes</td></tr>
       <tr><td><strong>DIO</strong></td>
         <td>Yes</td></tr>
       <tr><td><strong>Analog inputs</strong></td>
         <td>Yes</td></tr>
       <tr><td><strong>Connectivity</strong></td>
         <td>Ethernet, USB</td></tr>
       <tr><td><strong>Deploy method</strong></td>
         <td>USB or Wi-Fi via VS Code / OnBot</td></tr>
       <tr><td><strong>Simulation</strong></td>
         <td>Full desktop simulation support</td></tr>
       <tr><td><strong>Programs</strong></td>
         <td>FRC (2027+) and FTC via Motioncore (2027-2028+)</td></tr>
     </tbody>
   </table>

   <!-- ── POWER DISTRIBUTION ── -->
   <p class="sw-section-h">Power Distribution</p>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card sw-card-frc">
       <div class="sw-label sw-label-frc">REV Robotics</div>
       <div class="sw-card-title">Power Distribution Hub (PDH)</div>
       <div class="sw-card-desc">
         20 switchable high-current ports (40 A max each), 3 low-current
         ports, and a main breaker slot. CAN-connected for per-channel
         current monitoring. Rectangular form factor.
       </div>
     </div>
     <div class="sw-card sw-card-frc">
       <div class="sw-label sw-label-frc">CTRE</div>
       <div class="sw-card-title">Power Distribution Panel (PDP)</div>
       <div class="sw-card-desc">
         16 high-current ports (40 A max each) plus 8 lower-current ports.
         CAN-connected for current monitoring. Oval form factor.
         Legal but older; PDH is preferred for new builds.
       </div>
     </div>
   </div>

   <table class="sw-tbl">
     <thead>
       <tr><th>Feature</th><th>PDH (REV)</th><th>PDP (CTRE)</th></tr>
     </thead>
     <tbody>
       <tr><td>High-current ports</td><td>20 (40 A each)</td>
         <td>16 (40 A each)</td></tr>
       <tr><td>Low-current ports</td><td>3 (20 A each)</td>
         <td>8 (20 A each)</td></tr>
       <tr><td>Main breaker slot</td><td>Yes (120 A SB)</td>
         <td>Yes (120 A SB)</td></tr>
       <tr><td>CAN monitoring</td><td>Yes (per channel)</td>
         <td>Yes (aggregate)</td></tr>
       <tr><td>Switchable outputs</td><td>Yes (software)</td><td>No</td></tr>
     </tbody>
   </table>

   <!-- ── RADIO ── -->
   <p class="sw-section-h">Robot Radio</p>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card sw-card-frc">
       <div class="sw-label sw-label-frc">FRC Standard</div>
       <div class="sw-card-title">Vivid VH109</div>
       <div class="sw-card-desc">
         The standard FRC robot radio. Must be programmed annually with the
         FRC Radio Configuration Utility to set team number, SSID, and firmware.
         Powered via VRM barrel connector.
       </div>
     </div>
     <div class="sw-card sw-card-frc">
       <div class="sw-label sw-label-frc">FRC Legal</div>
       <div class="sw-card-title">OpenMesh OM5P-AC</div>
       <div class="sw-card-desc">
         Updated version of the OM5P-AN with the same FRC configuration
         process. 802.11ac support. Preferred for new builds.
       </div>
     </div>
   </div>

   <!-- ── MOTOR CONTROLLERS ── -->
   <p class="sw-section-h">Motor Controllers</p>

   <table class="sw-tbl">
     <thead>
       <tr>
         <th>Controller</th><th>Vendor</th><th>Interface</th>
         <th>Max current</th><th>Notes</th>
       </tr>
     </thead>
     <tbody>
       <tr><td><strong>SPARK MAX</strong></td><td>REV</td>
         <td>CAN or PWM</td><td>40 A</td>
         <td>Brushed and brushless (NEO). Most common for new teams.</td></tr>
       <tr><td><strong>SPARK Flex</strong></td><td>REV</td>
         <td>CAN or PWM</td><td>60 A</td>
         <td>Higher current; NEO Vortex motor.</td></tr>
       <tr><td><strong>Talon FX</strong></td><td>CTRE</td>
         <td>CAN</td><td>120 A peak</td>
         <td>Integrated with Falcon 500 and Kraken X60 motors.</td></tr>
       <tr><td><strong>Victor SPX</strong></td><td>CTRE</td>
         <td>CAN or PWM</td><td>40 A</td>
         <td>Lower cost. Brushed only.</td></tr>
     </tbody>
   </table>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card">
       <div class="sw-card-title">CAN bus (recommended)</div>
       <div class="sw-card-desc">
         Two-wire daisy-chain. Enables telemetry (current, temperature,
         velocity), firmware updates over the wire, and advanced
         closed-loop control on the controller itself. Requires correct
         termination at both ends of the chain.
       </div>
     </div>
     <div class="sw-card">
       <div class="sw-card-title">PWM (simpler fallback)</div>
       <div class="sw-card-desc">
         Three-wire (signal, +5 V, GND) from roboRIO PWM port.
         No telemetry. Easier to debug. Acceptable for rookie builds
         or when CAN is not supported.
       </div>
     </div>
   </div>

   <!-- ── PNEUMATICS ── -->
   <p class="sw-section-h">Pneumatics</p>

   <table class="sw-tbl">
     <thead>
       <tr>
         <th>Module</th><th>Vendor</th><th>Solenoid channels</th>
         <th>Pressure switch</th><th>Notes</th>
       </tr>
     </thead>
     <tbody>
       <tr><td><strong>Pneumatic Hub (PH)</strong></td><td>REV</td>
         <td>16 (CAN)</td><td>Analog + digital</td>
         <td>Preferred for new builds. Analog pressure sensing.</td></tr>
       <tr><td><strong>PCM</strong></td><td>CTRE</td>
         <td>8 (CAN)</td><td>Digital only</td>
         <td>Older module, still legal.</td></tr>
     </tbody>
   </table>

   <!-- ── SENSORS ── -->
   <p class="sw-section-h">Common Sensors</p>

   <table class="sw-tbl">
     <thead>
       <tr>
         <th>Sensor</th><th>Interface</th><th>Use case</th>
         <th>FRC + XRP</th>
       </tr>
     </thead>
     <tbody>
       <tr><td><strong>Quadrature encoder</strong></td>
         <td>DIO (2 channels)</td>
         <td>Wheel distance and velocity</td>
         <td><span class="sw-label sw-label-shared" style="margin:0">Shared</span></td></tr>
       <tr><td><strong>NavX / Pigeon 2 IMU</strong></td>
         <td>SPI / CAN</td>
         <td>Heading, gyro, accelerometer</td>
         <td><span class="sw-label sw-label-frc" style="margin:0">FRC</span></td></tr>
       <tr><td><strong>Limit switch</strong></td>
         <td>DIO</td>
         <td>Hard stop detection</td>
         <td><span class="sw-label sw-label-frc" style="margin:0">FRC</span></td></tr>
       <tr><td><strong>Ultrasonic (ping-echo)</strong></td>
         <td>DIO (2 channels)</td>
         <td>Distance measurement</td>
         <td><span class="sw-label sw-label-shared" style="margin:0">Shared</span></td></tr>
       <tr><td><strong>AprilTag camera</strong></td>
         <td>USB / Ethernet</td>
         <td>Field localization and pose estimation</td>
         <td><span class="sw-label sw-label-frc" style="margin:0">FRC</span></td></tr>
       <tr><td><strong>Color sensor (REV)</strong></td>
         <td>I2C</td>
         <td>Game piece detection</td>
         <td><span class="sw-label sw-label-frc" style="margin:0">FRC</span></td></tr>
     </tbody>
   </table>

   <!-- ── OTHER ── -->
   <p class="sw-section-h">Other Components</p>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card">
       <div class="sw-label sw-label-frc">FRC</div>
       <div class="sw-card-title">Voltage Regulator Module (VRM)</div>
       <div class="sw-card-desc">
         Powers the radio (12 V / 2 A) and other 5 V accessories.
         Plugs into a dedicated PDH/PDP port. Required for radio power
         on most builds.
       </div>
     </div>
     <div class="sw-card">
       <div class="sw-label sw-label-frc">FRC</div>
       <div class="sw-card-title">Driver Station Laptop</div>
       <div class="sw-card-desc">
         Windows 11 required (2027+). Runs the FRC Driver Station
         software to communicate with and enable the robot.
         Connected to robot radio over Wi-Fi at competition.
       </div>
     </div>
   </div>

   <!-- ── WHAT'S NEXT ── -->
   <p class="sw-section-h">What&rsquo;s Next</p>

   <div class="sw-grid sw-grid-3">
     <a class="sw-card sw-card-frc"
        href="../../zero-to-robot/step-1/intro-to-frc-robot-wiring.html">
       <div class="sw-card-title">Wiring Guide</div>
       <div class="sw-card-desc">
         Step-by-step control system wiring with diagrams.
       </div>
     </a>
     <a class="sw-card sw-card-frc"
        href="../../zero-to-robot/step-3/imaging-your-roborio.html">
       <div class="sw-card-title">Image the roboRIO</div>
       <div class="sw-card-desc">
         Required every season before deploying code.
       </div>
     </a>
     <a class="sw-card sw-card-frc"
        href="status-lights-ref.html">
       <div class="sw-card-title">Status Light Reference</div>
       <div class="sw-card-desc">
         Decode LED patterns on the roboRIO, radio, and motor
         controllers.
       </div>
     </a>
   </div>
