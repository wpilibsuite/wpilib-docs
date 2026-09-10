# Step 1: Build and Wire Your Robot

.. container:: sw-step-badge

   .. container:: sw-step-n

      01

   .. container::

      .. container:: sw-step-info-title

         Build and Wire Your Robot

      .. container:: sw-step-info-sub

         Step 1 of 4

**By the end of this step:** your drivetrain and control system will be
assembled, Systemcore will power on, and its web interface will open from your
computer.

Before starting, turn robot power **Off** and disconnect the battery. For FRC,
switch the main breaker off; for FTC, use the robot's power switch. Keep the
drivetrain safely supported so the wheels cannot move the robot during later
testing.

.. rubric:: What You Need for This Step

.. list-table::
   :header-rows: 1
   :widths: 28 36 36

   * - For every build
     - Alpha Systemcore power
     - Beta Systemcore power
   * - Systemcore and robot battery
     - 18 AWG red and black wire
     - Provided MicroFit Pwr/Bridge cable, when using Motioncore
   * - Compatible power distribution hardware
     - White Weidmuller ferrules and a ferrule crimper
     - Provided MicroFit-to-XT30 cable, when not using Motioncore
   * - Computer with Wi-Fi or a data-capable USB cable
     - Wire stripper and small flat-blade screwdriver
     - Matching XT30 extension only if bare-wire power is required

Do not prepare or connect power wiring until you have identified whether your
Systemcore is an Alpha or Beta unit. Alpha units were distributed during the
initial FRC alpha test; FTC test units are Beta hardware. If the revision is
unclear, check the unit and kit labeling before continuing.

.. TODO: Add a labeled comparison photo showing how to identify Alpha and Beta
   Systemcore hardware.

.. rubric:: Part 1: Assemble Your Robot

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Kitbot / Starter Bot Assembly
      :link: kitbot-starterbot-assembly
      :link-type: doc
      :class-card: sw-card-shared

      **FRC + FTC**
      ^^^
      Step-by-step guide to assembling the FRC Kit of Parts chassis or
      an FTC starter bot into a drive-ready robot.

.. rubric:: Part 2: Power the Systemcore

How you power the Systemcore depends on your hardware revision.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Alpha Systemcore
      :class-card: sw-card-shared

      Connect Systemcore directly to the robot's power distribution board.
      Use 18 AWG wire with white Weidmuller ferrules.

   .. grid-item-card:: Beta Systemcore
      :class-card: sw-card-shared

      Power Systemcore through the MicroFit Pwr/Bridge port only.

      - With Motioncore, connect Systemcore's Pwr/Bridge port to Motioncore's
        Bridge port using a provided MicroFit cable.
      - Without Motioncore, use the included MicroFit-to-XT30 cable. If bare
        wires are required, cut the ends from an XT30 extension cable.

.. warning::

   Do not use both power inputs on Alpha units (Bridge + Weidmuller)
   at the same time.

.. TODO: Add a close-up photo showing the Systemcore Pwr/Bridge connector and
   correct MicroFit cable orientation.

Use the provided cables whenever possible. If your team must build a cable,
follow the `Systemcore and Motioncore cable specifications
<https://downloads.limelightvision.io/documents/systemcore_motioncore_cable_specifications.pdf>`_
for its pinout, wire, and connector requirements. Systemcore connectors use
gold contacts in the Alpha specification; do not mate them with tin contacts.

Before connecting the battery, inspect every power connection:

- Red wire goes to positive and black wire goes to negative.
- No bare copper is visible outside a connector.
- Each connector is fully seated and cannot be pulled out gently.
- The Systemcore is connected by exactly one of the power methods above.

.. warning::

   Never power the Systemcore through a regulator (such as a VRM). It
   needs battery voltage directly, and some regulators can't supply
   enough current under full load.

.. important::

   The USB-C **LINK** port carries data only and does not power the
   Systemcore. On an Alpha unit, having LINK connected when robot power is
   applied starts flash mode instead of a normal boot. For an ordinary USB
   connection, power the Alpha Systemcore first and connect LINK after it
   starts.

.. rubric:: Part 3: Confirm It's Alive

Once powered, the Systemcore hosts its own network so you can connect
to it directly, before any radio or field network is involved.

.. list-table::
   :header-rows: 1

   * - Connection
     - Default value
   * - Built-in Wi-Fi SSID
     - ``SYSTEMCORE``
   * - Built-in Wi-Fi password
     - ``PASSWORD``
   * - Wi-Fi access point IP
     - ``172.30.0.1``
   * - USB (Windows)
     - ``172.26.0.1``
   * - USB (macOS / Linux)
     - ``172.27.0.1``

.. note::

   Units on OS image 9 or earlier use ``172.28.0.1`` (USB, Windows) or
   ``172.29.0.1`` (USB, macOS/Linux) instead.

1. Connect the battery and turn robot power **On**.
2. Confirm that the **Power** LED becomes solid green. The **Status** LED
   should be off when there are no hardware faults. A solid or blinking red
   Status LED indicates a fault; read the onboard display for details before
   continuing.
