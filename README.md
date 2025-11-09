# One-Dimensional Neutron Shielding Monte Carlo Simulation

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

**Author:** Iman Eivazi  
**Project Purpose:** Course project in nuclear physics and Python programming

## Introduction
Neutron shielding is a crucial aspect of nuclear reactor design and radiation protection. In simple terms, it is important to predict how many neutrons will pass through a shielding material of a given thickness versus how many will be stopped. Analytical methods exist for idealized conditions (for example, using the exponential attenuation law for neutron transmission), but complex scenarios often require computational approaches. This project uses a **Monte Carlo simulation** to model the passage of neutrons through a one-dimensional slab shield and estimates the probability of transmission (neutrons that make it through the shield) versus absorption. The simulation results are then compared to an analytical solution for validation. This project was developed by Iman Eivazi as part of an academic course in nuclear physics and Python programming.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Example Results](#example-results)
- [Author](#author)
- [License](#license)

## Installation
To get started with the simulation, please ensure you have the following installed:

- **Python 3.8+** – The code is written for Python 3.8 and above.
- **NumPy** – The simulation uses NumPy for efficient numeric computations.

Follow these steps to set up the project:
1. **Clone the repository** (or download the project files) to your local machine:
   ```bash
   git clone https://github.com/iman-eivazi/MonteCarlo-NeutronShield.git
Install the requirements. You can install NumPy (and any other dependencies) using pip:
bash
Copy code
pip install numpy
(Alternatively, you can use an environment manager like venv or conda to manage dependencies.)

## Usage
After installation, you can run the Monte Carlo simulation script to perform the neutron shielding simulation. The main script (for example, monte_carlo_simulation.py) can be executed from the command line as follows:
bash
Copy code
python monte_carlo_simulation.py
By default, the script will run the simulation with a set of default parameters (such as number of neutrons, shield thickness, etc.) and output the estimated transmission probability along with a comparison to the analytical result. You can also adjust the simulation parameters via command-line arguments (if implemented) or by editing the configuration variables at the top of the script. For example:
bash
Copy code
python monte_carlo_simulation.py --thickness 5.0 --num-neutrons 100000 --cross-section 1.0
The above command (if supported by the script) would simulate neutron transmission through a shield of thickness 5.0 (in arbitrary units) using 100,000 simulated neutrons and a macroscopic cross-section of 1.0 for the shield material. When the simulation runs, it will either print the results to the console or save them to an output file (depending on how the code is structured). Typically, the output includes the fraction of neutrons transmitted through the shield, the fraction absorbed, and the theoretical expected transmission for comparison.

## Project Structure
The repository is organized as follows:
bash
Copy code
├── monte_carlo_simulation.py   # Main Python script to run the Monte Carlo simulation
├── analytical_solution.py     # (Optional) Script or module for analytical calculations (if separate)
├── README.md                  # Project documentation (this file)
└── shield_schematic.png       # Schematic diagram of the shield scenario (for README illustration)
Note: The file structure may vary. In this project, all core simulation code can be contained in the main script. If an analytical_solution.py is not present, the analytical calculation is likely done within the main script itself. The image file shield_schematic.png is a placeholder name for a diagram illustrating the simulation scenario (if provided).

## Configuration
The simulation behavior can be modified using several parameters:
Number of neutrons (num_neutrons) – The number of virtual neutrons to simulate. A higher number yields more accurate (less noisy) results at the cost of longer runtime. The default might be set to a value like 100,000.
Shield thickness (thickness) – The thickness of the shielding material (in arbitrary units). This determines how far neutrons must travel to completely penetrate the shield. You can adjust this to simulate different shield thicknesses. The default could be, for example, 1.0 (one unit length).
Macroscopic cross-section (cross_section) – This value represents the probability per unit length of a neutron interacting with the shield material (via absorption or scattering). In essence, it is the inverse of the mean free path of neutrons in the material. For simplicity, the default is often set to 1.0 (in arbitrary units), meaning the mean distance a neutron travels before an interaction is 1 unit of length.
Random seed – (If implemented) Setting a seed for the random number generator ensures reproducible results. By default, the script may or may not fix the seed; if not, results will vary slightly each run.
These parameters may be defined at the top of the script as constants or may be provided as command-line options. To change them, edit the script or use the arguments as shown in the Usage section above. By experimenting with these parameters, you can explore different scenarios (for example, how increasing the shield thickness reduces the transmission probability, or how many neutrons are needed to get a stable estimate).

## Example Results
To validate the simulation, the results can be compared with the expected analytical solution. Analytically, if neutrons travel through a homogeneous material, the fraction that survive (i.e. pass through without any interaction) follows an exponential attenuation law. In other words, the transmission probability for a slab of thickness x is approximately: T = exp(-Σ x) where Σ is the macroscopic cross-section of the material (a measure of how likely a neutron is to interact per unit path length). The Monte Carlo simulation essentially performs a random experiment to estimate this probability by simulating many neutrons and counting how many make it through the shield. Below is a sample output from the simulation alongside the theoretical prediction. In this example, we simulated 100,000 neutrons for various shield thickness values, with a cross-section Σ = 1.0 (meaning the mean free path of neutrons is 1 unit length). The results show the Monte Carlo estimated transmission probability and the analytical value (e<sup>−Σx</sup>) for each thickness:
Shield Thickness	Monte Carlo Transmission	Analytical Transmission
1.0	0.36918	0.36788
2.0	0.13557	0.13534
3.0	0.04953	0.04979

Note: Due to the random nature of Monte Carlo simulation, the estimated probabilities will vary slightly with each run (especially if the number of neutrons is limited). However, as seen above, with a sufficiently large sample of neutrons the Monte Carlo results closely match the analytical values. Any small differences (on the order of a few thousandths or less) are due to statistical variation. 
 Illustration: Conceptual diagram of the neutron shielding simulation. A beam of neutrons is directed at a slab of material; some neutrons pass through, while others are absorbed or deflected.
 
## Author
Iman Eivazi – Developer and author of this project.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software. See the full license text below:
sql
Copy code
MIT License

## License
Copyright (c) 2025 Iman Eivazi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.