# Quick Start for Returning Teams

This checklist is for returning FRC teams preparing an existing robot or
project for the 2027 season. FTC teams moving to Systemcore for the first time
should begin with :doc:`New to WPILib </docs/zero-to-robot/new-to-wpilib>`.

1. Read the :doc:`2027 changelog
   </docs/yearly-overview/yearly-changelog>`, :doc:`known issues
   </docs/yearly-overview/known-issues>`, and :doc:`removed features
   </docs/yearly-overview/removed-features>` before changing the robot.
2. Make a backup or version-control checkpoint of last season's project.
3. :doc:`Update or image Systemcore
   </docs/zero-to-robot/step-3/imaging-your-systemcore>` for the current
   season.
4. Update the firmware on and :doc:`program the VH-109 radios
   </docs/zero-to-robot/step-3/radio-programming>`.
5. :doc:`Install the FIRST Driver Station
   </docs/zero-to-robot/step-2/first-driver-station>`.
6. Set up the environment for your language:

   - **Java or C++:** :doc:`install WPILib
     </docs/zero-to-robot/step-2/wpilib-setup>`.
   - **Python:** :doc:`install or update RobotPy
     </docs/zero-to-robot/step-2/python-setup>`. Install the WPILib desktop
     environment too if you want its VS Code setup and tools.
   - **Blocks:** choose either the OnBot or desktop path in :doc:`Step 2
     </docs/zero-to-robot/step-2/index>`.
   - **LabVIEW:** use the OnBot path in Step 2. Desktop LabVIEW is not
     available for Systemcore.

7. Open last season's project:

   - **Java or C++:** use :doc:`Import a Robot Project
     </docs/software/vscode-overview/importing-last-years-robot-code>`.
   - **Python:** open the existing project folder, update its dependencies,
     and run ``robotpy sync``.
   - **OnBot languages:** create or open the project using the Systemcore
     editor. Detailed migration instructions will be added as the 2027
     software is finalized.

8. :doc:`Update third-party libraries
   </docs/software/vscode-overview/3rd-party-libraries>`, then build the
   project and address changes identified in the changelog.
9. Test with the drivetrain safely supported, following :doc:`Step 4
   </docs/zero-to-robot/step-4/index>` before returning the robot to service.
