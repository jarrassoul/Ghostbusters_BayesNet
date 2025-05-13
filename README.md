# Ghostbusters BayesNet & Particle Filter Inference Project

This project implements probabilistic inference methods to track ghost positions in a Pacman maze. It combines exact inference using Bayes Nets with approximate inference using Particle Filters. The project was developed as part of an advanced AI course and demonstrates several key concepts including factor operations, variable elimination, observation and time updates, and action selection under uncertainty.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation and Requirements](#installation-and-requirements)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Pushing to GitHub](#pushing-to-github)
- [Acknowledgements](#acknowledgements)

---

## Overview

The project segments are organized as follows:

1. **Bayes Net & Exact Inference (Q1 – Q8)**
   - **Q1:** Construct the BayesNet structure.
   - **Q2:** Join factors (i.e., multiply probability tables).
   - **Q3:** Eliminate a variable (sum out).
   - **Q4:** Perform variable elimination.
   - **Q5:** Create a `DiscreteDistribution` class for defining distributions and computing noisy observation probabilities.
   - **Q6:** Update beliefs using exact inference based on noisy observations.
   - **Q7:** Update beliefs as time elapses by incorporating ghost motion (notably the GoSouthGhost behavior).
   - **Q8:** Full inference test – determine the most likely ghost positions and choose an action for Pacman accordingly.
2. **Particle Filter (Q9 – Q11)**
   - **Q9:** Initialize particles uniformly across legal positions.
   - **Q10:** Update particles based on noisy observations (resampling).
   - **Q11:** Update particles based on ghost motion (time elapse).

Visualizations (heatmaps, network diagrams, game boards) are generated and saved in the `visualizations/` folder at various stages to aid in debugging and to provide visual evidence of the inference process.

---

## Project Structure

Below is the directory layout of the project:


---

## Installation and Requirements

Ensure you have the following installed:

- **Python 3.6+**
- **Git**
- **Matplotlib** (for plotting visualizations)
- **NetworkX** (for graph visualizations)

You can install the required Python packages using pip:

```bash
pip install matplotlib networkx
