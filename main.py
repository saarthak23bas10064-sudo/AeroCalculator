import math

def simulate_flight(initial_mass, fuel_mass, thrust, burn_rate):
    """
    Simulates a basic rocket trajectory with mass depletion.
    Designed for Aerospace Engineering 'Real World' flight mechanics.
    """
    g = 9.81  # m/s^2 (Standard Gravity)
    dt = 1.0  # time step in seconds
    time = 0
    velocity = 0
    altitude = 0
    current_mass = initial_mass + fuel_mass
    
    print(f"{'Time (s)':<10} | {'Altitude (m)':<15} | {'Velocity (m/s)':<15}")
    print("-" * 45)

    results = []

    while fuel_mass > 0 and altitude >= 0:
        # Physics: F = ma -> a = (Thrust - Weight) / current_mass
        acceleration = (thrust - (current_mass * g)) / current_mass
        velocity += acceleration * dt
        altitude += velocity * dt
        
        # Consuming fuel per time step
        fuel_consumed = burn_rate * dt
        fuel_mass -= fuel_consumed
        current_mass -= fuel_consumed
        time += dt
        
        results.append({"Time": time, "Altitude": round(altitude, 2), "Velocity": round(velocity, 2)})
        
        # Print status every 5 seconds to keep the console clean
        if time % 5 == 0: 
            print(f"{time:<10} | {round(altitude, 2):<15} | {round(velocity, 2):<15}")

    print("-" * 45)
    print(f"Simulation Ended. Final Altitude: {round(altitude, 2)}m")
    return results

# Main Execution Block
if __name__ == "__main__":
    try:
        # Parameters for a small sounding rocket
        flight_data = simulate_flight(
            initial_mass=5000, 
            fuel_mass=2000, 
            thrust=80000, 
            burn_rate=50
        )
        
        # Attempt to save to CSV for data analysis (Optional)
        try:
            import pandas as pd
            df = pd.DataFrame(flight_data)
            df.to_csv("flight_log.csv", index=False)
            print("\n[SUCCESS] Flight log exported to 'flight_log.csv' for analysis.")
        except ImportError:
            print("\n[NOTE] Pandas library not found. Results shown in console only.")

    except Exception as e:
        print(f"An error occurred during simulation: {e}")
