# Using Lambda Functions

Lambda functions are a way of passing code to a function for *that* function to execute when it needs it. Java allows any object that could be an interface with a single method (a so-called "functional interface") to be written instead using a lambda function to improve readability and performance.

Commands v3 uses lambdas heavily because command builders need to be given behavior. A command factory does not usually run the command immediately; it packages up the lambda so the scheduler can run it later, when the command is scheduled.

The commonly used functional interfaces in v3 are:

- ``Consumer<Coroutine>`` - a function that accepts a ``Coroutine`` input with no outputs. Used when defining command bodies with the builder API. Every occurrence of ``run(coroutine -> ... )`` is a ``Consumer<Coroutine>``.
- ``Runnable`` - a function with no inputs and no outputs. Used when setting ``whenCanceled`` and for ``runRepeatedly(() -> ... )``
- ``BooleanSupplier`` - a function with no inputs and returns a ``boolean`` value. Heavily used by :doc:`triggers` and for coroutine ``waitUntil(() -> ...)``

## Lambda Examples

Imagine you have a function that needs to have some dynamic behavior based on its input. You need to pass an object to it that it can call when it needs it. These are often referred to as *callbacks*.

```java
/**
 * Runs until a user-supplied callback tells us to stop.
 */
public void runUntil(BooleanSupplier stop) {
  int counter = 0;
  while (!stop.getAsBoolean()) {
    counter += 1;
    System.out.println("Still going at iteration " + i + "!");
  }
}
```

### 1. Object-Oriented Approach (pre-Java 8)

In a purely object-oriented programming style, anything passed to the ``stop`` would need to be an instance of a type that implements the ``BooleanSupplier`` interface. This was the case in Java before the release of Java 8 in 2013:

```java
public class RandomCondition implements BooleanSupplier {
  @Override
  public boolean getAsBoolean() {
    return Math.random() >= 0.5;
  }
}

runUntil(new RandomCondition());
```

### 2. Anonymous Classes (pre-Java 8)

However, you didn't need to write an entire class for this. Java allows for *anonymous* classes, where you define the class where you need it instead of in its own file. This approach is a little easier than the first, since it means all the logic is defined exactly where it's used instead of in a separate file:

```java
runUntil(new BooleanSupplier() {
  @Override
  public void getAsBoolean() {
    return Math.random() >= 0.5;
  }
});
```

### 3. Lambda Functions (Java 8 and later)

The anonymous class approach still has some problems, though. There's a lot of unnecessary code that buries the code we actually care about - the actual logic of ``Math.random() >= 0.5``. Everything else - ``new BooleanSupplier()``, ``public void getAsBoolean()``, even the ``@Override`` annotation - is redundant because there's only thing that could *possibly* be implemented here. Lambda functions were added to make this process simpler. The anonymous class above can be rewritten as a lambda function instead and cut out all the redundant code:

```java
runUntil(() -> {
  return Math.random() >= 0.5;
});
```

And because this function is so simple - only a single line - it can be simplified by removing the curly braces and ``return`` keyword, going from a total of 6 lines of code down to just 1:

```java
runUntil(() -> Math.random() >= 0.5);
```

## Lambda Function Structure

A lambda function, like a normal function, has three components: a list of parameters that it accepts (which may be empty), a return type (which may be ``void``), and a body to perform some work. A lambda function separates the parameter list from the body using an arrow ``->``, pointing from the *inputs* to the *outputs*; the return type doesn't need to be specified anywhere, because the Java compiler already knows what it has to return based on the signature of the function it's passed to or the type of the variable it's assigned to.

```java
(param1, param2, ..., paramN) -> {
  ... body ...
  return <result>;
}
```

There are also several special cases for lambda functions to make them more concise:

1. Lambda functions with exactly one input parameter don't need parentheses around the parameter list.
2. Parameters to lambda functions don't need to have their types specified. This is why commands v3 code can use ``run(coroutine -> ...)`` instead of having to to specify ``run((Coroutine coroutine) -> ...)`` every time.
3. Lambda functions with only one line of code can omit the curly braces and ``return`` keyword

## How commands use lambda functions

Command builders are based around providing a lambda function for the logic that the command will run. ``Command.noRequirements()`` and ``Command.requiring(...).executing()`` both accept lambda functions for the command logic. These lambda functions accept a single ``Coroutine`` object and perform whatever command logic is needed. The optional ``whenCanceled()`` builder method also accepts a lambda function, but this one doesn't have any arguments.


The ``coroutine`` parameter is only valid while the command is running. Do not store it in a field or try to call it later from another thread or callback. If a command does not need the coroutine parameter, name it ``_`` to make that clear to readers and to the compiler.
