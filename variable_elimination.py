# variable_elimination.py

from join_factors import joinFactors
from eliminate_variable import eliminate

def normalizeFactor(factor):
    """
    Normalize the factor so that the probabilities sum to 1.
    """
    total = sum(factor["probability"].values())
    if total == 0:
        return factor
    new_prob = {}
    for assignment_key, prob in factor["probability"].items():
        new_prob[assignment_key] = prob / total
    factor["probability"] = new_prob
    return factor

def variableElimination(factors, queryVariables, eliminationOrder):
    """
    Performs variable elimination to compute the distribution over query variables.
    
    Parameters:
      factors (list): A list of factors (each a dict with keys:
                      "unconditioned", "conditioned", "variableDomainsDict", 
                      and "probability").
      queryVariables (set): The set of variables for which we want the posterior.
      eliminationOrder (list): A list specifying the order in which to eliminate 
                               the hidden variables.
                               
    Returns:
      A new factor representing the normalized distribution over the query variables.
    """
    # Make a copy of the factors list to work on
    workingFactors = list(factors)
    
    # Iterate over each variable in the elimination order:
    for var in eliminationOrder:
        # Identify all factors that involve the variable (either in unconditioned or conditioned)
        factorsToJoin = [factor for factor in workingFactors if var in factor["unconditioned"] or var in factor["conditioned"]]
        # Remove these factors from workingFactors
        workingFactors = [factor for factor in workingFactors if factor not in factorsToJoin]
        
        # If there are factors to join, combine them and then eliminate the variable.
        if factorsToJoin:
            joinedFactor = joinFactors(factorsToJoin)
            eliminatedFactor = eliminate(joinedFactor, var)
            workingFactors.append(eliminatedFactor)
    
    # Once all hidden variables have been eliminated, join any remaining factors.
    if len(workingFactors) > 0:
        finalFactor = joinFactors(workingFactors)
    else:
        finalFactor = None

    # The final factor might include extra variables. In a more sophisticated implementation,
    # you could project out only the query variables.
    # Finally, normalize the factor so that its probabilities sum to 1.
    normalizedFactor = normalizeFactor(finalFactor)
    return normalizedFactor


# -------------------- Test Harness for Question 4 --------------------
if __name__ == '__main__':
    # Example test: using similar factors as in Question 2.
    # We define a simple Bayes net with variables "X" and "Y",
    # where Factor A is P(X) and Factor B is P(Y|X).
    variableDomainsDict = {
        "X": [0, 1],
        "Y": [True, False]
    }
    
    # Factor A: Unconditioned over X.
    factorA = {
        "unconditioned": {"X"},
        "conditioned": set(),
        "variableDomainsDict": variableDomainsDict,
        "probability": {
            (("X", 0),): 0.3,
            (("X", 1),): 0.7,
        }
    }
    
    # Factor B: Y is unconditioned given X is conditioned.
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
    
    # Our factors list consists of Factor A and Factor B.
    factors = [factorA, factorB]
    
    # We want the posterior distribution over variable Y.
    queryVariables = {"Y"}
    # Eliminate hidden variable X.
    eliminationOrder = ["X"]
    
    resultFactor = variableElimination(factors, queryVariables, eliminationOrder)
    
    print("=== Variable Elimination Result ===")
    print("Unconditioned Variables:", resultFactor["unconditioned"])
    print("Conditioned Variables:", resultFactor["conditioned"])
    print("Probability Table:")
    for assignment_key, prob in resultFactor["probability"].items():
        print(dict(assignment_key), "->", prob)
