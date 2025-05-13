# # main.py

# from inference_q1 import constructBayesNet

# def main():
#     # Define a simple grid. For instance, a 3x3 grid.
#     legalPositions = [(x, y) for x in range(3) for y in range(3)]
#     # Maximum Manhattan distance on a 3x3 grid is 4.
#     maxDistance = 4

#     # Build the Bayes net.
#     net = constructBayesNet(legalPositions, maxDistance)

#     # Print the structure to verify.
#     print(net)

# if __name__ == '__main__':
#     main()

# main.py

# # Import the function for Question 1.
# from inference_q1 import constructBayesNet
# # Import the joinFactors function for Question 2.
# from join_factors import joinFactors
# # Import the eliminate function for Question 3.
# from eliminate_variable import eliminate

# def run_q1():
#     print("=== Question 1: Construct BayesNet ===")
#     # For example, use a simple 3x3 grid and maxDistance of 4.
#     legalPositions = [(x, y) for x in range(3) for y in range(3)]
#     maxDistance = 4
#     bayes_net = constructBayesNet(legalPositions, maxDistance)
#     print("BayesNet structure:")
#     print(bayes_net)  # This calls the BayesNet class's __str__ method.

# def run_q2():
#     print("\n=== Question 2: Join Factors ===")
#     # Example variable domains.
#     variableDomainsDict = {
#         "X": [0, 1],
#         "Y": [True, False]
#     }
#     # Define Factor A over variable X.
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7,
#         }
#     }
#     # Define Factor B over variable Y conditioned on X.
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2,
#         }
#     }
#     joined_factor = joinFactors([factorA, factorB])
#     print("Joined Factor:")
#     print("Unconditioned Variables:", joined_factor["unconditioned"])
#     print("Conditioned Variables:", joined_factor["conditioned"])
#     for assignment_key, prob in joined_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)

# def run_q3():
#     print("\n=== Question 3: Eliminate Variable ===")
#     # Define a sample factor over X and Y.
#     variableDomainsDict = {
#         "X": [0, 1],
#         "Y": [True, False]
#     }
#     factor = {
#         "unconditioned": {"X", "Y"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.2,
#             (("X", 0), ("Y", False)): 0.3,
#             (("X", 1), ("Y", True)): 0.4,
#             (("X", 1), ("Y", False)): 0.1,
#         }
#     }
#     # Eliminate variable Y from the factor.
#     eliminated_factor = eliminate(factor, "Y")
#     print("Factor after eliminating 'Y':")
#     print("Unconditioned Variables:", eliminated_factor["unconditioned"])
#     print("Conditioned Variables:", eliminated_factor["conditioned"])
#     print("Probability Table:")
#     for assignment_key, prob in eliminated_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)

# def main():
#     run_q1()
#     run_q2()
#     run_q3()

# if __name__ == '__main__':
#     main()




# main.py

# # Import functions for each question:
# from inference_q1 import constructBayesNet  # Question 1
# from join_factors import joinFactors         # Question 2
# from eliminate_variable import eliminate      # Question 3
# from variable_elimination import variableElimination  # Question 4

# def run_q1():
#     print("=== Question 1: Construct BayesNet ===")
#     # Set up a simple 3x3 grid as the legal positions for Pacman and Ghosts.
#     legalPositions = [(x, y) for x in range(3) for y in range(3)]
#     maxDistance = 4  # Maximum Manhattan distance (for a 3x3 grid, 4 is reasonable).
#     bayes_net = constructBayesNet(legalPositions, maxDistance)
#     print("BayesNet structure (Q1):")
#     print(bayes_net)  # Assuming BayesNet's __str__ prints variables, domains, and parents.

# def run_q2():
#     print("\n=== Question 2: Join Factors ===")
#     # Create an example with two factors similar to a typical join.
#     variableDomainsDict = {
#         "X": [0, 1],
#         "Y": [True, False]
#     }
    
#     # Factor A: Factor over X.
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7
#         }
#     }
    
#     # Factor B: Factor over Y given X.
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2
#         }
#     }
    
#     joined_factor = joinFactors([factorA, factorB])
#     print("Joined Factor from Q2:")
#     print("Unconditioned Variables:", joined_factor["unconditioned"])
#     print("Conditioned Variables:", joined_factor["conditioned"])
#     for assignment_key, prob in joined_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)

# def run_q3():
#     print("\n=== Question 3: Eliminate Variable ===")
#     # Define a simple factor over two variables X and Y.
#     variableDomainsDict = {
#         "X": [0, 1],
#         "Y": [True, False]
#     }
#     factor = {
#         "unconditioned": {"X", "Y"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.2,
#             (("X", 0), ("Y", False)): 0.3,
#             (("X", 1), ("Y", True)): 0.4,
#             (("X", 1), ("Y", False)): 0.1
#         }
#     }
#     # Eliminate variable 'Y'.
#     eliminated_factor = eliminate(factor, "Y")
#     print("Factor after eliminating 'Y' (Q3):")
#     print("Unconditioned Variables:", eliminated_factor["unconditioned"])
#     print("Conditioned Variables:", eliminated_factor["conditioned"])
#     print("Probability Table:")
#     for assignment_key, prob in eliminated_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)

# def run_q4():
#     print("\n=== Question 4: Variable Elimination ===")
#     # Use the same example as Q2 to perform variable elimination.
#     variableDomainsDict = {
#         "X": [0, 1],
#         "Y": [True, False]
#     }
#     # Factor A: P(X)
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7
#         }
#     }
#     # Factor B: P(Y|X)
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2
#         }
#     }
    
#     factors = [factorA, factorB]
#     # In this example, our query is the distribution for Y,
#     # and we eliminate hidden variable X.
#     queryVariables = {"Y"}
#     eliminationOrder = ["X"]
    
#     resultFactor = variableElimination(factors, queryVariables, eliminationOrder)
    
#     print("Variable Elimination Result (Q4):")
#     print("Unconditioned Variables:", resultFactor["unconditioned"])
#     print("Conditioned Variables:", resultFactor["conditioned"])
#     print("Probability Table:")
#     for assignment_key, prob in resultFactor["probability"].items():
#         print(dict(assignment_key), "->", prob)

