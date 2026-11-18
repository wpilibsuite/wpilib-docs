# Robot Connection Problems

This article covers problems connecting the Driver Station computer to the robot.

## I Can't Connect to My Robot

If the Driver Station can't communicate with your robot, work along the chain of connections from the Driver Station to the robot code until you find where it breaks.

.. important:: If this happens on the field, tell the :term:`FTA` immediately. In the pits, a :term:`CSA` can help you troubleshoot.

### Give the Robot Time to Start

After the robot is powered on, the radio and Systemcore both need time to start. Wait until the radio's status lights show that it has finished booting before troubleshooting. See :ref:`docs/hardware/hardware-basics/status-lights-ref:Vivid-Hosting VH-109 Radio` for what the radio's lights mean.

### Check the Driver Station Status Indicators

The :ref:`Status Pane <docs/software/firstdriverstation/first-driver-station-introduction:Status Pane>` of the FIRST Driver Station shows how far along the chain communication is working. Check the indicators in this order:

1. **DS**: If this indicator is not lit, the team number is not set. Enter your team number on the Settings tab as described in :ref:`docs/software/firstdriverstation/first-driver-station-introduction:Setting Up the Driver Station`.
2. **Radio Ping**: If the Driver Station can't reach the robot radio, the problem is between your computer and the radio. Check the cable or wireless connection from your computer, and see `Check Your Computer's Network Settings`_.
3. **Robot Ping**: If the Driver Station can reach the radio but not the robot, the problem is between the radio and Systemcore. Check that Systemcore is powered on and that the Ethernet cable between Systemcore and the radio is connected at both ends.
4. **Connection Status**: If the Driver Station can ping the robot but is not communicating with it, software on your computer may be blocking the connection. Check your :doc:`firewall configuration </docs/networking/networking-introduction/windows-firewall-configuration>`.
5. **Robot Code**: If the Driver Station is communicating with the robot but there is no robot code, see :ref:`docs/software/troubleshooting/code-problems:My Driver Station Says No Robot Code`.

When the Driver Station is not communicating with the robot, it also writes a Ping Result message to the Logs tab each time the status of a device changes. See :ref:`docs/software/firstdriverstation/first-driver-station-errors-warnings:Ping Status` for how to read these messages.

### Check the Physical Connections

Many connection problems are caused by cables and power.

- Make sure each Ethernet cable is fully seated at both ends. Look at the link lights next to each Ethernet port, where present, to see whether a link is detected.
- Try a different Ethernet cable, and if possible a different port on the radio.
- If your computer uses a USB Ethernet adapter, try a different adapter or USB port. See :ref:`docs/software/firstdriverstation/first-driver-station-best-practices:Recommended USB Ethernet adapters`.
- Check that the radio's power light is on and that its power wiring is secure. If the radio loses power, even briefly, it has to boot again, and the robot is unreachable until it does. See :ref:`docs/zero-to-robot/step-1/basic-robot-wiring:Radio Power` and :doc:`/docs/hardware/hardware-basics/wiring-best-practices`.

### Check Your Computer's Network Settings

- Make sure the network adapter you are using to connect to the robot is set to obtain an IP address automatically (:term:`DHCP`). Use ``ipconfig`` to confirm that it has an address on the robot network, as described in :doc:`/docs/software/troubleshooting/gathering-information`.
- Disable other network adapters, such as Wi-Fi when you are connected by Ethernet. See :ref:`docs/networking/networking-introduction/systemcore-network-troubleshooting:Disabling Network Adapters`.
- Disable the firewall or allow the robot programs through it. See :doc:`/docs/networking/networking-introduction/windows-firewall-configuration`.
- Turn off any proxy or VPN software.

For step-by-step tests using ``ping``, see :doc:`/docs/networking/networking-introduction/systemcore-network-troubleshooting`.

## My Dashboard Doesn't Show Any Data

If the Driver Station is connected to the robot but your dashboard is not, see :doc:`/docs/software/dashboards/troubleshooting-dashboard-connectivity`.
