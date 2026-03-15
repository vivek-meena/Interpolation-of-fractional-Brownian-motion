import numpy as np
import matplotlib.pyplot as plt

def calculate_tamsd_2d(x, y, dt):
    
   
    N = len(x)
    
    # Calculate for lags up to 50% of the trajectory length
    max_lag = N // 2
    
    tamsd = np.zeros(max_lag)
    lags = np.arange(1, max_lag + 1) * dt
    
    # Loop over every lag time 'n'
    for n in range(1, max_lag + 1):
        
        # --- Vectorized Calculation ---
        
        # 1. Create shifted arrays for X
        # x(t + delta) - x(t)
        dx = x[n:] - x[:-n]
        
        # 2. Create shifted arrays for Y
        # y(t + delta) - y(t)
        dy = y[n:] - y[:-n]
        
        # 3. Square and add them (The Pythagorean distance squared)
        squared_displacements = dx**2 + dy**2
        
        # 4. Average over all pairs
        tamsd[n-1] = np.mean(squared_displacements)
        
    return lags, tamsd


# 1. Generate Synthetic Data (2D Random Walk)

N_steps = 5000
dt = 0.1
D = 0.5 

# Generate noise
noise_x = np.random.normal(0, np.sqrt(2*D*dt), N_steps)
noise_y = np.random.normal(0, np.sqrt(2*D*dt), N_steps)

# Integrate to get trajectory
x_traj = np.cumsum(noise_x)
y_traj = np.cumsum(noise_y)

# 2. Calculate 2D TAMSD

lags, msd_val = calculate_tamsd_2d(x_traj, y_traj, dt)

# 3. Visualization

plt.figure(figsize=(12, 5))

# Plot A: The 2D Path (Bird's Eye View)
plt.subplot(1, 2, 1)
plt.plot(x_traj, y_traj, lw=0.8)
plt.plot(x_traj, y_traj, 'go', label='Start')
plt.plot(x_traj[-1], y_traj[-1], 'ro', label='End')
plt.title("2D Trajectory")
plt.xlabel("X ($\mu m$)")
plt.ylabel("Y ($\mu m$)")
plt.axis('equal')
plt.legend()

# Plot B: The TAMSD
plt.subplot(1, 2, 2)
plt.loglog(lags, msd_val, 'o', markersize=3, label="Calculated Eq 2 (2D)")

# Theoretical Line for 2D: MSD = 4*D*t
plt.loglog(lags, 4 * D * lags, 'r--', linewidth=2, label="Theory (4Dt)")

plt.title("2D TAMSD (Equation 2)")
plt.xlabel("Lag Time $\Delta$ (s)")
plt.ylabel("$\overline{\delta^2}$ ($\mu m^2$)")
plt.legend()
plt.grid(True, which="both", alpha=0.3)

plt.tight_layout()
plt.show()