# Installing the FIRST Driver Station

This guide will walk you though installing the FIRST Driver Station on your computer.

## Downloading Install Files

Navigate to the [First Drive Station Releases Page](https://github.com/wpilibsuite/FirstDriverStation-Public/releases/latest). On macOS platforms download the correct ``.pkg`` file and on Windows platforms download the correct ``.exe`` file for your device. For Linux devices, only the archive files are provided.

## Per Platform Setup

### Windows

On Windows, the app has everything configured by default. Just run the installer, and then run the application.

### macOS

There are 3 permissions that macOS requires. It requires Input Monitoring, Local Network access, and data access from other apps. You will get popups for these, and they must be accepted in order to work. The first time you start up the app, these prompts will cause the launch to fail, and you'll need to accept the Input Monitoring prompt, and then restart the app. Then you'll be able to accept the Local Network permission.

If Local Network access is declined, the app will still seem to function normally, as Apple does not provide a way to detect if the permission has been granted.

macOS will also prompt with "FirstDriverStation" would like to access data from other apps. This permission is required for launching dashboards and for log file writing. You should click Allow when this prompt appears.

If you decline any of these, you can fix the settings in the ``Privacy & Security`` tab of System Settings.

If Local Network access still does not work after re-enabling it there, see :ref:`macOS Permissions<docs/zero-to-robot/step-2/first-driver-station:macOs Permissions>` for a terminal-based workaround.

### Linux

The following packages must be installed in order for linux to work:

.. todo:: update when the FirstDriverStation docs update

Additionally, the app needs to be a part of the input group in order to have input access. That can be done with the following commands.

```text
sudo chgrp input FirstDriverStation
sudo chmod g+s FirstDriverStation
```

Finally, for proper controller access, the current user needs access to hidraw. To do that, create a ``/etc/udev/rules.d/72-hidraw.rules`` containing

```text
# Grant access to all hidraw devices for the active user
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0660", TAG+="uaccess"
```

Then reload udev rules:

```text
sudo udevadm control --reload-rules && sudo udevadm trigger
```

## macOs Permissions

masOs requires both Input Monitoring and Local Network access for the Driver Station to function correctly. If you decline one of these prompt, first try re-enabling access in System Settings->Privacy & Security. If the Driver Station still cannot access the local network, you can add macOS local network exceptions from Terminal for both Ethernet and Wi-Fi. The following commands allow access to any ``10.x.x.x`` address and any ``172.16.x.x`` through ``172.31.x.x`` address:

```text
sudo defaults write com.apple.network.local-network AllowedEthernetLocalNetworkAddresses -array "10.0.0.0/8"
sudo defaults write com.apple.network.local-network AllowedEthernetLocalNetworkAddresses -array-add "172.16.0.0/12"
sudo defaults write com.apple.network.local-network AllowedWiFiLocalNetworkAddresses -array "10.0.0.0/8"
sudo defaults write com.apple.network.local-network AllowedWiFiLocalNetworkAddresses -array-add "172.16.0.0/12"
```

After running these commands, reboot macOS before starting the Driver Station again.

.. warning:: These settings allow any app on the Mac to access local networks in those ranges without prompting. If you only need access to one robot network, a narrower CIDR range is more restrictive.

.. note:: For more information, see Apple's documentation on [understanding local network privacy](https://developer.apple.com/documentation/technotes/tn3179-understanding-local-network-privacy#macOS-considerations)
