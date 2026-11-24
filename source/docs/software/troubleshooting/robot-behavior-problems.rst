# Robot Behavior Problems

This article covers problems where the robot is connected but does not behave as expected, especially problems seen on the field.

.. important:: Don't rule anything out too early. It never hurts to double check that something is working properly.

## My Robot Stutters or Cuts Out When It Drives Hard

If your robot moves in jerky motions, or its motors briefly stop while it accelerates, pushes, or runs many mechanisms at once, it is often a sign of a *brownout*. A brownout happens when the battery voltage drops so low that the control system disables outputs to protect itself.

To confirm a brownout:

- Look at the status string in the :ref:`Status Pane <docs/software/firstdriverstation/first-driver-station-introduction:Status Pane>` of the FIRST Driver Station. It shows "Voltage Brownout" when a brownout occurs.
- Look at the battery voltage on the :ref:`Graph Tab <docs/software/firstdriverstation/first-driver-station-introduction:Graph Tab>` of the Driver Station.
- After a match, review the battery voltage in the Driver Station log. See :doc:`/docs/software/firstdriverstation/first-driver-station-log-viewer`.

Once you know when the brownout occurred, look for events that happened at the same time, and ask:

- Did you start the match with a battery that was low or in poor condition? See :doc:`/docs/hardware/hardware-basics/robot-battery` for how to care for and test batteries.
- Are the battery, main breaker, and power distribution connections tight? A loose connection can cause voltage drops that look like a brownout.
- Is the robot drawing too much current? Many motor controllers support current limits; see the manufacturer's documentation. :ref:`docs/software/systemcore-info/roborio-brownouts:Avoiding Brownout - Proactive Current Draw Planning` describes how to budget current draw across your mechanisms.
- Can you reproduce the problem in the pits? Running the same motion with the robot on blocks or on the practice field helps confirm the cause.

If the robot stops completely and the Driver Station loses communication, the radio or Systemcore may have lost power. See :doc:`/docs/software/troubleshooting/connection-problems`.

## My Joystick Inputs Seem to Drop Out

If you press buttons or move an axis and the robot doesn't respond, or responds late, there are several possible causes. First, try to reproduce the problem at home or in the pits. This step is important, and you should not assume the answer.

### I Can Reproduce It Off the Field

If the problem happens off the field too, the field network is not the cause. Check these areas:

- **Controllers and cables**: A worn USB cable, controller, or hub can cause dropped inputs. Check the Gamepad tab of the Driver Station to see whether the controller stays detected, and look for :ref:`Joystick Unplugged <docs/software/firstdriverstation/first-driver-station-errors-warnings:Joystick Unplugged>` warnings in the Logs tab. If your controllers change order, see :ref:`docs/software/firstdriverstation/first-driver-station-introduction:Re-Arranging and Locking Devices`.
- **The Driver Station computer**: If the computer is running slowly, high CPU or disk usage can delay the inputs the Driver Station sends. Close other programs or restart the computer. The Graph tab shows CPU usage, and :doc:`/docs/software/firstdriverstation/first-driver-station-best-practices` describes how to set up a reliable Driver Station computer.
- **Robot code**: Code that runs for a long time, such as long ``for`` or ``while`` loops or calls that wait or sleep, delays everything else in the robot program, including reading joystick inputs. See :ref:`docs/software/troubleshooting/code-problems:My Robot Responds Slowly and I See Loop Overrun Warnings`.

### It Only Happens on the Field

If you can't reproduce the problem off the field, it is more likely a network problem.

- Make sure your Driver Station computer's network settings match :ref:`docs/networking/networking-introduction/ip-configurations:On the Field DHCP Configuration`, or that your static configuration matches :ref:`docs/networking/networking-introduction/ip-configurations:Static Configuration`.
- Check how much bandwidth your robot uses, especially from cameras. See :doc:`/docs/networking/networking-introduction/measuring-bandwidth-usage`.
- Look for lost packets and high ping on the Driver Station Graph tab, or in the Driver Station log after the match.
- Talk to the :term:`FTA`, who can see field network information that you can't.
