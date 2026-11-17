Wire Your Systemcore Drivetrain
===============================

Use this guide for a basic four-motor drivetrain with two CIM motors on each
side and one SPARK MAX controller per motor. You can use this setup on a
Kitbot or another differential-drive chassis.

Systemcore runs the robot code and sends commands over CAN. Each SPARK MAX
has its own power connection and runs one motor.

.. note::

   This guide covers beta and later units and is still being completed.
   Systemcore power, CAN, and signal-light
   connections need to be checked against the hardware you have. The missing
   details are listed below.

Coming from Zero to Robot in FRC Docs? Continue here with the assembled
chassis. This guide covers Systemcore wiring before you set up your editor
and write code in Robot to Motion.

`← Back to assembly in FRC Docs
<{{ frc_docs_url }}docs/zero-to-robot/step-1/kitbot-starterbot-assembly.html>`_

Components
----------

* An assembled differential-drive chassis with four CIM motors, two per side.
* A Systemcore controller and the power cable for its hardware revision.
* Four REV SPARK MAX motor controllers.
* A robot battery, main breaker, and power distribution device, with wire
  and circuit protection that match your components and the current rules.
* A VH-109 radio and its power and Ethernet cables.
* CAN cables, appropriate connectors, mounting hardware, labels, and strain
  relief.

Check the manufacturer instructions for wire sizes, connectors, circuit
protection, and fastener torque. Check the current rules before choosing parts.

.. grid:: 1 3 3 3
   :gutter: 3

   .. grid-item::

      .. figure:: /docs/controls-overviews/images/control-system-hardware/systemcore.png
         :alt: Limelight Systemcore controller.
         :width: 200

         Systemcore. Photo courtesy of Limelight.

   .. grid-item::

      .. figure:: /docs/controls-overviews/images/control-system-hardware/spark-max-motor-controller.png
         :alt: REV SPARK MAX motor controller.
         :width: 200

         SPARK MAX. Photo courtesy of REV Robotics.

   .. grid-item::

      .. figure:: /docs/controls-overviews/images/control-system-hardware/robot-battery.png
         :alt: Robot battery with attached battery leads.
         :width: 200

         Robot battery. Photo courtesy of AndyMark.

See the `hardware component overview in FRC Docs
<{{ frc_docs_url }}docs/controls-overviews/control-system-hardware.html>`_ for photos and descriptions
of power distribution, radios, breakers, and other components.

.. admonition:: Photo placeholder: Complete drivetrain
   :class: note

   Show the assembled four-CIM drivetrain from above, with the left and right
   sides, Systemcore, four SPARK MAX controllers, power distribution, battery,
   and radio labeled.

Plan the Connections
--------------------

Each motor controller gets power from the power distribution device:

.. code-block:: text

   Battery -> main breaker / power distribution
              |-> protected branch -> leftLeader   SPARK MAX -> left CIM motor
              |-> protected branch -> leftFollower SPARK MAX -> other left CIM
              |-> protected branch -> rightLeader  SPARK MAX -> right CIM motor
              |-> protected branch -> rightFollower SPARK MAX -> other right CIM
              |-> Systemcore supply connection [details pending]
              `-> radio supply connection [installation-specific]

This map shows where power goes. It does not show connector pins or how to
assemble the cables. Write down the power channel used by each controller.
Power channel numbers and CAN IDs are separate.

Mount the controllers where their power, motor, and CAN connections are
accessible. Keep wiring away from moving parts and provide strain relief.
See `Wiring practices in FRC Docs
<{{ frc_docs_url }}docs/hardware/hardware-basics/wiring-best-practices.html>`_.

.. admonition:: Photo placeholder: Electronics layout
   :class: note

   Show controller mounting, accessible connectors, cable routing, and strain
   relief. Include enough of the chassis to show where the electronics sit.

SPARK MAX Power and Motor Connections
-------------------------------------

Disconnect the battery before making connections. Check the labels on the
SPARK MAX before connecting wires. Both the power input and motor output
have red and black wires.

* Connect each controller's ``V+`` and ``V-`` power inputs to its protected
  power distribution circuit. Check positive and negative before connecting.
* Connect one brushed CIM motor to each controller's ``A`` and ``B`` motor
  outputs. Leave output ``C`` unused and insulated.
* Set each controller to brushed motor mode before testing.

REV documents these connections in its `SPARK MAX power and motor reference
<https://docs.revrobotics.com/brushless/spark-max/specs/power-and-motor-connections>`_.
Check that reference when identifying the leads. Reversing polarity or mixing
up power and motor connections can damage the controller.

.. admonition:: Photo placeholder: SPARK MAX power and CIM motor leads
   :class: note

   Show one controller with V+ and V- input labels and A and B motor outputs
   visible. Show the unused C lead insulated and the battery disconnected.

CAN Controller Assignments
--------------------------

Use these example assignments to match the WPILib Blocks drivetrain guide.
Label each controller with its side, motor, and CAN ID.

.. list-table:: Example drivetrain assignments
   :header-rows: 1
   :widths: 25 15 30 30

   * - Program name
     - CAN ID
     - Motor
     - Power channel
   * - ``leftLeader``
     - 1
     - Left motor 1
     - Write in your channel
   * - ``leftFollower``
     - 2
     - Left motor 2
     - Write in your channel
   * - ``rightLeader``
     - 3
     - Right motor 1
     - Write in your channel
   * - ``rightFollower``
     - 4
     - Right motor 2
     - Write in your channel

