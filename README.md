# Generate the README.md file with the provided content

content = """
# Interpolation of Fractional Brownian Motion

This project focuses on the **numerical simulation and analysis of stochastic processes**, particularly Brownian motion. The simulation is implemented using **Python** to generate particle trajectories based on the **Langevin equation**, and the statistical properties of the motion are analyzed using mean square displacement and probability distribution functions.

---

# Overview

Brownian motion describes the random movement of particles caused by thermal fluctuations. It is widely used in **statistical physics, diffusion theory, and stochastic modeling**.

In this project:

- Multiple Brownian trajectories are simulated.
- Diffusion behavior is analyzed using **TAMSD and EAMSD**.
- Simulation results are compared with **analytical diffusion theory**.
- Probability distributions of particle positions are studied.

---

# Mathematical Model

## Langevin Equation

The stochastic motion of a Brownian particle is modeled by

dx(t) = sqrt(2D dt) * η(t)

where  

- D = diffusion coefficient  
- dt = time step  
- η(t) = Gaussian white noise with mean 0 and variance 1  

---

# Probability Distribution Function (PDF)

For Brownian motion, the position distribution follows a **Gaussian diffusion law**

P(x,t) = (1 / sqrt(4πDt)) * exp(-x² / (4Dt))

where  

- P(x,t) = probability density  
- x = particle position  
- t = time  
- D = diffusion coefficient  

The simulation histogram of particle positions is compared with this theoretical distribution.

---

# Time Averaged Mean Square Displacement (TAMSD)

The TAMSD for a trajectory x(t) is defined as

δ²(Δ) = (1/(T-Δ)) Σ [x(t+Δ) − x(t)]²

where  

- Δ = lag time  
- T = total observation time  

TAMSD measures diffusion behavior within a **single trajectory**.

---

# Ensemble Averaged TAMSD

When multiple trajectories are simulated, the **ensemble average** of TAMSD is calculated as

<δ²(Δ)> = (1/N) Σ δ²_i(Δ)

where  

- N = number of trajectories  

---

# Ensemble Averaged Mean Square Displacement (EAMSD)

The ensemble averaged MSD is defined as

<x²(t)> = (1/N) Σ [x_i(t) − x_i(0)]²

For normal Brownian diffusion,

<x²(t)> = 2Dt

which shows **linear scaling with time**.

---

# Simulation Parameters

| Parameter | Value |
|-----------|------|
| Number of trajectories | 1000 |
| Time steps | 50,000 |
| Time step size | 0.001 |
| Diffusion coefficient | 0.5 |

---

# Results and Analysis

The simulation produces the following results:

### Brownian Trajectories
Random particle paths demonstrating stochastic motion.

### TAMSD Analysis
Time-averaged MSD is computed for individual trajectories to study diffusion behavior.

### Ensemble MSD
Averaging across many trajectories shows the theoretical relation

MSD ∝ t

### Probability Distribution
The simulated distribution of particle positions matches the **Gaussian distribution predicted by diffusion theory**.

### Diffusion Coefficient Estimation
Least-square fitting is used to estimate the diffusion coefficient from log–log MSD plots.

---

# Technologies Used

- Python  
- NumPy  
- Matplotlib  

---

# How to Run

Clone the repository

git clone https://github.com/vivek-meena/Interpolation-of-fractional-Brownian-motion/tree/main

Install dependencies

pip install numpy matplotlib

Run the simulation

python simulation.py

---

# Applications

The methods used in this project are relevant for

- Statistical physics
- Diffusion and transport phenomena
- Particle tracking experiments
- Stochastic modeling
- Financial random walk models
"""

path = "/mnt/data/README.md"
with open(path, "w") as f:
    f.write(content)

path