# def main():
#     run_q1()
#     run_q2()
#     run_q3()
#     run_q4()

# if __name__ == '__main__':
#     main()





# main.py

# --- Import functions from our separate modules for each question ---


# main.py

# import os

# # --- Import functions for Questions 1-4 ---
# from inference_q1 import constructBayesNet       # Q1
# from join_factors import joinFactors              # Q2
# from eliminate_variable import eliminate           # Q3
# from variable_elimination import variableElimination  # Q4

# # --- Import visualization helpers ---
# from visualize_game import draw_game_board, draw_bayes_net_structure
# from visualize_factors import visualize_factor
# from visualize_elimination import visualize_eliminated_factor
# from visualize_var_elimination import visualize_var_elim_factor

# # --- Import functions for Question 5 ---
# from discrete_distribution import DiscreteDistribution  # Q5a
# from noisy_observations import getObservationProb, manhattanDistance  # Q5b

# def run_q1():
#     print("=== Question 1: Construct BayesNet ===")
#     legalPositions = [(x, y) for x in range(3) for y in range(3)]
#     maxDistance = 4
#     bayes_net = constructBayesNet(legalPositions, maxDistance)
#     print("BayesNet structure (Q1):")
#     print(bayes_net)
#     # Save visualizations for Q1:
#     draw_bayes_net_structure(bayes_net, filename="visualizations/bayes_net_structure_q1.png")
#     pacmanPos = (1, 1)
#     ghostPositions = {"ghost1": (0, 0), "ghost2": (2, 2)}
#     draw_game_board(legalPositions, pacmanPos, ghostPositions, filename="visualizations/game_board_q1.png")

# def run_q2():
#     print("\n=== Question 2: Join Factors ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7,
#         }
#     }
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2,
#         }
#     }
#     joined_factor = joinFactors([factorA, factorB])
#     print("Joined Factor from Q2:")
#     print("Unconditioned Variables:", joined_factor["unconditioned"])
#     print("Conditioned Variables:", joined_factor["conditioned"])
#     for assignment_key, prob in joined_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     # Save visualization:
#     visualize_factor(joined_factor, title="Joined Factor (Q2)", filename="visualizations/joined_factor_q2.png")

# def run_q3():
#     print("\n=== Question 3: Eliminate Variable ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factor = {
#         "unconditioned": {"X", "Y"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.2,
#             (("X", 0), ("Y", False)): 0.3,
#             (("X", 1), ("Y", True)): 0.4,
#             (("X", 1), ("Y", False)): 0.1,
#         }
#     }
#     eliminated_factor = eliminate(factor, "Y")
#     print("Factor after eliminating 'Y' (Q3):")
#     print("Unconditioned Variables:", eliminated_factor["unconditioned"])
#     print("Conditioned Variables:", eliminated_factor["conditioned"])
#     for assignment_key, prob in eliminated_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     # Save visualization for Q3:
#     visualize_eliminated_factor(eliminated_factor)

# def run_q4():
#     print("\n=== Question 4: Variable Elimination ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7,
#         }
#     }
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2,
#         }
#     }
#     factors = [factorA, factorB]
#     queryVariables = {"Y"}
#     eliminationOrder = ["X"]
#     resultFactor = variableElimination(factors, queryVariables, eliminationOrder)
#     print("Variable Elimination Result (Q4):")
#     print("Unconditioned Variables:", resultFactor["unconditioned"])
#     print("Conditioned Variables:", resultFactor["conditioned"])
#     for assignment_key, prob in resultFactor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     # Save visualization for Q4:
#     visualize_var_elim_factor(resultFactor)

# def run_q5():
#     print("\n=== Question 5: Discrete Distributions and Noisy Observations ===")
#     # --- Q5a: Test DiscreteDistribution ---
#     print("Testing DiscreteDistribution...")
#     dd = DiscreteDistribution({'a': 2, 'b': 3, 'c': 5})
#     print("Before normalization:", dd)
#     dd.normalize()
#     print("After normalization:", dd)
#     sample = dd.sample()
#     print("Sampled element:", sample)

#     # --- Q5b: Test getObservationProb ---
#     print("\nTesting getObservationProb for noisy observations:")
#     pacmanPos = (2, 3)
#     ghostPos = (4, 5)
#     jailPos = (0, 0)
#     trueDistance = manhattanDistance(pacmanPos, ghostPos)
#     print("True Manhattan distance between Pacman and ghost:", trueDistance)
#     print("\nNoisy observations for a ghost not in jail:")
#     for noisy in range(trueDistance - 2, trueDistance + 3):
#         prob = getObservationProb(noisy, pacmanPos, ghostPos, jailPos)
#         print(f"P(noisyDistance={noisy}) = {prob}")
    
#     print("\nTesting ghost in jail:")
#     prob_jail_none = getObservationProb(None, pacmanPos, jailPos, jailPos)
#     prob_jail_value = getObservationProb(5, pacmanPos, jailPos, jailPos)
#     print(f"Ghost in jail, observation None: {prob_jail_none}")
#     print(f"Ghost in jail, observation 5: {prob_jail_value}")

# def main():
#     os.makedirs("visualizations", exist_ok=True)
#     run_q1()
#     run_q2()
#     run_q3()
#     run_q4()
#     run_q5()

# if __name__ == '__main__':
#     main()


# main.py

# import os

# # --- Import functions for Questions 1-5 (assuming these have been implemented) ---
# from inference_q1 import constructBayesNet       # Q1
# from join_factors import joinFactors              # Q2
# from eliminate_variable import eliminate           # Q3
# from variable_elimination import variableElimination  # Q4
# from discrete_distribution import DiscreteDistribution  # Q5a
# from noisy_observations import getObservationProb, manhattanDistance  # Q5b

# # --- Import visualization helpers for Q1-Q5 ---
# from visualize_game import draw_game_board, draw_bayes_net_structure
# from visualize_factors import visualize_factor
# from visualize_elimination import visualize_eliminated_factor
# from visualize_var_elimination import visualize_var_elim_factor

# # --- Import modules for Question 6 ---
# from observation_update import observeUpdate
# from visualize_beliefs import visualize_belief_distribution

