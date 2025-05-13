# visualize_beliefs.py

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to save images
import matplotlib.pyplot as plt
import numpy as np
import os

def visualize_belief_distribution(beliefs, gridShape, filename="visualizations/beliefs_q6.png", title="Belief Distribution (Q6)"):
    """
    Visualizes a belief distribution over ghost positions as a heatmap.
    
    Parameters:
      beliefs:    A DiscreteDistribution (a dictionary) mapping (x,y) positions to probabilities.
      gridShape:  A tuple (max_x, max_y) representing the size of the grid. Positions are assumed to lie in 0..max_x-1 and 0..max_y-1.
      filename:   File path where the image will be saved, e.g., "visualizations/beliefs_q6.png".
      title:      Title for the plot.
    """
    max_x, max_y = gridShape
    # Create an array of zeros with shape (max_y, max_x) as imshow uses row,col order (i.e., y, x).
    grid = np.zeros((max_y, max_x))
    
    # For each position in the belief distribution, set the respective grid cell.
    for (x, y), prob in beliefs.items():
        if 0 <= x < max_x and 0 <= y < max_y:
            grid[y, x] = prob   # Note: row index=y, column index=x
    
    plt.figure(figsize=(max_x, max_y))
    plt.imshow(grid, cmap="hot", interpolation="nearest")
    plt.colorbar(label="Probability")
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
    print(f"{title} saved as {filename}")
    plt.close()

# Standalone test:
if __name__ == '__main__':
    from discrete_distribution import DiscreteDistribution
    # Create a fake belief distribution for a 5x5 grid.
    beliefs = DiscreteDistribution()
    for x in range(5):
        for y in range(5):
            beliefs[(x, y)] = (x + y + 1)  # just some pattern
    beliefs.normalize()
    visualize_belief_distribution(beliefs, gridShape=(5,5), filename="visualizations/test_beliefs.png", title="Test Belief Distribution")
