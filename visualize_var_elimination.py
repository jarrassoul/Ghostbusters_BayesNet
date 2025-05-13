# visualize_var_elimination.py

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to save images as PNG
import matplotlib.pyplot as plt
import os

def visualize_var_elim_factor(factor, title="Variable Elimination Result (Q4)", filename="visualizations/var_elim_result_q4.png"):
    """
    Visualizes the factor resulting from variable elimination as a bar chart
    and saves the plot as a PNG image.

    Parameters:
      factor: A dictionary representing the factor. It is expected to have a key "probability",
              which maps each assignment (a sorted tuple of (variable, value) pairs) to a probability.
      title:  Title of the plot.
      filename: The full path (including filename) where the PNG image will be saved.
                For example: "visualizations/var_elim_result_q4.png"
    """
    # Extract the probability table from the factor.
    prob_dict = factor.get("probability", {})
    
    # Prepare lists for the assignment labels and corresponding probability values.
    labels = []
    probabilities = []
    for assignment_key, prob in prob_dict.items():
        # Convert the assignment (a tuple of (variable, value) pairs) to a readable string.
        label = ', '.join(f"{var}={val}" for var, val in sorted(assignment_key))
        labels.append(label)
        probabilities.append(prob)
    
    # Create the bar chart.
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(probabilities)), probabilities, tick_label=labels)
    plt.xlabel("Assignments")
    plt.ylabel("Probability")
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Ensure the directory exists, then save the figure.
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
    print(f"{title} saved as {filename}")
    plt.close()

# Standalone test:
if __name__ == '__main__':
    # For a simple test, suppose variable elimination results in a factor defined only over Y.
    test_factor = {
        "unconditioned": {"Y"},
        "conditioned": set(),
        "variableDomainsDict": {"Y": [True, False]},
        "probability": {
            (("Y", True),): 0.3,
            (("Y", False),): 0.7
        }
    }
    visualize_var_elim_factor(test_factor)
