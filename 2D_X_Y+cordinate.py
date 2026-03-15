import numpy as np
import matplotlib.pyplot as plt

# Parameters
D = 0.5
dt = 0.01
N = 10000

# Gaussian noise
eta_x = np.random.normal(0.0, 1.0, size=N)
eta_y = np.random.normal(0.0, 1.0, size=N)

# Trajectories
x = np.zeros(N + 1)
y = np.zeros(N + 1)

# Overdamped Langevin update
for k in range(N):
    x[k + 1] = x[k] + np.sqrt(2 * D * dt) * eta_x[k]
    y[k + 1] = y[k] + np.sqrt(2 * D * dt) * eta_y[k]

# Plot
plt.plot(x, y, lw=0.8)
plt.scatter(x[0], y[0], color='red', s=60, label='Start')
plt.scatter(x[-1], y[-1], color='green', s=60, label='End')

plt.xlabel("x")
plt.ylabel("y")
plt.title("2D Brownian Motion (Overdamped Langevin)")
plt.axis("equal")
plt.legend()
plt.show()

