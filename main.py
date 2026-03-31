import math
import csv

class RocketSimulator:
    def __init__(self, mass, thrust, burn_time, drag_coeff, area):
        self.m = mass  # kg
        self.T = thrust  # N
        self.bt = burn_time  # s
        self.Cd = drag_coeff
        self.A = area  # m^2
        self.g = 9.81
        self.rho = 1.225  # Air density at sea level

    def calculate_trajectory(self, dt=0.1):
        time, alt, vel = 0, 0, 0
        log = []

        while alt >= 0:
            # Determine Thrust Phase
            current_T = self.T if time <= self.bt else 0
            
            # Simple Atmospheric Model (Density decreases with height)
            current_rho = self.rho * math.exp(-alt / 8500)
            
            # Physics Calculations
            drag = 0.5 * current_rho * (vel**2) * self.Cd * self.A
            net_force = current_T - (self.m * self.g) - (drag if vel > 0 else -drag)
            accel = net_force / self.m
            
            vel += accel * dt
            alt += vel * dt
            
            log.append({"Time": round(time, 2), "Altitude": round(alt, 2), "Velocity": round(vel, 2)})
            time += dt
            if time > 100: break # Safety break

        return log

# Example Usage
my_rocket = RocketSimulator(mass=5.0, thrust=150, burn_time=3.0, drag_coeff=0.75, area=0.01)
flight_data = my_rocket.calculate_trajectory()

# Save to CSV (Submission Requirement)
with open('flight_log.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Time", "Altitude", "Velocity"])
    writer.writeheader()
    writer.writerows(flight_data)

print("Simulation Complete. Data saved to flight_log.csv")