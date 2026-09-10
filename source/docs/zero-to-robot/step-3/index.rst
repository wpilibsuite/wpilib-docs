# Step 3: Configure Your Control System

.. container:: sw-step-badge

   .. container:: sw-step-n

      03

   .. container::

      .. container:: sw-step-info-title

         Configure Your Control System

      .. container:: sw-step-info-sub

         Step 3 of 4

**By the end of this step:** Systemcore will run the current season image, the
robot and Driver Station will use the same team number, and the computer will
communicate with the robot through the intended network path.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Robot Ready
      :class-card: sw-card-shared

      - Step 1 is complete and Systemcore powers on normally
      - Your computer opens ``robot.local`` over Systemcore Wi-Fi or USB

   .. grid-item-card:: Computer and Team Ready
      :class-card: sw-card-shared

      - Step 2 is complete and your program's driver software opens
      - You know your team number
      - FRC teams have an Ethernet cable available for the radio

Before you can deploy code, the Systemcore must be configured with the
current season's software and the radio must be programmed for your
team number.

.. warning::

   **Re-configure every season.**
   The Systemcore image is season-specific. A robot that worked last year will
   not accept code deploys until the Systemcore is updated with the current
   year's image.

.. rubric:: Part 1: Image the Systemcore

For a Systemcore that boots normally and runs OS version 11 or later, no
specialized imaging software is required. Routine updates run through its web
interface at ``robot.local``.

1. Download the current season's ``.llupdate`` file from the
   `Systemcore releases page <https://github.com/LimelightVision/systemcore-os-public/releases/latest>`_.
   Make sure to grab the alpha or beta update that matches your unit.
2. Boot the Systemcore normally and connect over Wi-Fi or USB. For an Alpha
   unit, connect USB-C LINK after power-up to avoid entering flash mode.
3. Open a browser and navigate to ``robot.local``.
4. Click the settings (gear) icon and open the configure/update section.
5. Under **OS Update**, click **Select File**, choose the ``.llupdate``
   file you downloaded, then click **Flash Update**. This takes several
   minutes.

.. TODO: Add a screenshot of the Systemcore OS Update controls with Select File
   and Flash Update labeled.

.. note::

   **USB connection:** a success message appears once the update finishes.

   **Wi-Fi connection:** the Systemcore reboots as part of the update.
   Manually reconnect and refresh the page to see the completion status.

After the reboot, reopen ``robot.local`` and confirm the installed OS version.
In the configuration tab, set the Systemcore team number, then confirm that the
onboard display shows the new value. Enter the same team number in the Driver
Station settings.

.. important::

   Units running an OS version older than 11, units that do not boot normally,
   and releases that require a full image use the Limelight Hardware Manager
   recovery procedure in the full guide below. Recovery images and routine
   ``.llupdate`` files are not interchangeable.

.. card:: Full Systemcore imaging guide
   :link: imaging-your-systemcore
   :link-type: doc
   :class-card: sw-card-shared

   Complete reference, including OS version prerequisites and the
   Limelight Hardware Manager recovery procedure for older units.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Using a roboRIO?
      :link: https://docs.wpilib.org/en/stable/index.html
      :link-type: url
      :class-card: sw-card-frc

      **FRC Legacy**
      ^^^
      Teams still running a roboRIO should refer to the
      2026 WPILib docs for imaging instructions.

   .. grid-item-card:: FTC Legacy (REV)?
      :link: https://ftc-docs.firstinspires.org/en/latest/hardware_and_software_configuration/configuring/index.html
      :link-type: url
      :class-card: sw-card-ftc

      **FTC Legacy**
      ^^^
      Teams on REV Control Hub / Expansion Hub should refer to the
      official FTC hardware configuration guide instead. This page
      covers Systemcore only.

.. rubric:: Part 2: Configure the Radio

The steps below are FRC-specific. FTC teams still configure their radio,
it's just built into the Systemcore itself rather than a separate device.
Systemcore-specific radio configuration steps for FTC are still being
written; see :doc:`Step 1: Confirm It's Alive <../step-1/index>` in the
meantime for the built-in connection details.

FRC teams use one of two radios: the current Vivid VH-109, or a legacy
OpenMesh OM5P.

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Vivid VH-109
      :class-card: sw-card-frc

      **FRC: Current Standard**
      ^^^
      Follow the steps below to configure this radio.

   .. grid-item-card:: Legacy OpenMesh Radios
      :link: openmesh
      :link-type: doc
      :class-card: sw-card-frc

      **FRC: Legacy Reference**
      ^^^
      Hardware specs, indicator LED meanings, and troubleshooting for
      teams still running OM5P radios.

The Vivid VH109 radio must be programmed with your team number and the
correct firmware before the robot can communicate wirelessly.

1. Connect the radio directly to your computer with an Ethernet cable
   in the :guilabel:`DS` port, and make sure it's powered (Weidmuller
   connectors or PoE).
2. Open a browser and navigate to ``http://radio.local/``.
3. Select :guilabel:`Robot Radio Mode`.
4. Enter your team number and, if desired, a suffix to identify your
   network.
5. Enter the 6 GHz and 2.4 GHz WPA/SAE keys. Teams will use these to
   connect to the robot's network.
6. Repeat the same steps on a second radio in :guilabel:`Access Point
   Mode`, using the exact same team number, suffix, and keys, if you
   have one for testing at home.

.. TODO: Add a screenshot of the VH-109 Robot Radio Mode page with team number,
   suffix, and WPA/SAE fields labeled.

.. tip::

   **Only have one radio?** You don't need an access point radio to test
   at home. See the alternative setups in the full radio guide below.

.. card:: Full Radio Programming Guide
   :link: radio-programming
   :link-type: doc
   :class-card: sw-card-frc

   Firmware updates, alternative one-radio setups, and troubleshooting
   for teams that can't reach the configuration page.

.. rubric:: Part 3: Verify Configuration

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Systemcore
      :class-card: sw-card-shared

      - Web interface and display show the expected OS version
      - Display and Driver Station show the same team number
      - Power LED is solid green and Status LED is off

   .. grid-item-card:: Network and Driver Station
      :class-card: sw-card-shared

      - Radio powers on and its configured SSID appears
      - Laptop connects through the intended USB or radio path
      - Driver Station shows robot communication in green

.. TODO: Add a screenshot of the Driver Station with the communication
   indicator highlighted in green.

The robot-code indicator may remain off until the first program is deployed in
Step 4. That does not mean Step 3 failed.

.. container:: sw-success

   .. container:: sw-success-h

      ✓ Your control system is configured.

   Continue when the team numbers match, the expected radio network appears,
   and the Driver Station communication indicator is green. The robot-code
   indicator can remain off until you deploy in Step 4.

.. container:: sw-nav

   :doc:`← Step 2: Set Up Your Environment <../step-2/index>`

   .. container:: sw-next

      :doc:`Step 4: Write and Drive → <../step-4/index>`

.. toctree::
   :maxdepth: 1
   :hidden:

   imaging-your-systemcore
   radio-programming
   openmesh
