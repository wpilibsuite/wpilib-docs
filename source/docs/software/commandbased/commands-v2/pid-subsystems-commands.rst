.. include:: <isonum.txt>

PID Control in Command-based
=================================================

.. note:: For a description of the WPILib PID control features used by these command-based wrappers, see :ref:`docs/software/advanced-controls/controllers/pidcontroller:PID Control in WPILib`.

One of the most common control algorithms used in FRC\ |reg| and FTC\ |reg| is the :term:`PID` controller. WPILib offers its own :ref:`PIDController <docs/software/advanced-controls/controllers/pidcontroller:PID Control in WPILib>` class ([Java](https://github.wpilib.org/allwpilib/docs/beta/java/edu/wpi/first/math/controller/PIDController.html), [C++](https://github.wpilib.org/allwpilib/docs/beta/cpp/classfrc_1_1_p_i_d_controller.html), :external:py:class:`Python <robotpy:wpimath.controller.PIDController>`) to help teams implement this functionality on their robots. The following example is from the RapidReactCommandBot example project ([Java](https://github.com/wpilibsuite/allwpilib/tree/v2027.0.0-alpha-6/wpilibjExamples/src/main/java/org/wpilib/examples/rapidreactcommandbot), [C++](https://github.com/wpilibsuite/allwpilib/tree/v2027.0.0-alpha-6/wpilibcExamples/src/main/cpp/examples/RapidReactCommandBot), [Python](https://github.com/robotpy/mostrobotpy/tree/main/examples/robot/RapidReactCommandBot)) and shows how PIDControllers can be used within the command-based framework:

.. tab-set::

   .. tab-item:: Java
      :sync: Java

      .. remoteliteralinclude:: https://raw.githubusercontent.com/wpilibsuite/allwpilib/v2027.0.0-alpha-6/wpilibjExamples/src/main/java/org/wpilib/examples/rapidreactcommandbot/subsystems/Shooter.java
         :language: java
         :lines: 5-
         :lineno-match:

   .. tab-item:: C++ (Header)
      :sync: C++ (Header)

      .. remoteliteralinclude:: https://raw.githubusercontent.com/wpilibsuite/allwpilib/v2027.0.0-alpha-6/wpilibcExamples/src/main/cpp/examples/RapidReactCommandBot/include/subsystems/Shooter.hpp
         :language: c++
         :lines: 5-
         :lineno-match:

   .. tab-item:: C++ (Source)
      :sync: C++ (Source)

      .. remoteliteralinclude:: https://raw.githubusercontent.com/wpilibsuite/allwpilib/v2027.0.0-alpha-6/wpilibcExamples/src/main/cpp/examples/RapidReactCommandBot/cpp/subsystems/Shooter.cpp
         :language: c++
         :lines: 5-
         :lineno-match:

   .. tab-item:: Python
      :sync: Python

      .. remoteliteralinclude:: https://raw.githubusercontent.com/robotpy/mostrobotpy/2027.0.0a6/examples/robot/RapidReactCommandBot/subsystems/shooter.py
         :language: python
         :lines: 5-
         :lineno-match:

A ``PIDController`` is declared inside the ``Shooter`` subsystem. It is used by ``ShootCommand`` alongside a feedforward to spin the shooter flywheel to the specified velocity. Once the ``PIDController`` reaches the specified velocity, the ``ShootCommand`` runs the feeder.