# def run_q1():
#     print("=== Question 1: Construct BayesNet ===")
#     legalPositions = [(x, y) for x in range(3) for y in range(3)]
#     maxDistance = 4
#     bayes_net = constructBayesNet(legalPositions, maxDistance)
#     print("BayesNet structure (Q1):")
#     print(bayes_net)
#     draw_bayes_net_structure(bayes_net, filename="visualizations/bayes_net_structure_q1.png")
#     pacmanPos = (1, 1)
#     ghostPositions = {"ghost1": (0, 0), "ghost2": (2, 2)}
#     draw_game_board(legalPositions, pacmanPos, ghostPositions, filename="visualizations/game_board_q1.png")

# def run_q2():
#     print("\n=== Question 2: Join Factors ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7,
#         }
#     }
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2,
#         }
#     }
#     joined_factor = joinFactors([factorA, factorB])
#     print("Joined Factor from Q2:")
#     print("Unconditioned Variables:", joined_factor["unconditioned"])
#     print("Conditioned Variables:", joined_factor["conditioned"])
#     for assignment_key, prob in joined_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     visualize_factor(joined_factor, title="Joined Factor (Q2)", filename="visualizations/joined_factor_q2.png")

# def run_q3():
#     print("\n=== Question 3: Eliminate Variable ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factor = {
#         "unconditioned": {"X", "Y"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.2,
#             (("X", 0), ("Y", False)): 0.3,
#             (("X", 1), ("Y", True)): 0.4,
#             (("X", 1), ("Y", False)): 0.1,
#         }
#     }
#     eliminated_factor = eliminate(factor, "Y")
#     print("Factor after eliminating 'Y' (Q3):")
#     print("Unconditioned Variables:", eliminated_factor["unconditioned"])
#     print("Conditioned Variables:", eliminated_factor["conditioned"])
#     for assignment_key, prob in eliminated_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     visualize_eliminated_factor(eliminated_factor)

# def run_q4():
#     print("\n=== Question 4: Variable Elimination ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7,
#         }
#     }
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2,
#         }
#     }
#     factors = [factorA, factorB]
#     queryVariables = {"Y"}
#     eliminationOrder = ["X"]
#     resultFactor = variableElimination(factors, queryVariables, eliminationOrder)
#     print("Variable Elimination Result (Q4):")
#     print("Unconditioned Variables:", resultFactor["unconditioned"])
#     print("Conditioned Variables:", resultFactor["conditioned"])
#     for assignment_key, prob in resultFactor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     visualize_var_elim_factor(resultFactor)

# def run_q5():
#     print("\n=== Question 5: Discrete Distributions and Noisy Observations ===")
#     # Q5a: Test DiscreteDistribution
#     print("Testing DiscreteDistribution...")
#     dd = DiscreteDistribution({'a': 2, 'b': 3, 'c': 5})
#     print("Before normalization:", dd)
#     dd.normalize()
#     print("After normalization:", dd)
#     print("Sampled element:", dd.sample())

#     # Q5b: Test getObservationProb
#     from noisy_observations import getObservationProb, manhattanDistance
#     print("\nTesting getObservationProb for noisy observations:")
#     pacmanPos = (2, 3)
#     ghostPos = (4, 5)
#     jailPos = (0, 0)
#     trueDistance = manhattanDistance(pacmanPos, ghostPos)
#     print("True Manhattan distance:", trueDistance)
#     for noisy in range(trueDistance - 2, trueDistance + 3):
#         prob = getObservationProb(noisy, pacmanPos, ghostPos, jailPos)
#         print(f"P(noisyDistance={noisy}) = {prob}")
#     print("\nTesting ghost in jail:")
#     print("Ghost in jail, observation None:", getObservationProb(None, pacmanPos, jailPos, jailPos))
#     print("Ghost in jail, observation 5:", getObservationProb(5, pacmanPos, jailPos, jailPos))

# def run_q6():
#     print("\n=== Question 6: Exact Inference - Observation Update ===")
#     # Create a uniform belief distribution over ghost positions on a 5x5 grid.
#     from discrete_distribution import DiscreteDistribution
#     legalPositions = [(x, y) for x in range(5) for y in range(5)]
#     beliefs = DiscreteDistribution()
#     for pos in legalPositions:
#         beliefs[pos] = 1.0
#     beliefs.normalize()
#     print("Initial uniform belief distribution:")
#     for pos, p in beliefs.items():
#         print(f"{pos}: {p}")
    
#     # Specify parameters for the observation update.
#     pacmanPos = (2, 2)
#     jailPos = (0, 0)  # Assume ghost jail is at (0,0)
#     noisyDistance = 2  # Sample noisy observation
#     # Update the beliefs based on the observation.
#     updatedBeliefs = observeUpdate(beliefs, noisyDistance, pacmanPos, jailPos)
#     print("\nUpdated beliefs after observing noisyDistance =", noisyDistance)
#     for pos, p in updatedBeliefs.items():
#         print(f"{pos}: {p}")
    
#     # Visualize the updated belief distribution as a heatmap.
#     # We assume grid shape is 5x5.
#     visualize_belief_distribution(updatedBeliefs, gridShape=(5,5), filename="visualizations/beliefs_q6.png", title="Belief Distribution after Observation (Q6)")


# def main():
#     os.makedirs("visualizations", exist_ok=True)
#     run_q1()
#     run_q2()
#     run_q3()
#     run_q4()
#     run_q5()
#     run_q6()

# if __name__ == '__main__':
#     main()

# main.py

# import os

# # --- Import functions for Questions 1-6 (already implemented) ---
# from inference_q1 import constructBayesNet       # Q1
# from join_factors import joinFactors              # Q2
# from eliminate_variable import eliminate           # Q3
# from variable_elimination import variableElimination  # Q4
# from discrete_distribution import DiscreteDistribution  # Q5a
# from noisy_observations import getObservationProb, manhattanDistance  # Q5b
# from observation_update import observeUpdate        # Q6

# # --- Import visualization helpers ---
# from visualize_game import draw_game_board, draw_bayes_net_structure
# from visualize_factors import visualize_factor
# from visualize_elimination import visualize_eliminated_factor
# from visualize_var_elimination import visualize_var_elim_factor
# from visualize_beliefs import visualize_belief_distribution

