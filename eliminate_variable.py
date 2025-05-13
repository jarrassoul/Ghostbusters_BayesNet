# eliminate_variable.py

# We will reuse the helper function from join_factors to generate assignments.
# Import it from join_factors.py. (Make sure join_factors.py is in the same folder.)
from join_factors import getAllPossibleAssignments

def eliminate(factor, eliminationVariable):
    """
    Eliminates (sums out) the given variable from the factor.
    
    Parameters:
      factor (dict): A dictionary representing the factor with keys:
                     - "unconditioned": set of unconditioned variables
                     - "conditioned": set of conditioned variables
                     - "variableDomainsDict": dict mapping variable names to their domains
                     - "probability": dict with keys as sorted tuple assignments and values as probabilities
      eliminationVariable (str): The variable to eliminate (must be in factor["unconditioned"]).
    
    Returns:
      new_factor (dict): A new factor with eliminationVariable removed from the unconditioned set
                         and its probability table computed by summing over eliminationVariable.
    """
    # Check validity: the variable to eliminate must be unconditioned in the factor.
    if eliminationVariable not in factor["unconditioned"]:
        raise ValueError("Elimination variable must be an unconditioned variable in the factor.")
    
    # Create new sets for the resulting factor.
    new_unconditioned = factor["unconditioned"].copy()
    new_unconditioned.remove(eliminationVariable)  # Remove the variable we are eliminating.
    
    # The conditioned set remains the same.
    new_conditioned = factor["conditioned"].copy()
    
    # The variableDomainsDict stays the same.
    variableDomainsDict = factor["variableDomainsDict"]
    
    # Create the new factor data structure.
    new_factor = {
        "unconditioned": new_unconditioned,
        "conditioned": new_conditioned,
        "variableDomainsDict": variableDomainsDict,
        "probability": {}
    }
    
    # The new factor's scope contains the remaining variables (both unconditioned and conditioned).
    remaining_vars = list(new_unconditioned | new_conditioned)
    
    # For every assignment over the remaining variables...
    for assignment in getAllPossibleAssignments(remaining_vars, variableDomainsDict):
        # We will sum over all possible values that eliminationVariable can take.
        summed_probability = 0.0
        for value in variableDomainsDict[eliminationVariable]:
            # Extend the current assignment with a value for the elimination variable.
            extended_assignment = assignment.copy()
            extended_assignment[eliminationVariable] = value
            
            # Create a key by sorting the assignment items to ensure consistent ordering.
            extended_assignment_key = tuple(sorted(extended_assignment.items()))
            summed_probability += factor["probability"].get(extended_assignment_key, 0)
        
        # Create a key for the new factor that does not include the elimination variable.
        assignment_key = tuple(sorted(assignment.items()))
        new_factor["probability"][assignment_key] = summed_probability
    
    return new_factor

# -------------------- Test Harness for Question 3 --------------------

if __name__ == '__main__':
    # Define a simple variable domain.
    variableDomainsDict = {
        "X": [0, 1],
        "Y": [True, False]
    }
    
    # Create a sample factor over variables X and Y.
    # For example, let the factor represent P(X, Y) (an unnormalized probability table).
    factor = {
        "unconditioned": {"X", "Y"},
        "conditioned": set(),
        "variableDomainsDict": variableDomainsDict,
        "probability": {
            (("X", 0), ("Y", True)): 0.2,
            (("X", 0), ("Y", False)): 0.3,
            (("X", 1), ("Y", True)): 0.4,
            (("X", 1), ("Y", False)): 0.1
        }
    }
    
    # Eliminate the variable "Y" from the factor.
    new_factor = eliminate(factor, "Y")
    
    print("Factor after eliminating variable 'Y':")
    print("Unconditioned Variables:", new_factor["unconditioned"])
    print("Conditioned Variables:", new_factor["conditioned"])
    print("Probability Table:")
    for assignment_key, prob in new_factor["probability"].items():
        print(dict(assignment_key), "->", prob)
