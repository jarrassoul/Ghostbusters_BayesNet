# inference.py

from bayes_net import BayesNet

def constructBayesNet(legalPositions, maxDistance):
    """
    Constructs a Bayesian network structure for the Ghostbusters assignment.

    Parameters:
        legalPositions (list): A list of legal positions (e.g., tuples) for Pacman and ghosts.
        maxDistance (int):     Maximum Manhattan distance used to build the observation domain.
    
    Returns:
        net (BayesNet):        The constructed Bayesian network.
    """
    # Create an instance of the BayesNet.
    net = BayesNet()
    
    # Define variable names.
    pacmanVar = "pacman"
    ghost1Var = "ghost1"
    ghost2Var = "ghost2"
    obs1Var = "obs1"  # Observation for ghost1.
    obs2Var = "obs2"  # Observation for ghost2.
    
    # Define the domains:
    # Both Pacman and ghost positions can be any of the legal positions.
    posDomain = legalPositions
    # Observations are Manhattan distances and can range from 0 to maxDistance.
    obsDomain = list(range(maxDistance + 1))
    
    # Add the positional variables. These are root nodes without parents.
    net.addVariable(pacmanVar, posDomain, [])
    net.addVariable(ghost1Var, posDomain, [])
    net.addVariable(ghost2Var, posDomain, [])
    
    # Add observation variables.
    # These depend on Pacman's position and the corresponding ghost's position.
    net.addVariable(obs1Var, obsDomain, [pacmanVar, ghost1Var])
    net.addVariable(obs2Var, obsDomain, [pacmanVar, ghost2Var])
    
    return net

# If you'd like to add a test here, you could include:
if __name__ == '__main__':
    # For example, legalPositions can be simple coordinates.
    # Assume a 3x3 grid for simplicity.
    legalPositions = [(x, y) for x in range(3) for y in range(3)]
    # Maximum Manhattan distance for a 3x3 grid is 4.
    maxDistance = 4

    bayes_net = constructBayesNet(legalPositions, maxDistance)
    print(bayes_net)