# # --- Import module for Question 7 ---
# from elapse_time import elapseTime

# def run_q1():
#     # [Implementation for Question 1...]
#     pass  # assume already implemented

# def run_q2():
#     # [Implementation for Question 2...]
#     pass

# def run_q3():
#     # [Implementation for Question 3...]
#     pass

# def run_q4():
#     # [Implementation for Question 4...]
#     pass

# def run_q5():
#     # [Implementation for Question 5...]
#     pass

# def run_q6():
#     # [Implementation for Question 6...]
#     pass

# def run_q7():
#     print("\n=== Question 7: Exact Inference - Time Elapse ===")
#     # Assume a grid of size 5x5 (for the ghost positions)
#     legalPositions = [(x, y) for x in range(5) for y in range(5)]
    
#     # Create a uniform belief distribution over ghost positions.
#     beliefs = DiscreteDistribution()
#     for pos in legalPositions:
#         beliefs[pos] = 1.0
#     beliefs.normalize()
    
#     print("Initial uniform beliefs:")
#     for pos, p in sorted(beliefs.items()):
#         print(f"{pos}: {p:.3f}")
    
#     # Update beliefs for time elapse using the transition model.
#     updatedBeliefs = elapseTime(beliefs, legalPositions)
    
#     print("\nBeliefs after time elapse:")
#     for pos, p in sorted(updatedBeliefs.items()):
#         print(f"{pos}: {p:.3f}")
    
#     # Visualize the updated belief distribution as a heatmap.
#     visualize_belief_distribution(updatedBeliefs,
#                                   gridShape=(5, 5),
#                                   filename="visualizations/beliefs_q7.png",
#                                   title="Belief Distribution after Time Elapse (Q7)")

# def main():
#     os.makedirs("visualizations", exist_ok=True)
#     run_q1()
#     run_q2()
#     run_q3()
#     run_q4()
#     run_q5()
#     run_q6()
#     run_q7()

# if __name__ == '__main__':
#     main()


# main.py

# import os

# # --- Import functions for Questions 1-6 (already implemented) ---
# from inference_q1 import constructBayesNet       # Q1
# from join_factors import joinFactors              # Q2
# from eliminate_variable import eliminate           # Q3
# from variable_elimination import variableElimination  # Q4
# from discrete_distribution import DiscreteDistribution  # Q5a
# from noisy_observations import getObservationProb, manhattanDistance  # Q5b
# from observation_update import observeUpdate        # Q6

# # --- Import visualization helpers ---
# from visualize_game import draw_game_board, draw_bayes_net_structure
# from visualize_factors import visualize_factor
# from visualize_elimination import visualize_eliminated_factor
# from visualize_var_elimination import visualize_var_elim_factor
# from visualize_beliefs import visualize_belief_distribution

# # --- Import module for Question 7 ---
# from elapse_time import elapseTime

# def run_q7():
#     print("\n=== Question 7: Exact Inference - Time Elapse ===")
    
#     # Define a 5x5 grid of legal positions; these represent possible ghost positions.
#     legalPositions = [(x, y) for x in range(5) for y in range(5)]
    
#     # Create an initial uniform belief distribution over ghost positions.
#     beliefs = DiscreteDistribution()
#     for pos in legalPositions:
#         beliefs[pos] = 1.0
#     beliefs.normalize()
    
#     print("Initial uniform beliefs:")
#     for pos, p in sorted(beliefs.items()):
#         print(f"{pos}: {p:.3f}")
    
#     # Update beliefs to reflect ghost motion (time elapse).
#     updatedBeliefs = elapseTime(beliefs, legalPositions)
    
#     print("\nBeliefs after time elapse (should shift toward the bottom due to GoSouth bias):")
#     for pos, p in sorted(updatedBeliefs.items()):
#         print(f"{pos}: {p:.3f}")
    
#     # Visualize the updated belief distribution as a heatmap.
#     visualize_belief_distribution(updatedBeliefs,
#                                   gridShape=(5, 5),
#                                   filename="visualizations/beliefs_q7.png",
#                                   title="Belief Distribution after Time Elapse (Q7)")

# def main():
#     os.makedirs("visualizations", exist_ok=True)
#     # ... run previous questions functions: run_q1(), run_q2(), ..., run_q6()
#     run_q7()

# if __name__ == '__main__':
#     main()



# main.py

# import os

# # --- Import functions for Questions 1-4 ---
# from inference_q1 import constructBayesNet       # Q1
# from join_factors import joinFactors              # Q2
# from eliminate_variable import eliminate           # Q3
# from variable_elimination import variableElimination  # Q4

# # --- Import functions for Question 5 ---
# from discrete_distribution import DiscreteDistribution  # Q5a
# from noisy_observations import getObservationProb, manhattanDistance  # Q5b

# # --- Import functions for Question 6 ---
# from observation_update import observeUpdate        # Q6

# # --- Import functions for Question 7 ---
# from elapse_time import elapseTime

# # --- Import visualization helpers ---
# from visualize_game import draw_game_board, draw_bayes_net_structure
# from visualize_factors import visualize_factor
# from visualize_elimination import visualize_eliminated_factor
# from visualize_var_elimination import visualize_var_elim_factor
# from visualize_beliefs import visualize_belief_distribution

# def run_q1():
#     print("=== Question 1: Construct BayesNet ===")
#     legalPositions = [(x, y) for x in range(3) for y in range(3)]
#     maxDistance = 4
#     bayes_net = constructBayesNet(legalPositions, maxDistance)
#     print("BayesNet structure (Q1):")
#     print(bayes_net)
#     # Save the Bayes net structure and game board as PNG images.
#     draw_bayes_net_structure(bayes_net, filename="visualizations/bayes_net_structure_q1.png")
#     pacmanPos = (1, 1)
#     ghostPositions = {"ghost1": (0, 0), "ghost2": (2, 2)}
#     draw_game_board(legalPositions, pacmanPos, ghostPositions, filename="visualizations/game_board_q1.png")