Connect all four controllers to the same Systemcore CAN bus. The Blocks
example uses bus 0 and CAN IDs 1–4. If your robot uses different IDs, update
the code to match.

The code sets one controller on each side to follow the other. Each still
needs its own power, motor, and CAN connections. Do not connect one
controller's motor output to another controller.

Use REV's `SPARK MAX control connection reference
<https://docs.revrobotics.com/brushless/spark-max/specs/control-connections>`_
to identify the CAN connector. Cable order does not set CAN IDs or follower
relationships.

.. admonition:: Photo placeholder: CAN wiring and controller labels
   :class: note

   Show the four controllers with CAN IDs 1–4 and motor-side labels. Make the
   CAN cable routing visible. Capture the Systemcore connector and termination
   once the connections have been checked for this Systemcore revision.

Systemcore Details Still Needed
-------------------------------

Power Input
~~~~~~~~~~~

Use the bridge-port Molex Micro-Fit+ connection and the supplied power cable.
FIRST confirms this power connection for both programs in its
`hardware update
<https://www.firstinspires.org/community-blog/control-system-update-first-tech-challenge-edition>`_.

The `SystemcoreTesting power instructions
<https://github.com/wpilibsuite/SystemcoreTesting#powering-on>`_
require battery voltage rather than a regulator such as
the VRM. Follow the installation instructions for your revision when selecting
the protected distribution connection; these notes do not establish its breaker
rating or connector polarity.

For the supplied Micro-Fit to XT30 adapter's pin assignments and orientation
drawing, see :doc:`/docs/software/systemcore-info/systemcore-cable-reference`.

Prepare the Power Connection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Disconnect the robot battery before installing or inspecting cables.
2. Identify the supplied Systemcore power cable and its keyed connector.
   Check its supply and ground assignments against the cable reference.
3. Identify the protected distribution circuit for Systemcore. Confirm the
   wire size, protection rating, and terminal requirements with the controller
   and distribution-device instructions before connecting it.
4. Trace supply and ground from distribution to the controller cable. Check
   for reversed polarity, damaged insulation, loose strands, and exposed contacts.
5. Secure the cable and provide strain relief. Record the distribution channel
   separately from the motor-controller power channels and CAN IDs.

The circuit-protection rating for this installation is still pending. This
sequence prepares the connection for inspection; complete that selection and
the remaining wiring checks before applying power.

Remaining Connection Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Wiring details to add
   :header-rows: 1
   :widths: 30 70

   * - Connection
     - Required information
   * - Systemcore supply
     - Protected distribution output, wire size, and fuse/breaker rating
       for the selected power cable and distribution device.
   * - CAN bus
     - Connection from the two-pin SL port to the controller chain and
       termination at the ends of the bus. See
       :doc:`/docs/software/systemcore-info/systemcore-can-wiring` for its status.
   * - Radio
     - Power connection and Ethernet port/cable assignment for the chosen
       Systemcore and VH-109 installation.
   * - Signal light
     - Systemcore connection diagram and indicator behavior for the installed
       hardware and firmware.

For more about the controller, see the `WPILib Systemcore introduction
<https://docs.wpilib.org/en/latest/docs/software/systemcore-info/systemcore-introduction.html>`_.
Use WPILib's Robot to Motion guide to update Systemcore and configure the
radio.

.. admonition:: Photo placeholder: Systemcore power connection
   :class: note

   Show the controller hardware revision, connector orientation, polarity
   markings, and power cable route to the protected distribution connection.
   Take the photo once the power connection has been checked.

.. admonition:: Photo placeholder: Radio installation
   :class: note

   Show the VH-109 mounting, labeled power connection, and Ethernet cable route
   to Systemcore. Use the same hardware configuration as the wiring reference.

.. admonition:: Photo placeholder: Signal-light connection
   :class: note

   Show the signal light mounting and its labeled Systemcore connection.
   Take the photo once the connector and wiring have been checked.

Sensor Connections
------------------

.. note::

   Systemcore Smart I/O pinouts, input behavior, signal limits, and sensor-bus
   wiring diagrams are still being completed. Use the controller and sensor
   documentation for your hardware revision before connecting a sensor.

For sensor types and mounting, see the `FRC sensor guides
<{{ frc_docs_url }}docs/hardware/sensors/sensor-overview-hardware.html>`_.
Use the :doc:`WPILib sensor APIs
</docs/software/hardware-apis/sensors/sensor-overview-software>` for code.

Systemcore Status and Signal Light
----------------------------------

.. note::

   Systemcore LED/display definitions, signal-light connections, and indicator
   patterns are still being completed for the installed hardware and firmware.

Inspect, Then Continue to Software Setup
----------------------------------------

Record power channels, CAN IDs, hardware revisions, and cable assignments.
Before applying power, follow the `physical inspection checklist in FRC Docs
<{{ frc_docs_url }}docs/hardware/hardware-basics/preemptive-troubleshooting.html>`_.
Resolve wiring and mounting problems before powered tests.

Once the hardware is ready, continue to :doc:`Robot to Motion <introduction>`.
The :doc:`Blocks drivetrain example </docs/software/blocks/first-project>`
uses the controller names and CAN IDs above. Follow it to set up the
followers, check motor direction, and test the drivetrain.

.. button-ref:: introduction
   :color: primary

   Continue to software setup in Robot to Motion →
