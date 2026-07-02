# Structuring Your Project

While WPILib and the commands v3 framework are flexible and don't force code to be written in a specific way, we recommend a standard structure to make code easier to understand (both for programmers and :term:`CSA` volunteers).

1. Write a single ``Robot`` class that owns the mechanisms and driver controls.
2. Write separate classes that implement ``Mechanism`` to represent each mechanism on the robot.
3. Use OpMode classes to define OpMode-specific behaviors.
4. Any commands that require a single mechanism should be written as ``Command`` methods in that mechanism's class.
5. Any commands that require multiple mechanisms should be written as ``Command`` methods in a related helper class.

## A Single Robot Class

WPILib needs a single entry point to start your program. Use a ``Robot`` class that extends from ``OpModeRobot``. Any behavior that should always be active - regardless of OpMode - should be defined here, such as default commands or trigger bindings.

Mechanisms should be declared as ``public final`` fields in the robot class and initialized in the field declaration or in the constructor. The former makes the code a little more concise, while the latter allows for flexibility if different mechanism implementations exist.

.. remoteliteralinclude:: https://raw.githubusercontent.com/wpilibsuite/allwpilib/main/wpilibjExamples/src/main/java/org/wpilib/examples/rebuiltcmdv3/Robot.java

## Mechanism Classes

Each physical mechanism on a robot should have a corresponding class in the codebase. These are typically in the ``first.robot.mechanisms`` package.

Mechanisms are often a combination of multiple actuators, such as a slapdown intake with one actuator or set of actuators to run intake rollers and a separate actuator that extends and retracts the intake. It's usually simpler for each independent actuator to have its own ``Mechanism`` class; if they're only used in the context of a larger mechanism, they can still be separate classes, but only used by a single encompassing mechanism.

In this example of a slapdown intake, there could be three classes:

1. ``IntakeRoller``, for controlling just the rollers
2. ``IntakeWrist``, for controlling the deployment of the intake
3. ``Intake``, which combines both the rollers and the wrist

.. remoteliteralinclude:: https://raw.githubusercontent.com/wpilibsuite/allwpilib/main/wpilibjExamples/src/main/java/org/wpilib/examples/rebuiltcmdv3/mechanisms/Intake.java
.. remoteliteralinclude:: https://raw.githubusercontent.com/wpilibsuite/allwpilib/main/wpilibjExamples/src/main/java/org/wpilib/examples/rebuiltcmdv3/mechanisms/IntakeRoller.java
.. remoteliteralinclude:: https://raw.githubusercontent.com/wpilibsuite/allwpilib/main/wpilibjExamples/src/main/java/org/wpilib/examples/rebuiltcmdv3/mechanisms/IntakeWrist.java

## OpMode Classes

OpMode classes let you group mode-specific logic together in one place without cluttering the main robot class. Because the command scheduler automatically scopes everything you do in the OpMode class to that OpMode, you don't need to worry about logic specific to that OpMode leaking out and still running when modes change. Commands that are only used in a specific OpMode can be defined in that OpMode class, too.

OpMode constructors are generally all that's needed. WPILib will automatically call them when that mode is selected on the driver station, passing in the main ``Robot`` object if the constructor accepts it.

.. remoteliteralinclude:: https://raw.githubusercontent.com/wpilibsuite/allwpilib/main/wpilibjExamples/src/main/java/org/wpilib/examples/rebuiltcmdv3/opmodes/auto/SweepAuto.java

## Mechanism-level Commands



## Multi-Mechanism Commands


