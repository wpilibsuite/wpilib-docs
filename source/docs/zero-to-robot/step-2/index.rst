# Step 2: Install Your Tools

.. raw:: html

   <!-- Step badge -->
   <div class="sw-step-badge">
     <span class="sw-step-n">02</span>
     <div>
       <div class="sw-step-info-title">Install Your Tools</div>
       <div class="sw-step-info-sub">Step 2 of 4</div>
     </div>
   </div>

.. rubric:: System Requirements

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: Required for Driver Station

      **Windows**
      ^^^
      - Windows 11 (required for 2027+)
      - 8 GB RAM minimum, 16 GB recommended
      - Driver Station
      - All WPILib tools available

   .. grid-item-card:: Coding and Simulation Only

      **macOS / Linux**
      ^^^
      - macOS 12+ or modern Linux distro
      - WPILib + VS Code for writing and simulating code
      - Cannot run Driver Station or image Systemcore
      - Deploy code over USB or Wi-Fi (needs network access)

.. warning::

   **Windows 10 is no longer supported as of 2027.**
   Upgrade to Windows 11 before installing the Driver Station.

.. rubric:: Installation Steps

.. grid:: 1 1 2 2
   :gutter: 3

   .. grid-item-card:: WPILib Installer
      :link: wpilib-setup
      :link-type: doc
      :class-card: sw-card-shared

      **Part 1**
      ^^^
      Installs Visual Studio Code, WPILib extensions, and all
      desktop tools (Glass, Elastic, OutlineViewer).
      Required for Java, C++, and Python teams.

   .. grid-item-card:: FRC Game Tools
      :link: first-driver-station
      :link-type: doc
      :class-card: sw-card-shared

      **Part 2** — Windows only
      ^^^
      Installs the FRC Driver Station.
      Required on the laptop that will drive the robot at competition.

   .. grid-item-card:: RobotPy Setup
      :link: python-setup
      :link-type: doc
      :class-card: sw-card-shared

      **Part 3** — Python teams only
      ^^^
      Install RobotPy and the required Python packages.
      Java and C++ teams can skip this part.

   .. grid-item-card:: Offline Installation
      :link: offline-installation-preparations
      :link-type: doc
      :class-card: sw-card-shared

      **Optional**
      ^^^
      Preparing to install without internet access?
      Download the offline installer packages in advance.

.. rubric:: Verify Your Installation

After completing all parts above, confirm the installation is working:

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: Open VS Code

      Launch the WPILib VS Code shortcut (not the system VS Code).
      You should see the WPILib icon (W) in the activity bar.

   .. grid-item-card:: Run WPILib Command

      Press :kbd:`Ctrl+Shift+P` (or :kbd:`Cmd+Shift+P` on Mac)
      and type *WPILib*. You should see WPILib commands in the palette.

   .. grid-item-card:: Check Driver Station

      Open the FRC Driver Station (Windows only). It should launch
      without errors. "No Robot Communication" is expected.

.. tip::

   **Vendor libraries are not installed here.**
   Libraries like REVLib and Phoenix 6 are added per-project in Step 4
   using the WPILib Dependency Manager. You do not need them yet.

.. raw:: html

   <div class="sw-nav">
     <a class="sw-nav-btn" href="../step-1/index.html">
       &larr; Step 1: Build Your Robot</a>
     <a class="sw-nav-btn sw-next" href="../step-3/index.html">
       Step 3: Configure Your Control System &rarr;</a>
   </div>

.. toctree::
   :maxdepth: 1
   :hidden:

   offline-installation-preparations
   first-driver-station
   wpilib-setup
   python-setup
   step-2-next-steps
