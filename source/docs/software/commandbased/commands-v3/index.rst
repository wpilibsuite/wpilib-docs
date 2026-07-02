# Commands v3 Programming

.. toctree::
   :maxdepth: 1

   creating-commands
   how-it-works
   lambda-functions
   making-commands-run
   mechanisms
   migration-guide
   scopes
   state-machines
   structuring-your-project
   telemetry
   triggers
   troubleshooting

Command-based programming is a way of writing a program where actions can be defined and configured to execute in response to some event. We call these actions "commands" and the events "triggers". Commands may run other commands to perform more complex actions; these are called "compositions" and are a powerful tool for building sophisticated behavior from simple building blocks. Just like commands outside of compositions, commands inside of compositions can still be configured to run in response to a trigger, but can also be manually scheduled when direct control is desired.

Commands v3 command logic is written as ordinary Java code. If a command needs to do something repeatedly, it writes a loop. If it needs to wait for a sensor, it waits for the sensor. If it needs to run another command, it forks or awaits that command. This makes command code read much closer to the behavior you are trying to describe.

Because multiple commands need to be able to run simultaneously, commands use a :term:`coroutine` to manage concurrency. Coroutines allow commands to say when they have reached a pause point in their work by calling ``Coroutine.yield()``. This pauses the command and lets the scheduler run another command until *it* reaches a pause point, and so on until every running command has had a chance to make progress. Most importantly, coroutines let us write command logic using standard Java with ``while`` loops, ``if`` statements, local variables, and helper methods, with the addition of ``coroutine.yield()`` in loops to allow other commands to run.

.. warning:: Calling ``coroutine.yield()`` is required to prevent commands from being greedy - if a command never yields, no other commands will be able to run and driver inputs will not be read until the command exits. WPILib will check ``while`` loops at compile-time to ensure that loops inside of command code will yield, and issue a compiler error if any greedy loops are found.

Core APIs
---------

The commands library is built around three core concepts. Most robot code will use all three:

- **Coroutines** manage concurrency and allow commands to pause and resume.
- **Commands** define the actions to be performed.
- **Mechanisms** represent robot hardware and manage resource ownership.

Coroutines
^^^^^^^^^^

Coroutines are the engine of the commands framework. They allow you to write asynchronous code that looks like synchronous code. When a command is running, it has access to a ``Coroutine`` object that can pause execution, wait for time to pass, wait for a condition to become true, or run child commands.

The most important method on the ``Coroutine`` class is ``yield()``. This method pauses the current command and allows the scheduler to run other commands. When the scheduler returns to the paused command, it will resume from where it left off.

Other useful methods on the ``Coroutine`` class include:

- ``wait(Time duration)``: Pauses the command for a specific amount of time.
- ``waitUntil(BooleanSupplier condition)``: Pauses the command until a condition is met.
- ``await(Command command)``: Starts another command and pauses until it completes.
- ``park()``: Pauses the command indefinitely until it is canceled.

Coroutines are cooperative, not preemptive. A command only gives other commands time to run when it calls a yielding method such as ``yield()``, ``wait()``, ``waitUntil()``, ``await()``, or ``park()``. A long calculation, blocking I/O operation, or infinite loop without a yield will stall the scheduler just as surely as it would stall any other periodic robot code.

Commands
^^^^^^^^

A command is a named piece of robot behavior that can be scheduled now or configured to run later in response to a trigger. Most commands control one or more mechanisms, but a command may also require no hardware at all. For example, resetting odometry, setting a flag, printing a diagnostic message, or coordinating other commands can all be useful no-requirement commands.

All commands have three required attributes:

1. **Requirements**. Commands must declare what mechanisms they control in order to avoid conflicting hardware requests.
2. **Logic**. Commands must *do* something.
3. **Name**. Names appear in telemetry and are crucial for debugging.

The recommended way to create commands is with the staged builders on ``Mechanism`` and ``Command``. The builders force each command to declare its requirements, provide logic, and end with a name, which catches incomplete command definitions at compile time instead of leaving unnamed or requirement-free commands hidden in a robot program.

Mechanisms
^^^^^^^^^^

A mechanism is a piece of robot hardware that can only be used by one command at a time. Examples include a drivetrain, an arm, an intake, an LED strip, or a vision processor whose active pipeline should not be changed by two commands at once. Mechanism classes are responsible for owning their hardware objects and providing command factory methods for the actions that are safe to perform on that hardware.

.. note:: Because the Java programming language does not have a concept of coroutines, the ``Coroutine`` class used in the commands library is a custom type created specifically for the library. It can only be used with commands and the command scheduler; it is *not* general-purpose.

Commands prevent conflicting hardware requests from being made by using a requirements system. Every command requires some number of mechanisms, and only one running command may require a particular mechanism at a time. For example, if a running command requires an ``Arm`` mechanism, then no other commands may use the arm at the same time. If another command starts that needs the arm, then the existing command will be canceled to allow the new command to run.

We recommend users define commands using the builders provided by the ``Command`` and ``Mechanism`` classes. The builders keep command code dense, which typically helps readability, and allow user code to hide direct hardware access from other classes, which prevents another class from bypassing requirements and sending unsafe actuator commands directly. Users who prefer object-oriented programming may implement the ``Command`` interface directly, but such class-based commands need to handle requirements, names, priorities, and cancellation behavior with care.

.. tab-set-code::

  ```java
  public class Arm implements Mechanism {
    // All hardware is private.
    // Anything that wants to move the arm should be done through commands.
    private final MotorController motor = ...;

    /**
     * Creates a command that moves the arm up.
     */
    public Command up() {
      // .run() will automatically require the arm mechanism
      return run(coroutine -> {
        // ... logic to move the arm up to a predetermined angle ...
      }).named("Arm Up");
    }
  }
  ```
