# Robot Code Problems

This article covers problems building and running robot code.

## My Build Says gradlew Is Not Recognized

The error ``gradlew is not recognized as an internal or external command`` usually means VS Code has the wrong folder open, or the project is missing files that are needed to build it. See :ref:`docs/software/basic-programming/reading-stacktraces:gradlew is not recognized...` for how to tell which one it is and how to fix it.

## My Driver Station Says No Robot Code

If the Driver Station is communicating with the robot but the Robot Code indicator is not lit, your robot program is not running.

- If you haven't deployed code since the robot was imaged or since you created the project, :doc:`deploy your code </docs/software/vscode-overview/deploying-robot-code>`.
- If you have deployed code, it may be crashing when it starts. Look for errors and stack traces in the Driver Station Logs tab, and see :doc:`/docs/software/basic-programming/reading-stacktraces` for help reading them.

## My Robot Responds Slowly and I See Loop Overrun Warnings

A *loop overrun* happens when part of the robot program takes too long to run, so the rest of the program does not get to run on time. Loop overruns become more common as a team's code grows.

### Why Loop Time Matters

Robot programs are *real-time systems*. The time between reading inputs, doing calculations, and setting outputs must be short and predictable. For example, ``TimedRobot`` calls the periodic methods every 20 ms by default.

When code runs too slowly, outputs no longer respond to inputs on time, which can cause complex and unexpected behavior. In severe cases the robot may move in a jerky or uncontrollable way and may not respond promptly to driver inputs or sensor changes.

### Reading the Warning

When a loop overruns, WPILib prints a warning to the Driver Station Logs tab, followed by how long each part of the loop took. The list will be similar to the following, although the exact formatting and order depend on your language and robot program:

```text
Loop time of 0.02s overrun
    disabledInit(): 0.000475s
    disabledPeriodic(): 0.001021s
    robotPeriodic(): 0.310620s
    TunableRegistry.update(): 0.000412s
```

The larger a number is, the more time that part of the loop took. In this example, ``robotPeriodic()`` took about 0.31 seconds, which is much longer than the 0.02 second (20 ms) loop period. That is where to look first.

Teams using the command-based framework may also see a ``CommandScheduler loop overrun`` message. It lists how long each subsystem's ``periodic()`` method and each running command's methods took.

### Finding the Slow Code

Start by reading the code that runs in the slow part of the loop. Common causes include:

- ``for`` or ``while`` loops that run many times, or that wait for something to happen.
- Calls that sleep or wait, such as ``Timer.delay()`` in Java.
- Printing many messages every loop.
- A function that calls itself, which can act like a loop.

If reading the code doesn't find the problem, measure how long the code takes to run. The ``Timer`` class's monotonic timestamp method (``getMonotonicTimestamp()`` in Java, ``GetMonotonicTimestamp()`` in C++, and ``get_monotonic_timestamp()`` in Python) returns the current time in seconds. Read the time before and after a section of code and subtract the two to find how long that section took. Doing this in several places shows which sections take the longest.

WPILib also provides a ``Tracer`` class ([Java](https://github.wpilib.org/allwpilib/docs/beta/java/wpilib.core/org/wpilib/system/Tracer.html), [C++](https://github.wpilib.org/allwpilib/docs/beta/cpp/classwpi_1_1_tracer.html), :py:class:`Python <robotpy:wpilib.Tracer>`) that does this for you, and is what WPILib uses to produce the loop overrun report. Add a named epoch after each section of code you want to measure (``addEpoch()`` in Java, ``AddEpoch()`` in C++, ``add_epoch()`` in Python), then print the epochs to see how long each section took (``printEpochs()``, ``PrintEpochs()``, or ``print_epochs()``). Clear the epochs before measuring again (``clearEpochs()``, ``ClearEpochs()``, or ``clear_epochs()``). By placing epochs carefully, you can find which parts of your code need to be made faster.
