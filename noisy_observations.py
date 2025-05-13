# noisy_observations.py

def manhattanDistance(pos1, pos2):
    """
    Computes the Manhattan distance between two positions.
    Each position is a tuple (x, y).
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def getObservationProb(noisyDistance, pacmanPos, ghostPos, jailPos, emissionModel=None):
    """
    Returns the probability of a noisy distance reading given Pacman's and a ghost's 
    positions, taking into account a special jail position.
    
    Parameters:
      noisyDistance: The observed (noisy) distance (an integer) or None.
      pacmanPos:     Tuple (x, y) for Pacman's position.
      ghostPos:      Tuple (x, y) for the ghost's position.
      jailPos:       Tuple (x, y) representing the ghost jail location.
      emissionModel: (Optional) A dictionary mapping true Manhattan distances to a 
                     dictionary that maps possible noisy distances to probabilities.
                     For example, if provided, you might have:
                         emissionModel[trueDistance][noisyDistance] = probability.
    
    Returns:
      A float probability P(noisyDistance | pacmanPos, ghostPos, jailPos).
    
    Default model (if emissionModel is None):
      - If ghostPos == jailPos:
           * Return 1.0 if noisyDistance is None, else return 0.0.
      - Otherwise, compute trueDistance and:
           * Return 0.8 if noisyDistance equals trueDistance.
           * Return 0.1 if |noisyDistance - trueDistance| == 1.
           * Return 0.0 for all other readings.
    """
    # Case: ghost is in jail.
    if ghostPos == jailPos:
        return 1.0 if noisyDistance is None else 0.0
    
    # If ghost is not in jail but no observation is provided, return 0.
    if noisyDistance is None:
        return 0.0
    
    trueDistance = manhattanDistance(pacmanPos, ghostPos)
    
    if emissionModel is not None:
        # Use the provided emission model.
        if trueDistance not in emissionModel:
            return 0.0
        return emissionModel[trueDistance].get(noisyDistance, 0.0)
    else:
        # Default simple model:
        if noisyDistance == trueDistance:
            return 0.8
        elif abs(noisyDistance - trueDistance) == 1:
            return 0.1
        else:
            return 0.0

# Standalone test for getObservationProb:
if __name__ == '__main__':
    # Example positions:
    pacmanPos = (2, 3)
    ghostPos = (4, 5)
    jailPos = (0, 0)
    
    # Test with default model:
    trueDist = manhattanDistance(pacmanPos, ghostPos)
    print("True Manhattan distance:", trueDist)
    for noisy in range(trueDist - 2, trueDist + 3):
        prob = getObservationProb(noisy, pacmanPos, ghostPos, jailPos)
        print(f"P(noisyDistance={noisy}) = {prob}")
    
    # Test the jail case:
    print("Ghost in jail, observation None:", getObservationProb(None, pacmanPos, jailPos, jailPos))
    print("Ghost in jail, observation 5:", getObservationProb(5, pacmanPos, jailPos, jailPos))
