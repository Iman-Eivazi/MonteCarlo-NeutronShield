import numpy as np
import math

# Monte Carlo Neutron Shielding Simulation
# Author: Iman Eivazi
# Description:
# This script simulates the passage of neutrons through a one-dimensional material (shield)
# using Monte Carlo random sampling. It calculates the fraction of neutrons that pass 
# through the material without any interaction (transmitted neutrons).
# 
# Author: Iman Eivazi

def simulate_transmission(num_neutrons: int, thickness: float, mean_free_path: float) -> float:
    """
    Simulate the transmission of neutrons through a 1D shield using Monte Carlo method.
    
    Each neutron travels a random distance (distance to collision) drawn from an 
    exponential distribution characterized by the given mean free path (lambda).
    If this distance is greater than or equal to the shield thickness, the neutron 
    does not collide within the material and is transmitted. If the distance is less 
    than the thickness, the neutron collides (and is absorbed or reflected, thus not transmitted).
    
    Parameters:
        num_neutrons (int): Number of neutron particles to simulate.
        thickness (float): Thickness of the shield (in the same units as mean_free_path).
        mean_free_path (float): Mean free path of neutrons in the shield material (in the same units as thickness).
        
    Returns:
        float: The fraction of neutrons that are transmitted through the shield (between 0 and 1).
    """
    # Sample random collision distances for each neutron from an exponential distribution
    distances = np.random.exponential(mean_free_path, size=num_neutrons)
    # Determine how many neutrons travel at least the full thickness without collision
    transmitted_count = np.count_nonzero(distances >= thickness)
    # Calculate fraction of neutrons that were transmitted
    fraction_transmitted = transmitted_count / num_neutrons
    return fraction_transmitted

def main():
    """Run a sample simulation and display the results."""
    # Simulation parameters
    num_neutrons = 1000000   # simulate one million neutrons for good statistical accuracy
    thickness = 1.0          # thickness of the shield (for example, in mean free path units)
    mean_free_path = 1.0     # mean free path of neutrons in the material (same units as thickness)
    
    # Run simulation
    fraction = simulate_transmission(num_neutrons, thickness, mean_free_path)
    
    # (Optional) Calculate the expected transmission fraction analytically for comparison 
    expected = math.exp(-thickness / mean_free_path)
    
    # Display the results
    print(f"Simulated transmission fraction: {fraction:.4f}")
    print(f"Expected (analytical) fraction:  {expected:.4f}")

if __name__ == "__main__":
    main()

# I.E