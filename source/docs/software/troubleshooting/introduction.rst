# Introduction to Troubleshooting

*Troubleshooting* is the skill of finding the cause of a problem and using that cause to work toward a fix.

## Problems Will Happen

Every robot has problems. They can be frustrating, but fixing them is something every team goes through each season.

This section helps teams identify and fix common robot problems that have control system causes. It is not a list of every possible problem. Instead, it gives general guidance and specific examples for the most common pain points.

## Symptom vs. Root Cause

When troubleshooting, separate the *symptom* from the *root cause*.

The *symptom* is the incorrect behavior you actually observe. For example, a robot that can only turn in place and cannot drive straight has a symptom.

The *root cause* is the incorrect software, electrical connection, or mechanical fault that actually causes the symptom.

Effective troubleshooting works backward from the observed symptom to the root cause. Ideally the root cause gets fixed, and the symptom goes away as a result.

Sometimes time pressure makes a team "patch over" a symptom without finding or fixing the root cause. Be cautious here, as patches are prone to break or cause more problems later.

## Work Methodically

Effective troubleshooting requires working methodically.

### Use the Scientific Method

The core of every troubleshooting strategy is the scientific method:

1. Observe what is happening.
2. Propose a hypothesis.
3. Design and run a test of that hypothesis.
4. Observe and interpret the results.
5. Repeat.

For most robot problems the hypothesis will be small. A valid hypothesis could be "If I invert this motor in my code, it will stop running backward." The test is to make the change, deploy the code, and try to reproduce the problem. If the motor now runs the correct direction, the hypothesis was likely correct. If the problem remains, the hypothesis was not entirely correct, and you should repeat the process with a new hypothesis.

### Change One Thing at a Time

When interpreting the results of a test, make sure the test changed only one thing. Changing only one thing is what lets you connect the result to a single root cause.

If you change many things and the problem goes away, you will not know which change actually fixed it. It may be tempting to change many things in the hope that one of them works, but this usually leaves many unnecessary changes behind.

If a change does not affect the symptom, undo it before trying the next idea. Otherwise unrelated changes pile up and can cause new problems.

### Keep a Written Record

Write down each step you take, why you took it, and what you observed. A written record keeps you from repeating tests, helps someone else pick up where you left off, and makes it much easier to ask for help. It is also useful the next time the same symptom appears.

### Start With the Most Likely Causes

A naive approach assumes *anything* could be the root cause and checks every possibility one by one. On a large and complex system like a robot there are too many possibilities to test them all.

Instead, start by assuming which root causes are *most likely* and test those first. As you gain experience, you will develop a better intuition for where to look.

Remember that these are *assumptions*. They are educated guesses about where the problem probably is not, not proof that it does not exist there. Be ready to go back and revisit them.

### Single vs. Multiple Points of Failure

Start by assuming that a *single point of failure* is causing the symptom. For simple, well designed systems this is usually true.

As systems grow larger and more complex, multiple failures become more likely. Treat this as a secondary assumption, but do not ignore the possibility that a symptom has more than one cause.

## Be Egoless

Emotions can run high while troubleshooting, especially when it feels like someone is being blamed. People can become defensive when their part of the robot is called into question.

Remember that everyone is on the same team, working toward the same goal. Choose words that describe and judge ideas, not people. Also try not to let your own assumptions keep you from considering faults in the parts of the robot you are responsible for.

## Practice

Troubleshooting is a learned skill. There are few facts to memorize, and seeing failures and their root causes again and again is the best way to improve.

Experienced mentors or students can often look at a problem and quickly name the root cause. This ability is not magic; it is learned. Good troubleshooters still follow the same process described here, but they have seen more problems and can recognize patterns and rule out unlikely causes faster.

Spend time practicing troubleshooting, and don't worry if it takes you longer than others at first.
