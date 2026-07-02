# Command Triggers

Triggers are the primary way to start commands in response to external events, such as a button press, a sensor value reaching a threshold, or a specific robot state. A trigger represents a true/false signal that is polled by an event loop. By default, that event loop is polled during ``Scheduler.run()``.

Triggers cache their signal when they are polled. Calling ``getAsBoolean()`` reads the most recently polled value, not necessarily the live value of the underlying button or sensor at that exact instant. This is what lets triggers reliably detect rising and falling edges within a scheduler cycle.

## Creating Triggers

A ``Trigger`` is created by providing a ``BooleanSupplier`` (a function that returns ``true`` or ``false``) or by combining existing triggers.

.. tab-set-code::

  ```java
  // A trigger for a gamepad button
  Trigger button = xboxController.a();

  // A trigger for a limit switch
  Trigger limitSwitch = new Trigger(limitSwitch::get);

  // A trigger for a complex condition by combining two triggers
  Trigger isReady = new Trigger(arm::isAtTarget).and(shooter::isAtSpeed);
  ```

## Trigger Bindings

Once you have a trigger, you can bind commands to it. There are several types of bindings that determine how the command responds to changes in the trigger's state.

### State-Based Bindings

Triggers implement the Java ``BooleanSupplier`` interface, making them compatible with any method that accepts a boolean condition, such as ``Coroutine.waitUntil``. The binding methods below schedule or cancel commands based on the trigger's cached signal and its previous cached signal.

*   ``onTrue(Command)``: Schedules the command when the trigger transitions from ``false`` to ``true`` (a *rising edge*). The command runs until it finishes or is interrupted, even if the trigger signal becomes ``false``.
*   ``onFalse(Command)``: Schedules the command when the trigger transitions from ``true`` to ``false`` (a *falling edge*). The command runs until it finishes or is interrupted, even if the trigger signal becomes ``true``.
*   ``whileTrue(Command)``: Schedules the command on a rising edge and cancels it on a falling edge. If the command stops while the trigger is still ``true``, it is **not** restarted.
*   ``whileFalse(Command)``: Schedules the command on a falling edge and cancels it on a rising edge. If the command stops while the trigger is still ``false``, it is **not** restarted.

Use ``onTrue`` and ``onFalse`` for commands that should start once and then manage their own lifetime. Use ``whileTrue`` and ``whileFalse`` for commands whose lifetime should be tied to the signal. For example, "move while the bumper is held" is a ``whileTrue`` binding, while "start an intake sequence when the bumper is pressed" is usually an ``onTrue`` binding.

### Continuous/Retry Bindings

*   ``retryWhileTrue(Command)``: Like ``whileTrue``, but if the command finishes while the trigger is still ``true``, it is immediately restarted.
*   ``retryWhileFalse(Command)``: Like ``whileFalse``, but restarts if the command finishes while the trigger is still ``false``.

Retry bindings continuously attempt to schedule their command while the signal remains in the requested state. If the command ends naturally, it will be started again. If it was interrupted by another same-priority command that requires the same mechanism, the retry binding may immediately schedule it again and interrupt the would-be interrupter. Use retry bindings when repeated attempts are intentional, not as a default replacement for ``whileTrue``.

### Toggle Bindings

*   ``toggleOnTrue(Command)``: Schedules the command on a ``false`` to ``true`` transition, and cancels it on the next ``false`` to ``true`` transition.
*   ``toggleOnFalse(Command)``: Schedules the command on a ``true`` to ``false`` transition, and cancels it on the next ``true`` to ``false`` transition.

Toggle bindings are best for operator controls where the driver explicitly switches a behavior on and off. They are usually a poor fit for safety behavior because the command's lifetime depends on remembering how many edges have occurred.

### Multi-Press Bindings

The ``multiPress(int, Time)`` binding allows commands to be bound when a trigger signal has had a minimum number of rising edges within a specific time period.

For example, ``Trigger.multiPress(2, Seconds.of(1.5))`` will go high when there have been **at least** two rising edges within the last 1.5 seconds, and will go low when there are fewer. This can be used with ``onTrue`` to respond to a double-press. The multi-press trigger remains high as long as enough presses are still inside the time window; it is not only high on the final button press.