# def run_q2():
#     print("\n=== Question 2: Join Factors ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7,
#         }
#     }
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2,
#         }
#     }
#     joined_factor = joinFactors([factorA, factorB])
#     print("Joined Factor from Q2:")
#     print("Unconditioned Variables:", joined_factor["unconditioned"])
#     print("Conditioned Variables:", joined_factor["conditioned"])
#     for assignment_key, prob in joined_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     visualize_factor(joined_factor, title="Joined Factor (Q2)", filename="visualizations/joined_factor_q2.png")

# def run_q3():
#     print("\n=== Question 3: Eliminate Variable ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factor = {
#         "unconditioned": {"X", "Y"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.2,
#             (("X", 0), ("Y", False)): 0.3,
#             (("X", 1), ("Y", True)): 0.4,
#             (("X", 1), ("Y", False)): 0.1,
#         }
#     }
#     eliminated_factor = eliminate(factor, "Y")
#     print("Factor after eliminating 'Y' (Q3):")
#     print("Unconditioned Variables:", eliminated_factor["unconditioned"])
#     print("Conditioned Variables:", eliminated_factor["conditioned"])
#     for assignment_key, prob in eliminated_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     visualize_eliminated_factor(eliminated_factor, filename="visualizations/eliminated_factor_q3.png")

# def run_q4():
#     print("\n=== Question 4: Variable Elimination ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7,
#         }
#     }
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2,
#         }
#     }
#     factors = [factorA, factorB]
#     queryVariables = {"Y"}
#     eliminationOrder = ["X"]
#     resultFactor = variableElimination(factors, queryVariables, eliminationOrder)
#     print("Variable Elimination Result (Q4):")
#     print("Unconditioned Variables:", resultFactor["unconditioned"])
#     print("Conditioned Variables:", resultFactor["conditioned"])
#     for assignment_key, prob in resultFactor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     visualize_var_elim_factor(resultFactor, filename="visualizations/var_elim_result_q4.png")

# def run_q5():
#     print("\n=== Question 5: Discrete Distributions and Noisy Observations ===")
#     # Q5a: Test DiscreteDistribution
#     print("Testing DiscreteDistribution...")
#     dd = DiscreteDistribution({'a': 2, 'b': 3, 'c': 5})
#     print("Before normalization:", dd)
#     dd.normalize()
#     print("After normalization:", dd)
#     print("Sampled element:", dd.sample())
#     # Q5b: Test getObservationProb
#     from noisy_observations import getObservationProb, manhattanDistance
#     print("\nTesting getObservationProb for noisy observations:")
#     pacmanPos = (2, 3)
#     ghostPos = (4, 5)
#     jailPos = (0, 0)
#     trueDistance = manhattanDistance(pacmanPos, ghostPos)
#     print("True Manhattan distance:", trueDistance)
#     for noisy in range(trueDistance - 2, trueDistance + 3):
#         prob = getObservationProb(noisy, pacmanPos, ghostPos, jailPos)
#         print(f"P(noisyDistance={noisy}) = {prob}")
#     print("\nTesting ghost in jail:")
#     print("Ghost in jail, observation None:", getObservationProb(None, pacmanPos, jailPos, jailPos))
#     print("Ghost in jail, observation 5:", getObservationProb(5, pacmanPos, jailPos, jailPos))

# def run_q6():
#     print("\n=== Question 6: Exact Inference - Observation Update ===")
#     from discrete_distribution import DiscreteDistribution
#     legalPositions = [(x, y) for x in range(5) for y in range(5)]
#     beliefs = DiscreteDistribution()
#     for pos in legalPositions:
#         beliefs[pos] = 1.0
#     beliefs.normalize()
#     print("Initial uniform belief distribution:")
#     for pos, p in beliefs.items():
#         print(f"{pos}: {p}")
#     pacmanPos = (2, 2)
#     jailPos = (0, 0)
#     noisyDistance = 2
#     updatedBeliefs = observeUpdate(beliefs, noisyDistance, pacmanPos, jailPos)
#     print("\nUpdated beliefs after observing noisyDistance =", noisyDistance)
#     for pos, p in updatedBeliefs.items():
#         print(f"{pos}: {p}")
#     visualize_belief_distribution(updatedBeliefs, gridShape=(5, 5),
#                                   filename="visualizations/beliefs_q6.png",
#                                   title="Belief Distribution after Observation (Q6)")

# def run_q7():
#     print("\n=== Question 7: Exact Inference - Time Elapse ===")
#     from discrete_distribution import DiscreteDistribution
#     legalPositions = [(x, y) for x in range(5) for y in range(5)]
#     beliefs = DiscreteDistribution()
#     for pos in legalPositions:
#         beliefs[pos] = 1.0
#     beliefs.normalize()
#     print("Initial uniform beliefs:")
#     for pos, p in sorted(beliefs.items()):
#         print(f"{pos}: {p:.3f}")
#     updatedBeliefs = elapseTime(beliefs, legalPositions)
#     print("\nBeliefs after time elapse (should shift toward the bottom due to GoSouth bias):")
#     for pos, p in sorted(updatedBeliefs.items()):
#         print(f"{pos}: {p:.3f}")
#     visualize_belief_distribution(updatedBeliefs, gridShape=(5, 5),
#                                   filename="visualizations/beliefs_q7.png",
#                                   title="Belief Distribution after Time Elapse (Q7)")

# def main():
#     os.makedirs("visualizations", exist_ok=True)
#     run_q1()
#     run_q2()
#     run_q3()
#     run_q4()
#     run_q5()
#     run_q6()
#     run_q7()

# if __name__ == '__main__':
#     main()

# main.py

# import os

# # --- Import functions for Questions 1-4 ---
# from inference_q1 import constructBayesNet       # Q1
# from join_factors import joinFactors              # Q2
# from eliminate_variable import eliminate           # Q3
# from variable_elimination import variableElimination  # Q4

# # --- Import functions for Question 5 ---
# from discrete_distribution import DiscreteDistribution  # Q5a
# from noisy_observations import getObservationProb, manhattanDistance  # Q5b

# # --- Import functions for Question 6 ---
# from observation_update import observeUpdate        # Q6

# # --- Import functions for Question 7 ---
# from elapse_time import elapseTime

# # --- Import visualization helpers ---
# from visualize_game import draw_game_board, draw_bayes_net_structure
# from visualize_factors import visualize_factor
# from visualize_elimination import visualize_eliminated_factor
# from visualize_var_elimination import visualize_var_elim_factor
# from visualize_beliefs import visualize_belief_distribution

