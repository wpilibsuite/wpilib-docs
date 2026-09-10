# Installing the FIRST Driver Station

The new FIRST Driver Station is distributed from the
`FirstDriverStation-Public releases page
<https://github.com/wpilibsuite/FirstDriverStation-Public/releases/latest>`_.

.. warning::

   Pre-season alpha releases may require a specific Systemcore OS version and
   are not compatible with the roboRIO or the current FTC SDK. Check the
   release notes before installing an alpha build. Production Driver Station
   releases for 2027 and later support the official FIRST Field Management
   System (FMS).

## Before You Download

- Read the release notes and confirm that the Driver Station and Systemcore
  OS versions are compatible.
- Download only from the official WPILib GitHub organization.
- On Windows, use an Intel or AMD 64-bit computer. Windows on Arm is not
  supported.

## Install

.. tab-set::

   .. tab-item:: Windows

      1. Download the ``.exe`` installer from the latest release.
      2. Run the installer and follow its prompts.
      3. Launch **FIRST Driver Station** from the Start menu.

   .. tab-item:: macOS

      1. Download and run the ``.pkg`` installer.
      2. Launch **FIRST Driver Station**.
      3. Allow **Input Monitoring**, **Local Network**, and access to data
         from other apps when macOS asks. The first launch may stop after the
         Input Monitoring prompt; launch the application again after granting
         permission.

      If a permission was declined, enable it under **System Settings →
      Privacy & Security**, then restart the Driver Station.

   .. tab-item:: Linux

      Linux releases are currently archives rather than installers and require
      additional controller-access configuration. Follow the **Per Platform
      Setup** section in the
      `official repository README
      <https://github.com/wpilibsuite/FirstDriverStation-Public#per-platform-setup>`_
      for the release you downloaded.

## Verify the Installation

1. Open the Driver Station. It should start without an error dialog.
2. Open **Settings** and enter your team number.
3. Connect a gamepad, then confirm that it appears and its controls respond in
   the USB/controller view.
4. With no robot connected, a communication warning is expected.

Continue to :doc:`Step 3: Configure Your Control System <../step-3/index>`.
