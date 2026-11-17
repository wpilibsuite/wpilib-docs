Systemcore Cable Reference
==========================

Limelight's `cable specification, revision 1
<https://downloads.limelightvision.io/documents/systemcore_motioncore_cable_specifications.pdf>`_
contains connector-orientation drawings. The following map identifies selected
cable assemblies for beta and later Systemcore installations. Check the
selected sensor or device documentation for cable compatibility.

.. list-table:: Cable drawing index
   :header-rows: 1
   :widths: 30 50 20

   * - Cable
     - Pin assignments
     - PDF page
   * - Three-pin SL Smart I/O
     - 1: ground (black); 2: supply (red); 3: signal (white)
     - 18
   * - Two-pin SL CAN
     - 1: CAN High (yellow); 2: CAN Low (green)
     - 20
   * - Four-pin SL I2C/encoder
     - 1: ground; 2: supply; 3: SDA/encoder A; 4: SCL/encoder B
     - 24
   * - Micro-Fit+ to XT30 power adapter
     - 1–2: unpopulated; 3: supply (red); 4: ground (black)
     - 27

Identify pin 1 from the manufacturer's orientation drawing, not from a
left-to-right reading of this table. CAN cable uses twisted conductors and
gold-plated contacts. CAN cable impedance is not a separate termination resistor.

Select the cable and supply rating for the installed controller revision before
connecting hardware. For the remaining installation steps see
:doc:`/docs/zero-to-robot/systemcore-wiring`.
