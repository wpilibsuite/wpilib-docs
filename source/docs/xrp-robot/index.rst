.. include:: <isonum.txt>

# Getting Started with XRP

The XRP (eXperimental Robot Platform), powered by
[Worcester Polytechnic Institute](http://wpi.edu), is a small, low-cost robot
designed for learning WPILib programming without full FRC hardware.
The same tools, language, and code patterns used for full FRC robots work on the XRP.

.. raw:: html


   <!-- ── WHY XRP ── -->
   <p class="sw-section-h">Why Use the XRP?</p>

   <div class="sw-grid sw-grid-4">

     <div class="sw-card sw-card-shared">
       <div class="sw-label sw-label-shared">Learn</div>
       <div class="sw-card-title">Real WPILib Code</div>
       <div class="sw-card-desc">
         Write the same Java, C++, or Python code you would deploy to
         a full FRC robot.
       </div>
     </div>

     <div class="sw-card sw-card-shared">
       <div class="sw-label sw-label-shared">Practice</div>
       <div class="sw-card-title">No Control System Required</div>
       <div class="sw-card-desc">
         No roboRIO, no PDH, no radio programming. Just the XRP,
         a USB cable for initial setup, and your laptop.
       </div>
     </div>

     <div class="sw-card sw-card-shared">
       <div class="sw-label sw-label-shared">Pre-season</div>
       <div class="sw-card-title">Off-Season Programming</div>
       <div class="sw-card-desc">
         Learn command-based programming, encoders, PID, and odometry
         before build season starts &mdash; on a desk.
       </div>
     </div>

     <div class="sw-card sw-card-ftc">
       <div class="sw-label sw-label-ftc">FTC 2027-2028+</div>
       <div class="sw-card-title">FTC Prep</div>
       <div class="sw-card-desc">
         Systemcore teams use the same WPILib toolchain. XRP skills
         transfer directly to FTC robot programming.
       </div>
     </div>

   </div>

   <!-- ── HOW IT WORKS ── -->
   <p class="sw-section-h">How It Works</p>

   <div class="sw-tip">
     XRP code runs on your <strong>laptop as a simulation</strong>, communicating
     with the XRP hardware over Wi-Fi. You use the same
     <strong>WPILib VS Code tools and Driver Station</strong> as FRC &mdash;
     the XRP just appears as a simulated robot that drives real motors.
   </div>

   <div class="sw-grid sw-grid-3">
     <div class="sw-card">
       <div class="sw-card-title">Create an XRP project</div>
       <div class="sw-card-desc">
         Use the WPILib VS Code extension you already installed.
         XRP projects use the same project structure as FRC.
       </div>
     </div>
     <div class="sw-card">
       <div class="sw-card-title">Run as simulation</div>
       <div class="sw-card-desc">
         Launch with <strong>Simulate Robot Code</strong> instead of
         Deploy. The simulation connects to the XRP over Wi-Fi.
       </div>
     </div>
     <div class="sw-card">
       <div class="sw-card-title">Drive with Driver Station</div>
       <div class="sw-card-desc">
         Open the FRC Driver Station (Windows) and enable TeleOp.
         Your joystick controls the XRP just like a full robot.
       </div>
     </div>
   </div>

   <!-- ── HARDWARE SPECS ── -->
   <p class="sw-section-h">Hardware Specifications</p>

   <table class="sw-tbl">
     <thead>
       <tr><th>Component</th><th>Details</th></tr>
     </thead>
     <tbody>
       <tr><td><strong>Processor</strong></td>
         <td>Raspberry Pi RP2040 dual-core Cortex-M0+ at 133 MHz</td></tr>
       <tr><td><strong>Wireless</strong></td>
         <td>Wi-Fi 802.11 b/g/n (2.4 GHz) for host communication</td></tr>
       <tr><td><strong>Drive motors</strong></td>
         <td>2 brushed DC gear motors with integrated quadrature encoders</td></tr>
       <tr><td><strong>IMU</strong></td>
         <td>Built-in 6-axis LSM6DS3 (gyro + accelerometer)</td></tr>
       <tr><td><strong>Servo ports</strong></td>
         <td>2 user servo outputs</td></tr>
       <tr><td><strong>User I/O</strong></td>
         <td>Reflectance sensor, ultrasonic distance sensor port</td></tr>
       <tr><td><strong>Power</strong></td>
         <td>USB-C or 3xAA battery pack</td></tr>
       <tr><td><strong>Cost</strong></td>
         <td>~$75 USD assembled (WPI / SparkFun)</td></tr>
     </tbody>
   </table>

   <!-- ── XRP vs FRC ── -->
   <p class="sw-section-h">XRP vs Full FRC Robot</p>

   <table class="sw-tbl">
     <thead>
       <tr><th>Feature</th><th>XRP</th><th>FRC Robot</th></tr>
     </thead>
     <tbody>
       <tr><td>WPILib API</td>
         <td>&#10003; Same Java/C++/Python API</td>
         <td>&#10003; Full API</td></tr>
       <tr><td>Command-based</td>
         <td>&#10003; Yes</td><td>&#10003; Yes</td></tr>
       <tr><td>Encoders</td>
         <td>&#10003; Integrated</td>
         <td>External (per motor controller)</td></tr>
       <tr><td>IMU / gyro</td>
         <td>&#10003; Built-in</td>
         <td>External (NavX, Pigeon 2)</td></tr>
       <tr><td>Driver Station</td>
         <td>&#10003; Same (Windows)</td>
         <td>&#10003; Same (Windows)</td></tr>
       <tr><td>Deploy method</td>
         <td>Simulate (Wi-Fi to laptop)</td>
         <td>Deploy to roboRIO/Systemcore</td></tr>
       <tr><td>CAN bus</td>
         <td>&#10007; Not available</td>
         <td>&#10003; Full CAN support</td></tr>
       <tr><td>Vendor libraries</td>
         <td>Not applicable</td>
         <td>REVLib, Phoenix 6, etc.</td></tr>
       <tr><td>Cost</td>
         <td>~$75</td><td>$3,000&ndash;$10,000+</td></tr>
     </tbody>
   </table>

   <!-- ── PREREQUISITES ── -->
   <p class="sw-section-h">Prerequisites</p>

   <div class="sw-grid sw-grid-2">
     <div class="sw-card">
       <div class="sw-card-title">Software (all platforms)</div>
       <ul style="font-size:0.875rem;line-height:1.8;margin:8px 0 0;padding-left:20px;">
         <li>WPILib installed (see
           <a href="../zero-to-robot/step-2/wpilib-setup.html">WPILib setup</a>)
         </li>
         <li>FRC Driver Station (Windows &mdash; for enabling)</li>
         <li>XRP firmware flashed on the board</li>
       </ul>
     </div>
     <div class="sw-card">
       <div class="sw-card-title">Hardware</div>
       <ul style="font-size:0.875rem;line-height:1.8;margin:8px 0 0;padding-left:20px;">
         <li>XRP robot kit (assembled)</li>
         <li>USB-C cable (for initial firmware flash)</li>
         <li>3&times;AA batteries or USB-C power bank</li>
         <li>2.4 GHz Wi-Fi on your laptop</li>
       </ul>
     </div>
   </div>

   <!-- ── GETTING STARTED ── -->
   <p class="sw-section-h">Getting Started</p>

   <div class="sw-grid sw-grid-3">

     <a class="sw-card sw-card-shared" href="hardware-and-imaging.html">
       <span class="sw-step-num">01</span>
       <div class="sw-card-title">Set Up Hardware</div>
       <div class="sw-card-desc">
         Flash XRP firmware, insert batteries, and connect to the XRP
         Wi-Fi network.
       </div>
     </a>

     <a class="sw-card sw-card-shared" href="getting-to-know-xrp.html">
       <span class="sw-step-num">02</span>
       <div class="sw-card-title">Get to Know the XRP</div>
       <div class="sw-card-desc">
         Sensor locations, motor wiring, the web UI, and what each
         I/O port is for.
       </div>
     </a>

     <a class="sw-card sw-card-shared" href="programming-xrp.html">
       <span class="sw-step-num">03</span>
       <div class="sw-card-title">Write and Run Code</div>
       <div class="sw-card-desc">
         Create an XRP project in WPILib VS Code, run the simulation,
         and drive your robot.
       </div>
     </a>

   </div>

   <!-- ── EXAMPLE PROJECTS ── -->
   <p class="sw-section-h">Example Projects</p>

   <div class="sw-grid sw-grid-2">
     <a class="sw-card sw-card-frc" href="programming-xrp.html">
       <div class="sw-card-title">XRP Arcade Drive</div>
       <div class="sw-card-desc">
         Basic teleop drive using a joystick. Good first project.
       </div>
     </a>
     <a class="sw-card sw-card-frc" href="hardware-support.html">
       <div class="sw-card-title">Sensors and Encoders</div>
       <div class="sw-card-desc">
         Read encoder distances, gyro heading, and reflectance sensor.
       </div>
     </a>
   </div>

   <div class="sw-tip">
     <strong>FIRST Training courses available.</strong>
     <a href="https://training.firstinspires.org/catalog?labels=%5B%22Topics%22%5D&values=%5B%22Programming%22%5D">
     Part 1</a> covers setup, methods, objects, and variables.
     <a href="https://training.firstinspires.org/courses/java-programming-part-2">
     Part 2</a> covers command-based programming, drive inputs, and arrays.
   </div>

.. toctree::
   :maxdepth: 1
   :hidden:

   hardware-and-imaging
   getting-to-know-xrp
   hardware-support
   web-ui
   programming-xrp
