Systemcore CAN Wiring
=====================

.. note::

   Systemcore instructions are being prepared. This page is not yet a complete
   wiring or configuration procedure.

FIRST's `hardware update
<https://www.firstinspires.org/community-blog/control-system-update-first-tech-challenge-edition>`_ identifies two-pin Molex SL CAN connectors for the updated Systemcore.

The :doc:`systemcore-cable-reference` identifies the two-pin SL CAN cable
and links its orientation drawing. A controller connection diagram,
bus layout, and termination procedure are still pending. Check the controller
hardware revision and each connected device's documentation before planning
the bus.

See :doc:`/docs/zero-to-robot/systemcore-wiring` for the drivetrain example.
For controller background, use :doc:`systemcore-introduction`.

Four-Controller Drivetrain Layout
---------------------------------

Use a single chain for the four SPARK MAX controllers in the drivetrain
example. This is a signal-routing plan; the controller-end connector and
termination details must be confirmed before applying power.

.. code-block:: text

   Systemcore bus 0
       |
       +-- leftLeader (1) -- leftFollower (2)
                                |
           rightFollower (4) -- rightLeader (3)
                  |
             far end of bus

The lines represent one continuous CAN pair, not motor power. Keep CAN High
and CAN Low continuous through the chain. The numbers are example CAN IDs;
physical cable order does not assign them. Use the same bus and IDs in code.

SPARK MAX Connections
---------------------

REV's `control connection reference
<https://docs.revrobotics.com/brushless/spark-max/specs/control-connections>`_
identifies the four-pin CAN/PWM port on the power-input side:

.. list-table:: SPARK MAX CAN/PWM connector in CAN mode
   :header-rows: 1

   * - Pin
     - Signal
   * - 1 and 3
     - CAN High
   * - 2 and 4
     - CAN Low

The matching signals connect internally, allowing the chain to pass through
each controller. Use REV's orientation drawing to identify pins. The Systemcore
two-pin SL cable and SPARK MAX four-pin JST-PH connector are different;
use a compatible cable assembly that preserves High and Low.

Termination Check
-----------------

A CAN chain needs termination at both ends. REV's
`SPARK-only network example
<https://docs.revrobotics.com/rev-hardware-client/ion/telemetry/running-multiple-spark-motor-controllers>`_
uses 120 ohm resistors at each end. Adding Systemcore requires checking what
termination the installed controller provides before choosing external resistors.

Before completing this layout, establish the controller-end termination and
the far-end termination. Record any switchable termination in other connected
devices. Adding a power distribution device to CAN changes the layout; its
power connection alone does not put it on this bus.

The beta-and-later controller termination arrangement remains to be verified.
Do not treat the cable's characteristic impedance as an installed resistor.
