# AeroCalc-Py: Rocket Trajectory Simulator

### Purpose
In Aerospace Engineering, calculating a rocket's vertical trajectory is complex because the mass of the vehicle decreases as fuel is consumed. This tool automates this calculation to provide accurate altitude and velocity data over time.

### Features
- **Physics Engine:** Real-time calculation of acceleration using $F = ma$.
- **Mass Depletion:** Simulates fuel burn rate over a set time-step.
- **Data Export:** Outputs flight logs to a `.csv` file for external analysis.

### How to Use
1. Ensure Python 3.x is installed.
2. Run the script via command prompt: `python main.py`.
3. The simulation will display time, altitude, and velocity updates until fuel exhaustion.
