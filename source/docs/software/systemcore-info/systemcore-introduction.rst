# Systemcore Introduction

.. image:: /docs/controls-overviews/images/control-system-hardware/systemcore.png
  :width: 500

The Limelight Systemcore is designed specifically with FIRST in mind. The Systemcore is powered by a Raspberry Pi Compute Module 5 (CM5), and uses a Raspberry Pi RP2350 for reconfigurable I/O.

The Systemcore is a reconfigurable robotics controller that includes built-in ports for Controller Area Network (CAN), Inter-Integrated Circuits (I2C), USB, Ethernet, and reconfigurable I/O for Pulse Width Modulation (PWM), Digital I/O, and Analog Input to quickly connect the common sensors and actuators used in robotics. The controller features LEDs, a display, and an onboard IMU. It has an onboard quad-core ARM real-time Cortex‑A76 processor.

This documentation covers beta and later Systemcore units. See :doc:`systemcore-cable-reference` for cable pin assignments and :doc:`/docs/zero-to-robot/systemcore-wiring` for the drivetrain wiring guide.

FIRST's `December 8, 2025 hardware update
<https://www.firstinspires.org/community-blog/control-system-update-first-tech-challenge-edition>`_ confirms bridge-port Micro-Fit+ power, two-pin Molex SL CAN connectors,
a configuration button, and digital-mode I/O pull-ups for the updated hardware
used by both programs.

.. note::

   For alpha-unit information, see the `SystemcoreTesting repository
   <https://github.com/wpilibsuite/SystemcoreTesting>`_.
