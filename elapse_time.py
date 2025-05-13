# elapse_time.py

from discrete_distribution import DiscreteDistribution

def getGhostTransitionDistribution(currentPos, legalPositions):
    """
    Given the current ghost position and a list of legal positions (typically the grid positions),
    returns a probability distribution (as a DiscreteDistribution) over possible next positions,
    with a bias toward moving south (simulating GoSouthGhost behavior).

    Moves considered:
      - North: (x, y-1)
      - South: (x, y+1)  -- biased (higher weight)
      - East : (x+1, y)
      - West : (x-1, y)
      - Stay : (x, y)
      
    Only moves resulting in a position inside legalPositions are allowed.
    """
    x, y = currentPos
    # Base weights for moves, with a small extra weight to "stay"
    moves = {
        (x, y - 1): 1.0,    # North
        (x, y + 1): 1.0,    # South
        (x + 1, y): 1.0,    # East
        (x - 1, y): 1.0,    # West
        (x, y): 0.5         # Stay in place
    }
    # If moving south is allowed, boost its weight to simulate the GoSouthGhost behavior.
    if (x, y + 1) in legalPositions:
        moves[(x, y + 1)] *= 2.0

    # Build a distribution only over legal moves.
    legalMoves = DiscreteDistribution()
    for pos, weight in moves.items():
        if pos in legalPositions:
            legalMoves[pos] = weight
    legalMoves.normalize()
    return legalMoves

def elapseTime(beliefs, legalPositions):
    """
    Updates the belief distribution to reflect ghost motion via the transition model.
    
    For each current ghost position, get a transition distribution (cached if possible), and distribute 
    the probability mass according to the transition probabilities.
    
    Parameters:
      beliefs: A DiscreteDistribution representing the current belief over ghost positions.
      legalPositions: A list of legal positions (e.g., all positions in the maze).
      
    Returns:
      A new, normalized DiscreteDistribution over ghost positions after the time elapse.
    
    Note:
      – If code performance is an issue, this function caches transition distributions so that 
        self.getGhostTransitionDistribution is not recalculated for every ghost position repeatedly.
      – With a GoSouth bias, as time elapses the belief distribution should move toward the board’s bottom.
    """
    newBeliefs = DiscreteDistribution()
    # Cache for transition distributions to avoid redundant calls.
    transitionCache = {}
    for currentPos, prob in beliefs.items():
        if currentPos in transitionCache:
            transitionDist = transitionCache[currentPos]
        else:
            transitionDist = getGhostTransitionDistribution(currentPos, legalPositions)
            transitionCache[currentPos] = transitionDist
        # For each possible next position, move the belief according to the transition model.
        for nextPos, transProb in transitionDist.items():
            newBeliefs[nextPos] += prob * transProb
    newBeliefs.normalize()
    return newBeliefs

# Standalone test:
if __name__ == '__main__':
    from discrete_distribution import DiscreteDistribution
    # Define a simple 5x5 grid.
    legalPositions = [(x, y) for x in range(5) for y in range(5)]
    # Create an initial uniform belief distribution over ghost positions.
    beliefs = DiscreteDistribution()
    for pos in legalPositions:
        beliefs[pos] = 1.0
    beliefs.normalize()
    
    print("Initial beliefs:")
    for pos, p in sorted(beliefs.items()):
        print(f"{pos}: {p:.3f}")
    
    # Update beliefs using elapseTime.
    newBeliefs = elapseTime(beliefs, legalPositions)
    
    print("\nBeliefs after elapseTime (expected to shift south):")
    for pos, p in sorted(newBeliefs.items()):
        print(f"{pos}: {p:.3f}")
