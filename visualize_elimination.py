# visualize_elimination.py

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to save images as PNG
import matplotlib.pyplot as plt
import os

def visualize_eliminated_factor(factor, title="Eliminated Factor Visualization", filename="visualizations/eliminated_factor_q3.png"):
    """
    Visualizes the probability distribution of a factor obtained after eliminating a variable.
    The factor's probability table is shown as a bar chart, and the plot is saved as a PNG image.
    
    Parameters:
      factor: A dictionary representing the factor. It is expected to have a "probability" key,
              where each key is a sorted tuple of (variable, value) pairs and the corresponding value
              is the probability.
      title: Title for the plot.
      filename: File path (including name) where the PNG image will be saved.
                For example: "visualizations/eliminated_factor_q3.png"
    """
    # Extract the probability dictionary from the factor.
    prob_dict = factor.get("probability", {})
    
    # Create lists to store the assignment labels and corresponding probability values.
    labels = []
    probabilities = []
    
    for assignment_key, prob in prob_dict.items():
        # Build a human-readable label from the assignment (e.g., "X=0, Z=True")
        label = ', '.join(f"{var}={val}" for var, val in sorted(assignment_key))
        labels.append(label)
        probabilities.append(prob)
    
    # Set up the bar chart.
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(probabilities)), probabilities, tick_label=labels)
    plt.xlabel("Assignments")
    plt.ylabel("Probability")
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Ensure the output directory exists, then save the figure.
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
    print(f"{title} saved as {filename}")
    plt.close()

# Standalone test:
if __name__ == '__main__':
    # Example: Suppose after eliminating variable "Y" from a factor originally defined for X and Y,
    # you obtained a new factor defined only over X.
    test_eliminated_factor = {
         "unconditioned": {"X"},   # After elimination, only X remains.
         "conditioned": set(),
         "variableDomainsDict": {"X": [0, 1], "Y": [True, False]},
         "probability": {
            (("X", 0),): 0.6,
            (("X", 1),): 0.4,
         }
    }
    # This will save the visualization as "visualizations/eliminated_factor_q3.png" in your project.
    visualize_eliminated_factor(test_eliminated_factor)
