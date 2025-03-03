import matplotlib
matplotlib.use('TkAgg')  # Fix for PyCharm backend issue
import numpy as np
import matplotlib.pyplot as plt

# === Adjustable Parameters ===
P_bottle = 400000  # Initial pressure in bottle (Pa)
P_atm = 101325     # Atmospheric pressure (Pa)
rho_water = 1000   # Density of water (kg/m³)
nozzle_diameter = 0.01  # Nozzle diameter (m)
water_volume = 1.0e-3  # Water volume in m³ (1L)
m_rocket = 0.15    # Dry mass of the rocket (kg)
dt = 0.01          # Time step (s)
g = 9.81           # Gravity (m/s²)

# === Derived Parameters ===
A_nozzle = np.pi * (nozzle_diameter / 2) ** 2  # Nozzle cross-section (m²)
v_exhaust = np.sqrt(2 * (P_bottle - P_atm) / rho_water)  # Exhaust velocity (m/s)
m_water = rho_water * water_volume  # Initial water mass (kg)

# === Simulation Variables ===
time = [0]
velocity = [0]
height = [0]
mass = [m_rocket + m_water]
acceleration = [0]  # Track acceleration over time

while m_water > 0:
    # Compute thrust
    mass_flow_rate = rho_water * A_nozzle * v_exhaust  # dm/dt
    thrust = mass_flow_rate * v_exhaust

    # Compute acceleration
    acc = (thrust / mass[-1]) - g

    # Update velocity & position
    new_velocity = velocity[-1] + acc * dt
    new_height = height[-1] + velocity[-1] * dt + 0.5 * acc * dt ** 2

    # Update mass
    m_water -= mass_flow_rate * dt
    m_water = max(m_water, 0)  # Prevent negative water mass
    mass.append(m_rocket + m_water)

    # Store values
    time.append(time[-1] + dt)
    velocity.append(new_velocity)
    height.append(new_height)
    acceleration.append(acc)

# === Plot Results ===
fig, ax1 = plt.subplots()
ax1.plot(time, height, label="Height (m)", color="blue")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Height (m)", color="blue")

ax2 = ax1.twinx()
ax2.plot(time, velocity, label="Velocity (m/s)", color="red")
ax2.set_ylabel("Velocity (m/s)", color="red")

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # Move third y-axis for acceleration
ax3.plot(time, acceleration, label="Acceleration (m/s²)", color="green")
ax3.set_ylabel("Acceleration (m/s²)", color="green")

plt.title("Ideal Water Rocket Launch (No Ground Effect)")
plt.show()
