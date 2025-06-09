

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
