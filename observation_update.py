# observation_update.py

from discrete_distribution import DiscreteDistribution
from noisy_observations import getObservationProb

def observeUpdate(beliefs, noisyDistance, pacmanPos, jailPos):
    """
    Updates the belief distribution over ghost positions given a noisy observation.
    
    Parameters:
      beliefs:       A DiscreteDistribution over ghost positions.
      noisyDistance: The observed noisy distance (an integer) or None.
      pacmanPos:     Tuple (x, y) for Pacman's position.
      jailPos:       Tuple (x, y) representing the ghost jail position.
    
    Returns:
      A new DiscreteDistribution (normalized) that incorporates the evidence.
      
    For each ghost position, the update is:
        new_prob(ghostPos) = current_prob(ghostPos) * getObservationProb(noisyDistance, pacmanPos, ghostPos, jailPos)
    Then, the distribution is normalized.
    """
    newBeliefs = DiscreteDistribution()
    for pos in beliefs.keys():
        # Multiply the prior by the likelihood of observing the noisy distance given the candidate ghost position.
        newBeliefs[pos] = beliefs[pos] * getObservationProb(noisyDistance, pacmanPos, pos, jailPos)
    newBeliefs.normalize()
    return newBeliefs

# Standalone test:
if __name__ == '__main__':
    from discrete_distribution import DiscreteDistribution
    # Suppose our ghost can be anywhere on a 5x5 grid.
    legalPositions = [(x, y) for x in range(5) for y in range(5)]
    beliefs = DiscreteDistribution()
    for pos in legalPositions:
        beliefs[pos] = 1.0
    beliefs.normalize()
    
    pacmanPos = (2, 2)
    jailPos = (0, 0)  # Example jail location
    noisyDistance = 2  # Example observation

    updatedBeliefs = observeUpdate(beliefs, noisyDistance, pacmanPos, jailPos)
    print("Updated Beliefs:")
    for pos, p in updatedBeliefs.items():
        print(f"{pos}: {p}")