# # --- Import full inference test (Question 8) ---
# from full_inference_test import full_inference_test

# def run_q1():
#     print("=== Question 1: Construct BayesNet ===")
#     legalPositions = [(x, y) for x in range(3) for y in range(3)]
#     maxDistance = 4
#     bayes_net = constructBayesNet(legalPositions, maxDistance)
#     print("BayesNet structure (Q1):")
#     print(bayes_net)
#     draw_bayes_net_structure(bayes_net, filename="visualizations/bayes_net_structure_q1.png")
#     pacmanPos = (1, 1)
#     ghostPositions = {"ghost1": (0, 0), "ghost2": (2, 2)}
#     draw_game_board(legalPositions, pacmanPos, ghostPositions, filename="visualizations/game_board_q1.png")

# def run_q2():
#     print("\n=== Question 2: Join Factors ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7,
#         }
#     }
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2,
#         }
#     }
#     joined_factor = joinFactors([factorA, factorB])
#     print("Joined Factor from Q2:")
#     print("Unconditioned Variables:", joined_factor["unconditioned"])
#     print("Conditioned Variables:", joined_factor["conditioned"])
#     for assignment_key, prob in joined_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     visualize_factor(joined_factor, title="Joined Factor (Q2)", filename="visualizations/joined_factor_q2.png")

# def run_q3():
#     print("\n=== Question 3: Eliminate Variable ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factor = {
#         "unconditioned": {"X", "Y"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.2,
#             (("X", 0), ("Y", False)): 0.3,
#             (("X", 1), ("Y", True)): 0.4,
#             (("X", 1), ("Y", False)): 0.1,
#         }
#     }
#     eliminated_factor = eliminate(factor, "Y")
#     print("Factor after eliminating 'Y' (Q3):")
#     print("Unconditioned Variables:", eliminated_factor["unconditioned"])
#     print("Conditioned Variables:", eliminated_factor["conditioned"])
#     for assignment_key, prob in eliminated_factor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     visualize_eliminated_factor(eliminated_factor, filename="visualizations/eliminated_factor_q3.png")

# def run_q4():
#     print("\n=== Question 4: Variable Elimination ===")
#     variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
#     factorA = {
#         "unconditioned": {"X"},
#         "conditioned": set(),
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0),): 0.3,
#             (("X", 1),): 0.7,
#         }
#     }
#     factorB = {
#         "unconditioned": {"Y"},
#         "conditioned": {"X"},
#         "variableDomainsDict": variableDomainsDict,
#         "probability": {
#             (("X", 0), ("Y", True)): 0.1,
#             (("X", 0), ("Y", False)): 0.9,
#             (("X", 1), ("Y", True)): 0.8,
#             (("X", 1), ("Y", False)): 0.2,
#         }
#     }
#     factors = [factorA, factorB]
#     queryVariables = {"Y"}
#     eliminationOrder = ["X"]
#     resultFactor = variableElimination(factors, queryVariables, eliminationOrder)
#     print("Variable Elimination Result (Q4):")
#     print("Unconditioned Variables:", resultFactor["unconditioned"])
#     print("Conditioned Variables:", resultFactor["conditioned"])
#     for assignment_key, prob in resultFactor["probability"].items():
#         print(dict(assignment_key), "->", prob)
#     visualize_var_elim_factor(resultFactor, filename="visualizations/var_elim_result_q4.png")

# def run_q5():
#     print("\n=== Question 5: Discrete Distributions and Noisy Observations ===")
#     # Q5a: Test DiscreteDistribution
#     print("Testing DiscreteDistribution...")
#     dd = DiscreteDistribution({'a': 2, 'b': 3, 'c': 5})
#     print("Before normalization:", dd)
#     dd.normalize()
#     print("After normalization:", dd)
#     print("Sampled element:", dd.sample())
#     # Q5b: Test getObservationProb
#     from noisy_observations import getObservationProb, manhattanDistance
#     print("\nTesting getObservationProb for noisy observations:")
#     pacmanPos = (2, 3)
#     ghostPos = (4, 5)
#     jailPos = (0, 0)
#     trueDistance = manhattanDistance(pacmanPos, ghostPos)
#     print("True Manhattan distance:", trueDistance)
#     for noisy in range(trueDistance - 2, trueDistance + 3):
#         prob = getObservationProb(noisy, pacmanPos, ghostPos, jailPos)
#         print(f"P(noisyDistance={noisy}) = {prob}")
#     print("\nTesting ghost in jail:")
#     print("Ghost in jail, observation None:", getObservationProb(None, pacmanPos, jailPos, jailPos))
#     print("Ghost in jail, observation 5:", getObservationProb(5, pacmanPos, jailPos, jailPos))

# def run_q6():
#     print("\n=== Question 6: Exact Inference - Observation Update ===")
#     from discrete_distribution import DiscreteDistribution
#     legalPositions = [(x, y) for x in range(5) for y in range(5)]
#     beliefs = DiscreteDistribution()
#     for pos in legalPositions:
#         beliefs[pos] = 1.0
#     beliefs.normalize()
#     print("Initial uniform belief distribution:")
#     for pos, p in beliefs.items():
#         print(f"{pos}: {p}")
#     pacmanPos = (2, 2)
#     jailPos = (0, 0)
#     noisyDistance = 2
#     updatedBeliefs = observeUpdate(beliefs, noisyDistance, pacmanPos, jailPos)
#     print("\nUpdated beliefs after observing noisyDistance =", noisyDistance)
#     for pos, p in updatedBeliefs.items():
#         print(f"{pos}: {p}")
#     visualize_belief_distribution(updatedBeliefs, gridShape=(5, 5),
#                                   filename="visualizations/beliefs_q6.png",
#                                   title="Belief Distribution after Observation (Q6)")

