.. include:: <isonum.txt>

# Running Your Test Program

**By the end of this page:** you will have confirmed that an FRC drivetrain
responds correctly while tethered and through the radio, with its wheels safely
off the floor.

This page covers the FRC Driver Station path. First, create and deploy the
:doc:`Java, C++, or Python drivetrain program
</docs/zero-to-robot/step-4/creating-test-drivetrain-program-cpp-java-python>`
and complete the Step 3 communication checks.

## Before You Enable

.. warning::

   A drivetrain can move as soon as the robot is enabled. Safely support the
   robot with all drive wheels clear of the floor. Keep hands, hair, tools, and
   loose clothing away from moving parts. Have another person ready to turn
   robot power off.

Confirm all of the following:

- The Systemcore, Driver Station, and WPILib project use the same team number.
- The drivetrain example was deployed without a build or deploy error.
- The controller is connected and assigned to port 0.
- Controller axes return to neutral when released.
- Motor ports or CAN IDs in the program match the wired devices.
- One drivetrain side is inverted in software as shown by the complete example.

## Test While Tethered

Test through a direct connection before testing through the radio. This
separates program and controller problems from radio configuration problems.

1. Boot the Systemcore normally.
2. Connect the Driver Station computer directly to the Systemcore:

   - Use the USB-C LINK port with a data-capable cable. On Alpha hardware,
     connect LINK after the Systemcore boots so it does not enter flash mode.
   - Or connect directly by Ethernet.

3. Open **FIRST Driver Station**.
4. In Driver Station settings, enter the team number shown on the Systemcore
   display.
5. Open the controller/USB view. Assign the controller to port 0 and verify
   that its axes and buttons respond. Use :kbd:`F1` to rescan if a controller
   was reconnected.
6. Confirm that Driver Station shows:

   - Robot communication
   - Robot code
   - Controller input
   - A plausible robot battery voltage

If communication is missing, return to
:doc:`Step 3 <../step-3/index>`. If communication is present but robot code is
missing, inspect the deploy output and Driver Station log before enabling.

## First Enable

1. Select **Teleoperated** mode.
2. Ask everyone nearby to stand clear and announce that the robot is about to
   enable.
3. Click **Enable** in Driver Station.
4. Move the forward axis only a small amount, then release it. Confirm that
   both sides turn in the expected direction.
5. Test steering with a small input.
6. Click **Disable**, or press :kbd:`Enter`, before approaching the robot.

.. important::

   The keyboard enable shortcut is :kbd:`[` + :kbd:`]` + :kbd:`\\`, not
   :kbd:`Enter`. The :kbd:`Space` bar is **Emergency Stop**, not ordinary
   disable. An emergency-stopped robot must be rebooted before it can be
   enabled again.

If one side runs backward, disable the robot and change that side's inversion
setting in software. Do not reverse motor power leads as a substitute for
correct drivetrain configuration.

## Test Through the Radio

Only continue after tethered operation works.

1. Configure the robot and access-point VH-109 radios with matching team
   number, suffix, and security keys as described in
   :doc:`Programming Your Radio <../step-3/radio-programming>`.
2. Connect the Driver Station computer to the access-point radio by Ethernet.
3. Confirm that robot communication and robot code return in Driver Station.
4. Repeat the **First Enable** procedure with the robot safely supported.

Passing both tests confirms that the program, Systemcore, controller, and radio
path are working together. Lower the robot to the floor only after disabling
it and confirming that all drivetrain directions are correct. For the first
floor test, use a clear open area, begin with small controller inputs, and keep
another person ready to disable or power off the robot.

.. container:: sw-success

   .. container:: sw-success-h

      ✓ Your FRC drivetrain passed its supported-wheel tests.

   The robot is ready for a careful floor test in a clear area.

.. container:: sw-nav

   :doc:`← Create Your Test Drivetrain Program
   <creating-test-drivetrain-program-cpp-java-python>`

   .. container:: sw-next

      :doc:`Return to Step 4 → <index>`