## Combining Triggers

Triggers can be combined using standard boolean operators to create more complex conditions. These operations create new trigger objects and do not modify the originals.

*   ``Trigger.and(BooleanSupplier)``: High when **both** signals are high.
*   ``Trigger.or(BooleanSupplier)``: High when **either** signal is high.
*   ``Trigger.negate()``: High when the original signal is low.

.. tab-set-code::

  ```java
  Trigger bothButtons = buttonA.and(buttonB);
  Trigger eitherButton = buttonA.or(buttonB);
  Trigger notButton = buttonA.negate();
  ```

## Modifying Trigger Behavior

You can also modify how a trigger responds to the underlying condition:

*   ``debounce(Time duration)``: Creates a trigger that only becomes ``true`` if the original condition is ``true`` for at least the specified duration.
*   ``risingEdge()``: Creates a trigger that is only ``true`` for a single loop cycle when the original condition transitions from ``false`` to ``true``.
*   ``fallingEdge()``: Creates a trigger that is only ``true`` for a single loop cycle when the original condition transitions from ``true`` to ``false``.

Because ``risingEdge()`` and ``fallingEdge()`` are only high for one scheduler cycle, bind commands to them with ``onTrue``. A ``whileTrue`` binding on a one-cycle edge trigger will schedule the command and then cancel it on the next cycle.

## Scopes

Trigger bindings exist in *scopes*. When a scope exits, any trigger binding that was created in that scope will be removed and the commands attached to that binding will be canceled. This is a critical safety feature of the library.

1.  **Global Scope**: Bindings created in the ``Robot`` constructor or methods called by it. These are always active.
2.  **OpMode Scope**: Bindings created while a specific OpMode is running. These are automatically removed when the OpMode ends.
3.  **Command Scope**: Bindings created inside a running command. These are removed when the command finishes or is canceled.

See :doc:`scopes` for more details.

## Game Controller Triggers

The ``org.wpilib.command3.button`` package provides specialized classes for creating triggers from game controllers, such as Xbox and PS5 (DualSense) controllers. These classes provide methods that return ``Trigger`` objects for every button, d-pad direction, and trigger on the controller. Prefer these named methods over raw button numbers when possible; the resulting robot code is easier to read and easier to audit during an event.

For a full list of available controller classes and their methods, see the `org.wpilib.command3.button <https://github.wpilib.org/allwpilib/docs/beta/java/org/wpilib/command3/button/package-summary.html>`__ Javadoc.

### Advanced Controller Triggers

You can also use axis values (like the analog sticks or analog triggers) to create triggers by using the ``axisGreaterThan``, ``axisLessThan``, or ``axisMagnitudeGreaterThan`` methods, or by providing a custom ``BooleanSupplier``. Axis-based triggers usually need a threshold and sometimes a debounce so small joystick noise does not repeatedly schedule and cancel commands.

.. tab-set-code::

  ```java
  // Trigger when the left Y axis is pushed more than 50% forward
  Trigger highThrottle = new Trigger(() -> driverController.getLeftY() > 0.5);

  highThrottle.onTrue(Command.print("High Throttle!"));
  ```

.. tab-set-code::

  ```java
  import org.wpilib.framework.TimedRobot;
  import org.wpilib.command3.button.RobotModeTriggers;

  public class Robot extends TimedRobot {
    public Robot() {
      // GLOBAL SCOPE: This binding is always active
      driverController.a().onTrue(arm.up());
    }

    @Override
    public void autonomousInit() {
      // OPMODE SCOPE: This binding only exists during autonomous
      RobotModeTriggers.autonomous().onTrue(drive.followPath("AutoPath"));
    }
  }

  // COMMAND SCOPE example
  public Command sweepAndScore() {
    return Command.noRequirements(coroutine -> {
      // This binding only exists while the 'sweepAndScore' command is running
      intakeTrigger.onTrue(intake.runOnce());

      coroutine.await(drive.followPath("SweepPath"));
    }).named("Sweep and Score");
  }
  ```