# def run_q7():
#     print("\n=== Question 7: Exact Inference - Time Elapse ===")
#     from discrete_distribution import DiscreteDistribution
#     legalPositions = [(x, y) for x in range(5) for y in range(5)]
#     beliefs = DiscreteDistribution()
#     for pos in legalPositions:
#         beliefs[pos] = 1.0
#     beliefs.normalize()
#     print("Initial uniform beliefs:")
#     for pos, p in sorted(beliefs.items()):
#         print(f"{pos}: {p:.3f}")
#     updatedBeliefs = elapseTime(beliefs, legalPositions)
#     print("\nBeliefs after time elapse (should shift toward the bottom due to GoSouth bias):")
#     for pos, p in sorted(updatedBeliefs.items()):
#         print(f"{pos}: {p:.3f}")
#     visualize_belief_distribution(updatedBeliefs, gridShape=(5, 5),
#                                   filename="visualizations/beliefs_q7.png",
#                                   title="Belief Distribution after Time Elapse (Q7)")

# def main():
#     os.makedirs("visualizations", exist_ok=True)
#     run_q1()
#     run_q2()
#     run_q3()
#     run_q4()
#     run_q5()
#     run_q6()
#     run_q7()
#     print("\n=== Question 8: Full Inference Test ===")
#     full_inference_test()

# if __name__ == '__main__':
#     main()

# main.py


# main.py

import os

# --- Import functions for Questions 1-4 (Exact Inference) ---
from inference_q1 import constructBayesNet       # Q1
from join_factors import joinFactors              # Q2
from eliminate_variable import eliminate           # Q3
from variable_elimination import variableElimination  # Q4

# --- Import functions for Question 5 (Discrete Distribution & Noisy Observations) ---
from discrete_distribution import DiscreteDistribution  # Q5a
from noisy_observations import getObservationProb, manhattanDistance  # Q5b

# --- Import functions for Question 6 (Observation Update) ---
from observation_update import observeUpdate        # Q6

# --- Import functions for Question 7 (Time Elapse) ---
from elapse_time import elapseTime

# --- Import full inference test for Question 8 ---
from full_inference_test import full_inference_test  # Q8

# --- Import functions for Particle Filter (Questions 9, 10, 11) ---
from particle_filter import initializeUniformly, getBeliefDistribution, particleObserveUpdate, particleElapseTime

# --- Import visualization helpers ---
from visualize_game import draw_game_board, draw_bayes_net_structure
from visualize_factors import visualize_factor
from visualize_elimination import visualize_eliminated_factor
from visualize_var_elimination import visualize_var_elim_factor
from visualize_beliefs import visualize_belief_distribution

# ----------------------
# Question 1: Construct BayesNet
# ----------------------
def run_q1():
    print("=== Question 1: Construct BayesNet ===")
    legalPositions = [(x, y) for x in range(3) for y in range(3)]
    maxDistance = 4
    bayes_net = constructBayesNet(legalPositions, maxDistance)
    print("BayesNet structure (Q1):")
    print(bayes_net)
    draw_bayes_net_structure(bayes_net, filename="visualizations/bayes_net_structure_q1.png")
    pacmanPos = (1, 1)
    ghostPositions = {"ghost1": (0, 0), "ghost2": (2, 2)}
    draw_game_board(legalPositions, pacmanPos, ghostPositions, filename="visualizations/game_board_q1.png")

# ----------------------
# Question 2: Join Factors
# ----------------------
def run_q2():
    print("\n=== Question 2: Join Factors ===")
    variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
    factorA = {
        "unconditioned": {"X"},
        "conditioned": set(),
        "variableDomainsDict": variableDomainsDict,
        "probability": {
            (("X", 0),): 0.3,
            (("X", 1),): 0.7,
        }
    }
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
    joined_factor = joinFactors([factorA, factorB])
    print("Joined Factor from Q2:")
    print("Unconditioned Variables:", joined_factor["unconditioned"])
    print("Conditioned Variables:", joined_factor["conditioned"])
    for assignment_key, prob in joined_factor["probability"].items():
        print(dict(assignment_key), "->", prob)
    visualize_factor(joined_factor, title="Joined Factor (Q2)", filename="visualizations/joined_factor_q2.png")

# ----------------------
# Question 3: Eliminate Variable
# ----------------------
def run_q3():
    print("\n=== Question 3: Eliminate Variable ===")
    variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
    factor = {
        "unconditioned": {"X", "Y"},
        "conditioned": set(),
        "variableDomainsDict": variableDomainsDict,
        "probability": {
            (("X", 0), ("Y", True)): 0.2,
            (("X", 0), ("Y", False)): 0.3,
            (("X", 1), ("Y", True)): 0.4,
            (("X", 1), ("Y", False)): 0.1,
        }
    }
    eliminated_factor = eliminate(factor, "Y")
    print("Factor after eliminating 'Y' (Q3):")
    print("Unconditioned Variables:", eliminated_factor["unconditioned"])
    print("Conditioned Variables:", eliminated_factor["conditioned"])
    for assignment_key, prob in eliminated_factor["probability"].items():
        print(dict(assignment_key), "->", prob)
    visualize_eliminated_factor(eliminated_factor, filename="visualizations/eliminated_factor_q3.png")

# ----------------------
# Question 4: Variable Elimination
# ----------------------
def run_q4():
    print("\n=== Question 4: Variable Elimination ===")
    variableDomainsDict = {"X": [0, 1], "Y": [True, False]}
    factorA = {
        "unconditioned": {"X"},
        "conditioned": set(),
        "variableDomainsDict": variableDomainsDict,
        "probability": {
            (("X", 0),): 0.3,
            (("X", 1),): 0.7,
        }
    }
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
    factors = [factorA, factorB]
    queryVariables = {"Y"}
    eliminationOrder = ["X"]
    resultFactor = variableElimination(factors, queryVariables, eliminationOrder)
    print("Variable Elimination Result (Q4):")
    print("Unconditioned Variables:", resultFactor["unconditioned"])
    print("Conditioned Variables:", resultFactor["conditioned"])
    for assignment_key, prob in resultFactor["probability"].items():
        print(dict(assignment_key), "->", prob)
    visualize_var_elim_factor(resultFactor, filename="visualizations/var_elim_result_q4.png")

