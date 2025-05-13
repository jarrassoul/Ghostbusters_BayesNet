# join_factors.py

import itertools

def getAllPossibleAssignments(variables, variableDomainsDict):
    """
    Generates all possible assignments for the given variables.
    
    Parameters:
      variables: A list of variable names.
      variableDomainsDict: A dict mapping variable names to a list of possible values.
    
    Yields:
      A dictionary representing one possible assignment.
    """
    # Prepare list of domains for the given variables.
    domains_list = [variableDomainsDict[var] for var in variables]
    for values in itertools.product(*domains_list):
        yield dict(zip(variables, values))

def joinFactors(factors):
    """
    Joins a list of factors by multiplying their probability tables.
    
    Parameters:
      factors (list): A list of factors. Each factor is a dict with:
                      - "unconditioned": set of unconditioned variables
                      - "conditioned": set of conditioned variables
                      - "variableDomainsDict": dict mapping variable names to their domain
                      - "probability": a dict mapping an assignment (as a sorted tuple) to a probability.
                      
    Returns:
      A new factor (dictionary) representing the product of the input factors.
    """
    # Aggregate the new unconditioned and conditioned sets.
    new_unconditioned = set()
    new_conditioned = set()
    variableDomainsDict = None
    
    for factor in factors:
        new_unconditioned |= factor["unconditioned"]
        new_conditioned |= factor["conditioned"]
        if variableDomainsDict is None:
            variableDomainsDict = factor["variableDomainsDict"]
    
    # Remove variables from conditioned that are also unconditioned.
    new_conditioned -= new_unconditioned
    
    new_factor = {
        "unconditioned": new_unconditioned,
        "conditioned": new_conditioned,
        "variableDomainsDict": variableDomainsDict,
        "probability": {}
    }
    
    # All variables present in the new factor.
    all_vars = list(new_unconditioned | new_conditioned)
    
    # For every assignment for the full set of variables, compute the product of probabilities.
    for assignment in getAllPossibleAssignments(all_vars, variableDomainsDict):
        # Use sorted tuple of (var, value) for consistent key ordering.
        assignment_key = tuple(sorted(assignment.items()))
        prob = 1.0
        for factor in factors:
            # Get the variables that this factor covers.
            factor_vars = list(factor["unconditioned"] | factor["conditioned"])
            # Restrict the assignment to these variables.
            factor_assignment = {var: assignment[var] for var in factor_vars}
            factor_assignment_key = tuple(sorted(factor_assignment.items()))
            # Multiply the probabilities.
            prob *= factor["probability"].get(factor_assignment_key, 0)
        new_factor["probability"][assignment_key] = prob

    return new_factor

# Optional test harness for Q2
if __name__ == '__main__':
    # Example variable domains: 
    variableDomainsDict = {
        "X": [0, 1],
        "Y": [True, False]
    }
    
    # Factor A: Factor on variable X with probabilities P(X)
    factorA = {
        "unconditioned": {"X"},
        "conditioned": set(),
        "variableDomainsDict": variableDomainsDict,
        "probability": {
            (("X", 0),): 0.3,
            (("X", 1),): 0.7,
        }
    }
    
    # Factor B: Factor on variable Y conditioned on X with probabilities P(Y|X)
    factorB = {
        "unconditioned": {"Y"},
        "conditioned": {"X"},
        "variableDomainsDict": variableDomainsDict,
        "probability": {
            (("X", 0), ("Y", True)): 0.1,
            (("X", 0), ("Y", False)): 0.9,
            (("X", 1), ("Y", True)): 0.8,
            (("X", 1), ("Y", False)): 0.2,
        }
    }
    
    # Join the two factors.
    joined_factor = joinFactors([factorA, factorB])
    
    print("Joined Factor from Question 2:")
    print("Unconditioned Variables:", joined_factor["unconditioned"])
    print("Conditioned Variables:", joined_factor["conditioned"])
    for assignment_key, probability in joined_factor["probability"].items():
        print(dict(assignment_key), "->", probability)
