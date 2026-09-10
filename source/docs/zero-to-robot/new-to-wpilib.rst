New to WPILib
==============

If you already know how to write code, this page maps familiar programming
ideas to a WPILib robot. WPILib is what lets your code talk to motors, sensors,
and everything else wired into the control system.

.. tip::

   **New to programming too?** Start with :doc:`Zero to Robot <introduction>`.
   It teaches the programming concepts as you build and bring up the robot.

.. rubric:: How the Pieces Fit Together
   :class: wl-shared-text

Same building blocks whether you're on FRC or FTC.

.. grid:: 1 2 3 5
   :gutter: 3

   .. grid-item-card:: Robot Class

      The entry point for your program. Defines what runs when the robot
      is enabled, disabled, or switches modes.

   .. grid-item-card:: Subsystems

      A piece of the robot (drivetrain, arm, intake) wrapped in code
      that owns its own motors and sensors.

   .. grid-item-card:: Commands

      An action a subsystem performs, like "drive forward" or "raise the
      arm to height." You schedule commands; you don't call them directly.

   .. grid-item-card:: OpModes

      Coming from FTC, this is what you already know. A WPILib Robot
      Class fills a similar role by defining what runs in each robot mode.

   .. grid-item-card:: Hardware APIs

      The classes for motor controllers, encoders, and other devices.
      This is what actually puts a signal on the wire.

.. rubric:: Where FRC and FTC Differ
   :class: wl-shared-text

At this introductory level, the most visible differences are the Driver
Station and where motors connect. FRC uses the FRC Driver Station, with motor
controllers wired into the FRC control system. FTC uses its own Driver Station
software, and motors and servos connect through Motioncore. The programming
building blocks above apply to both programs; the
:doc:`Zero to Robot guide <introduction>` identifies the program-specific
steps.

.. tip::

   **Need to back up?** If the robot still needs to be built or wired,
   start with the :doc:`hardware overview </docs/hardware/hardware-basics/hardware-overview>`
   before writing code against hardware that isn't connected yet.

.. container:: sw-nav

   .. container:: sw-next

      :doc:`Continue to Zero to Robot → <introduction>`