3. Connect the computer to the ``SYSTEMCORE`` Wi-Fi network using password
   ``PASSWORD``, or connect it to the USB-C LINK port with a data-capable
   cable. On Alpha hardware, connect LINK only after power-up for a normal
   boot.
4. Open ``http://robot.local`` in a browser. If that name does not resolve,
   use the appropriate IP address from the table.
5. Confirm that the Systemcore web interface loads and identifies the unit.
   The onboard display also shows connection information such as IP addresses.

.. TODO: Add a paired image of the successful robot.local page and the matching
   Systemcore onboard display.

If the web interface loads, the Systemcore has power, has booted, and can
communicate with the computer. It does not yet mean that the radio, motor
controllers, or drivetrain are configured.

.. warning::

   If the Systemcore does not boot, a connector becomes hot, a breaker trips,
   or you see or smell smoke, turn robot power off and disconnect the
   battery immediately. Recheck polarity, exposed conductors, and shorts before
   applying power again.

.. note::

   These LED meanings and the custom-connector requirements come from the
   Alpha hardware specification. Check the production specification before
   applying them to hardware whose labeling or revision differs.

.. rubric:: Part 4: Wire the Rest of the Control System

Motor controllers, radio, CAN bus, and pneumatics wiring still follow
the reference guides below.

Turn robot power **Off** and disconnect the battery again before making any of
these connections.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item::

      .. rubric:: FRC
         :class: wl-frc-text

   .. grid-item::

      .. rubric:: FTC
         :class: wl-ftc-text

   .. grid-item-card:: FRC Robot Wiring Walkthrough
      :link: basic-robot-wiring
      :link-type: doc
      :class-card: sw-card-frc

      **FRC**
      ^^^
      **Wiring your first robot?**

      Complete, start-to-finish instructions for wiring a basic
      drivetrain robot. Start here and follow the steps in order.

   .. grid-item-card:: FTC Robot Wiring Walkthrough
      :link: ../../ftc/basic-ftc-robot-wiring
      :link-type: doc
      :class-card: sw-card-ftc

      **FTC Coming 2027-2028**
      ^^^
      **Wiring your first robot?**

      Complete, start-to-finish instructions for wiring a basic
      Systemcore and Motioncore drivetrain robot. Start here and
      follow the steps in order.

   .. grid-item-card:: FRC Robot Wiring Reference
      :link: intro-to-frc-robot-wiring
      :link-type: doc
      :class-card: sw-card-frc

      **FRC**
      ^^^
      **Looking up a connection?**

      Connection diagrams and component details to look up while
      wiring or troubleshooting an FRC control system.

   .. grid-item-card:: FTC Robot Wiring Reference
      :link: ../../ftc/ftc-robot-wiring-overview
      :link-type: doc
      :class-card: sw-card-ftc

      **FTC Coming 2027-2028**
      ^^^
      **Looking up a connection?**

      Connection diagrams and component details to look up while
      wiring or troubleshooting an FTC control system.

.. admonition:: Wiring Guide Compatibility

   Use **Part 2 on this page** for the current 2027 instructions for powering
   and connecting Systemcore.

   The FRC walkthrough and reference still show roboRIO-era hardware. Their
   guidance remains useful for the PDH or PDP, main breaker, motor controllers,
   CAN bus, radio, and pneumatics. Do not follow their roboRIO power or data
   connections when building a Systemcore robot.

   The FTC walkthrough and reference are placeholders for the fall 2027
   Systemcore and Motioncore release. Until those instructions are published,
   teams using the REV Control Hub or Expansion Hub should follow the
   `current FTC Robot Wiring Guide
   <https://ftc-docs.firstinspires.org/en/latest/robot_building/wiring_guide/wiring-guide.html>`_.

.. tip::

   **Not sure which PDH or PDP you have?**
   The **Power Distribution Hub (PDH)** is the REV Robotics unit
   (rectangular, 20 slots). The older
   **Power Distribution Panel (PDP)** is the Cross The Road Electronics unit
   (oval shape, 16 slots). Both are legal; wiring diagrams for each are in
   the wiring overview above.

.. container:: sw-success

   .. container:: sw-success-h

      ✓ Your robot is assembled, powered, and ready for software setup.

   Continue when every power connection passes inspection, Systemcore's Power
   LED is solid green, and ``robot.local`` opens from the computer. The radio,
   motor controllers, and drivetrain do not need to be configured yet.

.. container:: sw-nav

   :doc:`← Zero to Robot <../introduction>`

   .. container:: sw-next

      :doc:`Step 2: Set Up Your Environment → <../step-2/index>`

.. toctree::
   :maxdepth: 1
   :hidden:

   Kitbot / Starter Bot Assembly <kitbot-starterbot-assembly>
   FRC Robot Wiring Walkthrough <basic-robot-wiring>
   FTC Robot Wiring Walkthrough </docs/ftc/basic-ftc-robot-wiring>
   FRC Robot Wiring Reference <intro-to-frc-robot-wiring>
   FTC Robot Wiring Reference </docs/ftc/ftc-robot-wiring-overview>