# ----------------------
# Question 5: Discrete Distributions and Noisy Observations
# ----------------------
def run_q5():
    print("\n=== Question 5: Discrete Distributions and Noisy Observations ===")
    # Q5a: Test DiscreteDistribution
    print("Testing DiscreteDistribution...")
    dd = DiscreteDistribution({'a': 2, 'b': 3, 'c': 5})
    print("Before normalization:", dd)
    dd.normalize()
    print("After normalization:", dd)
    print("Sampled element:", dd.sample())
    # Q5b: Test getObservationProb
    from noisy_observations import getObservationProb, manhattanDistance
    print("\nTesting getObservationProb for noisy observations:")
    pacmanPos = (2, 3)
    ghostPos = (4, 5)
    jailPos = (0, 0)
    trueDistance = manhattanDistance(pacmanPos, ghostPos)
    print("True Manhattan distance:", trueDistance)
    for noisy in range(trueDistance - 2, trueDistance + 3):
        prob = getObservationProb(noisy, pacmanPos, ghostPos, jailPos)
        print(f"P(noisyDistance={noisy}) = {prob}")
    print("\nTesting ghost in jail:")
    print("Ghost in jail, observation None:", getObservationProb(None, pacmanPos, jailPos, jailPos))
    print("Ghost in jail, observation 5:", getObservationProb(5, pacmanPos, jailPos, jailPos))

# ----------------------
# Question 6: Exact Inference - Observation Update
# ----------------------
def run_q6():
    print("\n=== Question 6: Exact Inference - Observation Update ===")
    from discrete_distribution import DiscreteDistribution
    legalPositions = [(x, y) for x in range(5) for y in range(5)]
    beliefs = DiscreteDistribution()
    for pos in legalPositions:
        beliefs[pos] = 1.0
    beliefs.normalize()
    print("Initial uniform belief distribution:")
    for pos, p in beliefs.items():
        print(f"{pos}: {p}")
    pacmanPos = (2, 2)
    jailPos = (0, 0)
    noisyDistance = 2
    updatedBeliefs = observeUpdate(beliefs, noisyDistance, pacmanPos, jailPos)
    print("\nUpdated beliefs after observing noisyDistance =", noisyDistance)
    for pos, p in updatedBeliefs.items():
        print(f"{pos}: {p}")
    visualize_belief_distribution(updatedBeliefs, gridShape=(5, 5),
                                  filename="visualizations/beliefs_q6.png",
                                  title="Belief Distribution after Observation (Q6)")

# ----------------------
# Question 7: Exact Inference - Time Elapse
# ----------------------
def run_q7():
    print("\n=== Question 7: Exact Inference - Time Elapse ===")
    from discrete_distribution import DiscreteDistribution
    legalPositions = [(x, y) for x in range(5) for y in range(5)]
    beliefs = DiscreteDistribution()
    for pos in legalPositions:
        beliefs[pos] = 1.0
    beliefs.normalize()
    print("Initial uniform beliefs:")
    for pos, p in sorted(beliefs.items()):
        print(f"{pos}: {p:.3f}")
    updatedBeliefs = elapseTime(beliefs, legalPositions)
    print("\nBeliefs after time elapse (should shift toward the bottom due to GoSouth bias):")
    for pos, p in sorted(updatedBeliefs.items()):
        print(f"{pos}: {p:.3f}")
    visualize_belief_distribution(updatedBeliefs, gridShape=(5, 5),
                                  filename="visualizations/beliefs_q7.png",
                                  title="Belief Distribution after Time Elapse (Q7)")

# ----------------------
# Question 8: Full Inference Test
# ----------------------
def run_q8():
    print("\n=== Question 8: Full Inference Test ===")
    full_inference_test()

# ----------------------
# Question 9: Particle Filter - Initialization (and Particle Filter Q10 and Q11)
# ----------------------
def run_q9():
    print("\n=== Question 9: Particle Filter - Initialization ===")
    legalPositions = [(x, y) for x in range(5) for y in range(5)]
    numParticles = 500
    particles = initializeUniformly(legalPositions, numParticles)
    print("First 10 particles:", particles[:10])
    beliefDistribution = getBeliefDistribution(particles)
    print("Belief distribution (from particles):")
    for pos, prob in sorted(beliefDistribution.items()):
        print(f"{pos}: {prob:.3f}")
    visualize_belief_distribution(beliefDistribution,
                                  gridShape=(5, 5),
                                  filename="visualizations/particle_beliefs_q9.png",
                                  title="Particle Filter Belief Distribution (Q9)")

def run_q10():
    print("\n=== Question 10: Particle Filter - Observation Update ===")
    legalPositions = [(x, y) for x in range(5) for y in range(5)]
    numParticles = 500
    particles = initializeUniformly(legalPositions, numParticles)
    print("Initial particles (first 10):", particles[:10])
    pacmanPos = (2, 2)
    jailPos = (0, 0)
    noisyDistance = 2
    particles_updated = particleObserveUpdate(particles, noisyDistance, pacmanPos, jailPos, legalPositions, numParticles)
    print("Particles after observation update (first 10):", particles_updated[:10])
    beliefParticles = getBeliefDistribution(particles_updated)
    visualize_belief_distribution(beliefParticles, gridShape=(5, 5),
                                  filename="visualizations/particle_obs_update_q10.png",
                                  title="Particle Filter Belief (Observation Update Q10)")

def run_q11():
    print("\n=== Question 11: Particle Filter - Time Elapse ===")
    legalPositions = [(x, y) for x in range(5) for y in range(5)]
    numParticles = 500
    particles = initializeUniformly(legalPositions, numParticles)
    print("Initial particles (first 10):", particles[:10])
    particles_time = particleElapseTime(particles, legalPositions)
    print("Particles after time elapse (first 10):", particles_time[:10])
    beliefParticles_time = getBeliefDistribution(particles_time)
    visualize_belief_distribution(beliefParticles_time, gridShape=(5, 5),
                                  filename="visualizations/particle_time_elapse_q11.png",
                                  title="Particle Filter Belief (Time Elapse Q11)")

# ----------------------
# Main Driver: Run Questions 1 through 11
# ----------------------
def main():
    os.makedirs("visualizations", exist_ok=True)
    run_q1()
    run_q2()
    run_q3()
    run_q4()
    run_q5()
    run_q6()
    run_q7()
    run_q8()
    run_q9()
    run_q10()
    run_q11()

if __name__ == '__main__':
    main()
