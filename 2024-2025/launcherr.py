import matplotlib
matplotlib.use('TkAgg')  # Fix for PyCharm backend issue
import numpy as np
import matplotlib.pyplot as plt

# === Adjustable Parameters ===
P_bottle = 400000  # Initial pressure in bottle (Pa)
P_atm = 101325     # Atmospheric pressure (Pa)
rho_water = 1000   # Density of water (kg/m³)
nozzle_diameter = 0.01  # Nozzle diameter (m)
bottle_diameter = 0.1  # Bottle diameter (m²)
water_volume = 1.0e-3  # Water volume in m³ (1L)
m_rocket = 0.15    # Dry mass of the rocket (kg)
dt = 0.001         # Time step (s)
g = 9.81           # Gravity (m/s²)

# === Derived Parameters ===
A_nozzle = np.pi * (nozzle_diameter / 2) ** 2  # Nozzle cross-section (m²)
A_bottle = np.pi * (bottle_diameter / 2) ** 2  # Bottle cross-section (m²)
v_exhaust = np.sqrt(2 * (P_bottle - P_atm) / rho_water)  # Exhaust velocity (m/s)
m_water = rho_water * water_volume  # Initial water mass (kg)

# === Simulation Variables ===
time = [0]
velocity = [0]
mass = [m_rocket + m_water]
acceleration = [0]
a_internal_list = [0]  # Track internal acceleration
v_bottle = v_exhaust * (A_nozzle / A_bottle)  # Initial velocity of water inside bottle
dv_bottle_dt = 0  # Initialize rate of change of internal water velocity

while m_water > 0:
    # Compute mass flow rate
    mass_flow_rate = rho_water * A_nozzle * v_exhaust  # dm/dt
    thrust = mass_flow_rate * v_exhaust  # Thrust force

    # Compute acceleration including internal water movement
    if len(time) > 1:
        dv_bottle_dt = (v_bottle - (v_exhaust * (A_nozzle / A_bottle))) / dt  # Rate of change of internal water velocity
    a_internal = (m_water / (m_rocket + m_water)) * dv_bottle_dt  # Internal water correction
    acc = (thrust / (m_rocket + m_water)) - g - a_internal  # Adjusted acceleration

    # Update velocity
    new_velocity = velocity[-1] + acc * dt

    # Update mass
    m_water -= mass_flow_rate * dt
    m_water = max(m_water, 0)  # Prevent negative water mass
    mass.append(m_rocket + m_water)

    # Store values
    time.append(time[-1] + dt)
    velocity.append(new_velocity)
    acceleration.append(acc)
    a_internal_list.append(a_internal)
    v_bottle = v_exhaust * (A_nozzle / A_bottle)  # Update internal water velocity

# === Plot Results ===
fig, ax1 = plt.subplots()
ax1.plot(time, velocity, label="Velocity (m/s)", color="red")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Velocity (m/s)", color="red")

ax2 = ax1.twinx()
ax2.plot(time, acceleration, label="Acceleration (m/s²)", color="green")
ax2.set_ylabel("Acceleration (m/s²)", color="green")

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # Move third y-axis for internal acceleration
ax3.plot(time, a_internal_list, label="Internal Acceleration (m/s²)", color="blue")
ax3.set_ylabel("Internal Acceleration (m/s²)", color="blue")

plt.title("Water Rocket Launch with Internal Water Effect")
plt.show()
