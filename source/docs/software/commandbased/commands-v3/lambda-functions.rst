# Using Lambda Functions

Lambda functions are a way of passing code to a function for *that* function to execute when it needs it. Java allows any object that could be an interface with a single method (a so-called "functional interface") to be written instead using a lambda function to improve readability and performance.

Commands v3 uses lambdas heavily because command builders need to be given behavior. A command factory does not usually run the command immediately; it packages up the lambda so the scheduler can run it later, when the command is scheduled.

## How commands use lambda functions

Command builders are based around providing a lambda function for the logic that the command will run. ``Command.noRequirements()`` and ``Command.requiring(...).executing()`` both accept lambda functions for the command logic. These lambda functions accept a single ``Coroutine`` object and perform whatever command logic is needed. The optional ``whenCanceled()`` builder method also accepts a lambda function, but this one doesn't have any arguments.


The ``coroutine`` parameter is only valid while the command is running. Do not store it in a field or try to call it later from another thread or callback. If a command does not need the coroutine parameter, name it ``_`` to make that clear to readers and to the compiler.
