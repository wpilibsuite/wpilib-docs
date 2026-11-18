# Gathering Debug Information

Gathering data is a key step in troubleshooting. Much of what a robot's control system does is *hidden* from view and needs special tools to observe. The following tools are not a complete list, but every robot programmer should be familiar with them.

## FIRST Driver Station

The FIRST Driver Station is the first place to check when the robot does not behave as expected.

- The :ref:`Status Pane <docs/software/firstdriverstation/first-driver-station-introduction:Status Pane>` is always visible. Its indicators show whether the Driver Station can reach the robot radio, the robot, and the robot code, and its status string shows conditions such as "No Robot Communication", "No Robot Code", and "Voltage Brownout".
- The :ref:`Logs Tab <docs/software/firstdriverstation/first-driver-station-introduction:Logs Tab>` shows messages from the Driver Station, WPILib, your robot code, and Systemcore. The :doc:`/docs/software/firstdriverstation/first-driver-station-errors-warnings` article explains some of the messages produced by the Driver Station.
- The :ref:`Graph Tab <docs/software/firstdriverstation/first-driver-station-introduction:Graph Tab>` plots battery voltage, lost packets, ping, and CPU usage over time. The :doc:`/docs/software/firstdriverstation/first-driver-station-debug-graph` adds timing information for the Driver Station's own loops.
- The :ref:`Reporting Tab <docs/software/firstdriverstation/first-driver-station-introduction:Reporting Tab>` shows software versions and information about CAN devices.

The Driver Station also records log files that you can review after a match using AdvantageScope. See :doc:`/docs/software/firstdriverstation/first-driver-station-log-viewer` for details. Reviewing the log is often the best way to understand a problem that happened on the field, when there was no time to look at the Driver Station during the match.

## Robot Console Output

Your robot program can print messages, and WPILib and vendor libraries print warnings and errors. These messages, including stack traces from crashes, appear in the Driver Station Logs tab. See :doc:`/docs/software/vscode-overview/viewing-console-output` for other ways to view them, and :doc:`/docs/software/basic-programming/reading-stacktraces` for help reading the errors you find.

## Telemetry and Data Logs

Recording values from your robot code makes it much easier to see what the robot was doing when a problem occurred. Dashboards such as AdvantageScope and Elastic can display values from the robot while it runs, and data logs can be reviewed afterward. See :doc:`/docs/software/telemetry/index` for more information.

## Command Line Utilities

Your computer has command line tools that help troubleshoot network problems. On Windows, open a command prompt by clicking :guilabel:`Start`, typing ``cmd``, and pressing :kbd:`Enter`. Type the commands below into the command prompt.

The examples below use team 1234, so the robot network addresses start with ``10.12.34``. See :ref:`docs/networking/networking-introduction/ip-configurations:TE.AM IP Address Notation` to find the addresses for your team.

### Using ``ping``

``ping`` checks basic network communication between your computer and another device. It confirms that the physical connection (wired or wireless) and a small part of the network software are working.

Type ``ping``, a space, and the address to check, then press :kbd:`Enter`. For example, to check Systemcore at ``10.12.34.2``:

```text
C:\Users\YOUR_USER>ping 10.12.34.2

Pinging 10.12.34.2 with 32 bytes of data:
Reply from 10.12.34.2: bytes=32 time=3ms TTL=64
Reply from 10.12.34.2: bytes=32 time=3ms TTL=64
Reply from 10.12.34.2: bytes=32 time=3ms TTL=64
Reply from 10.12.34.2: bytes=32 time=3ms TTL=64

Ping statistics for 10.12.34.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 3ms, Maximum = 3ms, Average = 3ms
```

This shows four test messages being sent, and the device at ``10.12.34.2`` replying to each one within three milliseconds.

- If none of the pings get a reply, something is preventing all communication. A cable may be unplugged, the device may be off, or the device may not have the expected address.
- If only some pings get a reply, something is interfering with communication. A cable may be loose, or the wireless network may be congested or experiencing interference.

You can also ping a device by name. See :doc:`/docs/networking/networking-introduction/systemcore-network-troubleshooting` for how to use this to narrow down connection problems.

### Using ``ipconfig``

``ipconfig`` summarizes the configuration of your computer's network adapters. It helps confirm that your computer is actually connected to the robot network. Type ``ipconfig`` and press :kbd:`Enter`.

The following example (shortened) shows a computer whose Wi-Fi adapter is not connected:

```text
C:\Users\YOUR_USER>ipconfig

Windows IP Configuration


Wireless LAN adapter Wi-Fi:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
```

The following example (shortened) shows a computer whose Ethernet adapter has received an address from team 1234's robot radio:

```text
C:\Users\YOUR_USER>ipconfig

Windows IP Configuration


Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 10.12.34.201
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
```

If the adapter you expect to use shows ``Media disconnected``, check the cable or wireless connection. If it shows an address that does not start with ``10.TE.AM``, your computer is not getting an address from the robot network. See :doc:`/docs/networking/networking-introduction/ip-configurations` for the addresses each device should have.

## Manufacturer Tools

Many manufacturers provide their own tools for configuring and troubleshooting their hardware, such as checking firmware versions, CAN IDs, and fault codes. See the manufacturer's documentation, linked from :doc:`/docs/software/support/support-resources`, for details.
