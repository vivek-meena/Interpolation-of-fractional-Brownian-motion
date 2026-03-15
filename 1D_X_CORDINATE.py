import numpy as np
import matplotlib.pyplot as plt

def generate_1d_langevin(N, dt, D):
    
    # 1. Pre-allocate the x array with zeros
    x = np.zeros(N)
    
    # 2. Calculate the scaling factor: sqrt(2 * D * dt)
    scale_factor = np.sqrt(2 * D * dt)
    
    # 3. Generate N random numbers (The noise term)
    random_kicks = np.random.normal(loc=0.0, scale=1.0, size=N)
    
    # x_{i+1} = x_i + (scale_factor * random_kick)
    for i in range(1, N):
        dx = scale_factor * random_kicks[i-1]
        x[i] = x[i-1] + dx
        
    return x

trajectory = generate_1d_langevin(N=1000, dt=0.1, D=0.5)

# Plotting the result
plt.plot(trajectory)
plt.title("1D Langevin Trajectory (Simulated)")
plt.xlabel("Frame (i)")
plt.ylabel("Position (x)")
plt.show()