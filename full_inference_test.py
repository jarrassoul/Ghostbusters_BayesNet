# full_inference_test.py

import os
from discrete_distribution import DiscreteDistribution
from noisy_observations import manhattanDistance
from visualize_beliefs import visualize_belief_distribution
from visualize_game import draw_game_board

def full_inference_test():
    """
    Full Inference Test for Question 8:
      1. Uses belief distributions to identify the most likely ghost positions.
      2. Chooses an action that minimizes the maze (Manhattan) distance between Pacman and the nearest ghost.
      
    Visualizations:
      - Saves heatmaps of ghost belief distributions.
      - Saves the game board illustration with Pacman and ghosts at their inferred positions.
    """
    # Define legal positions on a 5x5 grid.
    legalPositions = [(x, y) for x in range(5) for y in range(5)]
    
    # Initialize belief distributions for two ghosts (e.g., ghost1 and ghost2),
    # here starting uniformly over all legal positions.
    ghostBeliefs1 = DiscreteDistribution()
    ghostBeliefs2 = DiscreteDistribution()
    for pos in legalPositions:
        ghostBeliefs1[pos] = 1.0
        ghostBeliefs2[pos] = 1.0
    ghostBeliefs1.normalize()
    ghostBeliefs2.normalize()
    
    # Helper function to get the most likely position for a belief distribution.
    def getMaxPosition(belief):
        max_prob = -1
        max_pos = None
        for pos, prob in belief.items():
            if prob > max_prob:
                max_prob = prob
                max_pos = pos
        return max_pos, max_prob

    ghost1_max, p1 = getMaxPosition(ghostBeliefs1)
    ghost2_max, p2 = getMaxPosition(ghostBeliefs2)
    print("Most likely ghost positions:")
    print("  Ghost 1:", ghost1_max, "with probability", p1)
    print("  Ghost 2:", ghost2_max, "with probability", p2)
    
    # Assume Pacman's current position.
    pacmanPos = (2, 2)
    # Define a list of legal actions.
    legalActions = ["North", "South", "East", "West", "Stop"]

    # Helper function: return Pacman's new position given a current position and an action.
    def getNewPosition(position, action):
        x, y = position
        if action == "North":
            return (x, y - 1)
        elif action == "South":
            return (x, y + 1)
        elif action == "East":
            return (x + 1, y)
        elif action == "West":
            return (x - 1, y)
        else:  # Stop
            return (x, y)

    # Helper for Manhattan distance.
    def maze_distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # For each legal action, compute Pacman's new position and the maze distance from that location
    # to both ghost1 and ghost2's most likely positions; then choose the action with minimal max proximity.
    best_action = None
    best_distance = float("inf")
    for action in legalActions:
        newPos = getNewPosition(pacmanPos, action)
        d1 = maze_distance(newPos, ghost1_max)
        d2 = maze_distance(newPos, ghost2_max)
        min_d = min(d1, d2)
        print(f"Action: {action} -> NewPos: {newPos}; Distances: Ghost1 = {d1}, Ghost2 = {d2} (min = {min_d})")
        if min_d < best_distance:
            best_distance = min_d
            best_action = action

    print("\nPacman's current position:", pacmanPos)
    print("Chosen action for Pacman:", best_action, "with resulting minimum maze distance:", best_distance)

    # Visualize each ghost's belief distribution as a heatmap.
    visualize_belief_distribution(ghostBeliefs1, gridShape=(5, 5),
                                  filename="visualizations/ghost1_beliefs_q8.png",
                                  title="Ghost 1 Belief Distribution (Q8)")
    visualize_belief_distribution(ghostBeliefs2, gridShape=(5, 5),
                                  filename="visualizations/ghost2_beliefs_q8.png",
                                  title="Ghost 2 Belief Distribution (Q8)")
    # Visualize the board, drawing Pacman and ghosts (using their most likely positions).
    ghostPositions = {"ghost1": ghost1_max, "ghost2": ghost2_max}
    draw_game_board(legalPositions, pacmanPos, ghostPositions,
                    filename="visualizations/full_inference_q8.png")
    print("Full Inference Test (Q8) completed.")

if __name__ == '__main__':
    os.makedirs("visualizations", exist_ok=True)
    full_inference_test()
