# visualize_factors.py

import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend so that images are saved as files.
import matplotlib.pyplot as plt
import os

def visualize_factor(factor, title="Factor Visualization", filename=None):
    """
    Visualizes a factor's probability distribution as a bar chart and saves it as a PNG image.
    
    Parameters:
      factor: A dictionary representing a factor. It should have a "probability" key that maps
              each assignment (represented as a sorted tuple of (variable, value) pairs) to a probability.
      title:  Title for the plot.
      filename: If provided, the plot is saved to this file (e.g., "visualizations/joined_factor.png").
                If not provided, the image is displayed interactively (though on 'Agg', no window will popup).
    """
    # Extract the probability dictionary.
    prob_dict = factor.get("probability", {})
    
    # Prepare labels and probability values.
    labels = []
    probabilities = []
    for assignment_key, prob in prob_dict.items():
        # Construct a human-readable assignment label. Sorting ensures consistency.
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
    
    # Save the plot as a PNG image if filename is provided.
    if filename:
        # Ensure the target directory exists.
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename)
        print(f"{'joined_factor'} saved as {filename}")
    else:
        plt.show()
    
    plt.close()

# Optional test to run this module directly
if __name__ == '__main__':
    # Create a sample factor, for example purposes only.
    test_factor = {
        "unconditioned": {"X"},
        "conditioned": {"Y"},
        "variableDomainsDict": {"X": [0, 1], "Y": [True, False]},
        "probability": {
            (("X", 0), ("Y", True)): 0.1,
            (("X", 0), ("Y", False)): 0.9,
            (("X", 1), ("Y", True)): 0.8,
            (("X", 1), ("Y", False)): 0.2,
        }
    }
    # Save the test factor visualization as a PNG image.
    visualize_factor(test_factor, title="Test Factor Visualization", filename="visualizations/test_factor.png")
