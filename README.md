# Interpolation of Fractional Brownian Motion

**B.Tech Project Report** | Department of Physics | Indian Institute of Technology Guwahati
**Author:** Vivek Meena (Roll No. 230121067) | **Supervisor:** Prof. Samudrajit Thapa | **Year:** 2026

---

## Overview

This project presents a comprehensive **numerical simulation and statistical analysis of Brownian motion** using a discrete Langevin dynamics framework in Python. A large ensemble of stochastic particle trajectories is generated and analyzed using multiple complementary statistical tools to verify the fundamental properties of classical Brownian diffusion.

All analyses are implemented in a single Jupyter Notebook (`1ALL_CODE.ipynb`) and supporting Python scripts.

---

## Table of Contents

- [Overview](#overview)
- [Mathematical Model](#mathematical-model)
- [Simulation Parameters](#simulation-parameters)
- [Analyses Performed](#analyses-performed)
- [Results](#results)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [References](#references)

---

## Mathematical Model

### Langevin Equation (Discrete Form)

The stochastic motion of a Brownian particle is modeled using:

$$x_{i+1} = x_i + \sqrt{2D \, dt} \cdot \eta_i$$

where:
- $D$ = diffusion coefficient
- $dt$ = time step
- $\eta_i \sim \mathcal{N}(0, 1)$ = standard normal random variable

### Time-Averaged Mean Squared Displacement (TAMSD)

$$\delta_i^2(\Delta) = \frac{1}{N - \Delta} \sum_{k=1}^{N-\Delta} \left[ x_i(k + \Delta) - x_i(k) \right]^2$$

### Ensemble-Averaged TAMSD (EATAMSD)

$$\langle \delta^2(\Delta) \rangle = \frac{1}{N_\text{traj}} \sum_{i=1}^{N_\text{traj}} \delta_i^2(\Delta)$$

### Ergodicity Breaking (EB) Parameter

$$EB(\Delta) = \frac{\langle \delta^4(\Delta) \rangle}{\langle \delta^2(\Delta) \rangle^2} - 1$$

For Brownian motion, the theoretical prediction is:

$$EB(\Delta) = \frac{4\Delta}{3T}$$

### Probability Distribution Function

$$P(x, t) = \frac{1}{\sqrt{4\pi D t}} \exp\left(-\frac{x^2}{4Dt}\right)$$

---

## Simulation Parameters

| Parameter | Value |
|---|---|
| Number of trajectories | 5000 |
| Number of time steps | 1000 |
| Time step `dt` | 0.0001 |
| Diffusion coefficient `D` | 0.5 |

---

## Analyses Performed

The notebook (`1ALL_CODE.ipynb`) contains the following analyses in order:

### 1. Trajectory Generation
- Simulates 5000 independent Brownian trajectories using the Langevin model
- Plots 20 sample trajectories to visualize stochastic motion

### 2. Time-Averaged MSD (TAMSD)
- Computes TAMSD for all 5000 trajectories
- Computes ensemble-averaged TAMSD
- Plots on log-log scale to verify linear scaling $\delta^2 \propto \Delta$

### 3. Ensemble-Averaged MSD (EAMSD) vs EATAMSD
- Computes EAMSD: $\langle x^2(t) \rangle = \frac{1}{N} \sum [x_i(t) - x_i(0)]^2$
- Compares EAMSD and EATAMSD on log-log scale to verify ergodicity

### 4. Scaling Analysis & Diffusion Coefficient Estimation
- Performs log-log linear regression on TAMSD:  $y = mx + c$
- Extracts scaling exponent $\alpha$ (slope) and intercept $c$
- Estimates diffusion coefficient: $D = 10^c / 2$

### 5. Ergodicity Breaking (EB) Parameter
- Computes EB parameter from TAMSD fluctuations
- Compares simulation EB with theoretical prediction $4\Delta/3T$

### 6. Position Distribution & Gaussian Analysis
- Extracts particle positions at final time $t = T$
- Fits Gaussian distribution and compares with theoretical PDF
- Reports mean $\mu$, variance $\sigma^2$, and theoretical $2Dt$

### 7. Time Evolution of Variance
- Computes $\sigma^2(t)$ at every time step across all trajectories
- Compares with theoretical curve $2Dt$

### 8. Time Evolution of PDF
- Extracts position distributions at multiple time snapshots
- Fits Gaussian at each time and overlays theoretical PDF

### 9. Displacement Distribution at Different Lag Times
- Analyzes displacement PDFs for lag values: $\Delta = 2, 10, 15, 20, 50, 60, 70, 100$
- Fits Gaussian and compares with theory $\sigma^2 = 2D\Delta \cdot dt$
- Generates individual subplots and combined overlay plot

---

## Results

| Quantity | Simulated | Theoretical |
|---|---|---|
| Scaling exponent $\alpha$ | 1.0079 | 1.0 |
| Diffusion coefficient $D$ | 0.5214 | 0.5 |
| Mean position $\mu$ | 0.0043 | 0.0 |
| Variance $\sigma^2$ at $t=T$ | 0.0988 | 0.0999 |

All analyses confirm that the simulated system exhibits **classical Brownian motion with normal diffusion and ergodic behavior**.

---

## Project Structure

```
Interpolation-of-fractional-Brownian-motion/
│
├── null.ipynb          # Main Jupyter Notebook (all analyses)
└── README.md                # This file
```

---

## Requirements

Install dependencies using:

```bash
pip install numpy matplotlib scipy
```

| Package | Version |
|---|---|
| Python | ≥ 3.6 |
| NumPy | any |
| Matplotlib | any |
| SciPy | any |

---

## How to Run

### Option 1 — Jupyter Notebook (Recommended)

```bash
# Clone the repository
git clone https://github.com/vivek-meena/Interpolation-of-fractional-Brownian-motion.git

# Navigate into the folder
cd Interpolation-of-fractional-Brownian-motion

# Install dependencies
pip install numpy matplotlib scipy

# Launch Jupyter
jupyter notebook 1ALL_CODE.ipynb
```

### Option 2 — Run individual Python scripts

```bash
python 1D_TAMSD.py
python TAMSD_MT.py
python log.py
```

---

## References

1. S. Thapa, N. Lukat, C. Selhuber-Unkel, A. G. Cherstvy, and R. Metzler, *"Transient superdiffusion of polydisperse vacuoles in highly motile amoeboid cells,"* J. Chem. Phys., vol. 150, p. 144901, 2019. https://doi.org/10.1063/1.5086269

2. I. M. Jánosi, A. Padash, J. A. C. Gallas, and H. Kantz, *"Passive tracer advection in the equatorial Pacific region: statistics, correlations and a model of fractional Brownian motion,"* Ocean Sci., vol. 18, pp. 307–320, 2022. https://doi.org/10.5194/os-18-307-2022

3. Wikipedia, *"Brownian motion,"* Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Brownian_motion

---

## License

This project was developed as a B.Tech project at **IIT Guwahati** under the supervision of **Prof. Samudrajit Thapa**. All rights reserved © 2026 Vivek Meena.
