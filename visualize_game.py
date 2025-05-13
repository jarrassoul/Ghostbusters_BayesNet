
# import matplotlib
# matplotlib.use('Agg')

# import matplotlib.pyplot as plt
# import networkx as nx

# def draw_game_board(legalPositions, pacmanPos, ghostPositions):
#     """
#     Visualizes the game board by showing a grid of legal positions and overlaying markers for Pacman and ghosts.
    
#     Parameters:
#       legalPositions: List of tuples (x, y) defining legal grid coordinates.
#       pacmanPos:      Tuple (x, y) representing Pacman’s current position.
#       ghostPositions: Dictionary mapping ghost identifier (e.g., "ghost1", "ghost2") to their positions.
#     """
#     xs = [pos[0] for pos in legalPositions]
#     ys = [pos[1] for pos in legalPositions]
    
#     x_min, x_max = min(xs) - 0.5, max(xs) + 0.5
#     y_min, y_max = min(ys) - 0.5, max(ys) + 0.5

#     plt.figure(figsize=(6, 6))
#     plt.scatter(xs, ys, s=200, color='lightgray', edgecolors='black', zorder=1)
    
#     for x in range(min(xs), max(xs) + 1):
#         plt.axvline(x - 0.5, color='gray', linestyle='--', linewidth=0.5)
#     for y in range(min(ys), max(ys) + 1):
#         plt.axhline(y - 0.5, color='gray', linestyle='--', linewidth=0.5)
    
#     plt.scatter([pacmanPos[0]], [pacmanPos[1]], s=300, color='yellow', edgecolors='black', zorder=2, label='Pacman')
    
#     ghost_colors = ['red', 'magenta']
#     for idx, (ghostId, pos) in enumerate(ghostPositions.items()):
#         plt.scatter([pos[0]], [pos[1]], s=300, color=ghost_colors[idx % len(ghost_colors)], edgecolors='black', zorder=3, label=ghostId)
    
#     plt.xlim(x_min, x_max)
#     plt.ylim(y_min, y_max)
#     plt.gca().set_aspect('equal', adjustable='box')
#     plt.xticks(range(min(xs), max(xs) + 1))
#     plt.yticks(range(min(ys), max(ys) + 1))
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.title("Pacman Maze Visualization")
#     plt.gca().invert_yaxis()
#     plt.legend(loc="upper left")
#     plt.show()

# def draw_bayes_net_structure(net):
#     """
#     Visualizes the Bayesian network structure by plotting its nodes and edges.
    
#     Parameters:
#       net: An instance of BayesNet containing the variables.
#     """
#     G = nx.DiGraph()
    
#     for var, info in net.variables.items():
#         G.add_node(var)
#         for parent in info['parents']:
#             G.add_edge(parent, var)
    
#     plt.figure(figsize=(5, 4))
#     pos = nx.spring_layout(G, seed=42)
#     nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, arrowstyle='->', arrowsize=20)
#     plt.title("Bayesian Network Structure")
    
#     # Save the figure instead of showing it interactively
#     plt.savefig('bayes_net_structure.png')
#     print("Bayesian network structure saved as bayes_net_structure.png")


# if __name__ == '__main__':
#     # --- Visualize the Game Board ---
#     # Define a 3x3 grid for legal positions.
#     legalPositions = [(x, y) for x in range(3) for y in range(3)]
    
#     # Set example positions.
#     pacmanPos = (1, 1)
#     ghostPositions = {
#         "ghost1": (0, 0),
#         "ghost2": (2, 2)
#     }
    
#     # Draw the game board.
#     draw_game_board(legalPositions, pacmanPos, ghostPositions)
    
#     # --- Visualize the Bayes Net Structure ---
#     from inference import constructBayesNet  # Ensure inference.py is in the same project directory
    
#     maxDistance = 4
#     bayes_net = constructBayesNet(legalPositions, maxDistance)
    
#     draw_bayes_net_structure(bayes_net)



import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for saving images
import matplotlib.pyplot as plt
import networkx as nx
import os

def draw_game_board(legalPositions, pacmanPos, ghostPositions, filename=None):
    """
    Visualizes the game board by showing a grid of legal positions and overlaying markers for Pacman and ghosts.
    
    Parameters:
      legalPositions: List of tuples (x, y) defining legal grid coordinates.
      pacmanPos:      Tuple (x, y) representing Pacman’s current position.
      ghostPositions: Dictionary mapping ghost identifier (e.g., "ghost1", "ghost2") to their positions.
      filename:       If provided, the image is saved to this file (PNG format).
    """
    xs = [pos[0] for pos in legalPositions]
    ys = [pos[1] for pos in legalPositions]
    
    x_min, x_max = min(xs) - 0.5, max(xs) + 0.5
    y_min, y_max = min(ys) - 0.5, max(ys) + 0.5

    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, s=200, color='lightgray', edgecolors='black', zorder=1)
    
    for x in range(min(xs), max(xs) + 1):
        plt.axvline(x - 0.5, color='gray', linestyle='--', linewidth=0.5)
    for y in range(min(ys), max(ys) + 1):
        plt.axhline(y - 0.5, color='gray', linestyle='--', linewidth=0.5)
    
    plt.scatter([pacmanPos[0]], [pacmanPos[1]], s=300, color='yellow', edgecolors='black', 
                zorder=2, label='Pacman')
    
    ghost_colors = ['red', 'magenta']
    for idx, (ghostId, pos) in enumerate(ghostPositions.items()):
        plt.scatter([pos[0]], [pos[1]], s=300, color=ghost_colors[idx % len(ghost_colors)], 
                    edgecolors='black', zorder=3, label=ghostId)
    
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks(range(min(xs), max(xs) + 1))
    plt.yticks(range(min(ys), max(ys) + 1))
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Pacman Maze Visualization")
    plt.gca().invert_yaxis()
    plt.legend(loc="upper left")
    plt.tight_layout()

    if filename:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename)
        print(f"Game board saved as {filename}")
    else:
        plt.show()
    plt.close()

def draw_bayes_net_structure(net, filename=None):
    """
    Visualizes the Bayesian network structure by plotting its nodes and edges.
    
    Parameters:
      net: An instance of BayesNet containing the variables.
      filename: If provided, the plot is saved as a PNG image at this location.
    """
    G = nx.DiGraph()
    
    # Add nodes and edges based on parent relationships.
    for var, info in net.variables.items():
        G.add_node(var)
        for parent in info['parents']:
            G.add_edge(parent, var)
    
    plt.figure(figsize=(5, 4))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, 
            arrowstyle='->', arrowsize=20)
    plt.title("Bayesian Network Structure")
    plt.tight_layout()
    
    if filename:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        plt.savefig(filename)
        print(f"Bayesian network structure saved as {filename}")
    else:
        plt.show()
    plt.close()

# For testing this module independently:
if __name__ == '__main__':
    # Test game board visualization:
    legalPositions = [(x, y) for x in range(3) for y in range(3)]
    pacmanPos = (1, 1)
    ghostPositions = {"ghost1": (0, 0), "ghost2": (2, 2)}
    draw_game_board(legalPositions, pacmanPos, ghostPositions, filename="visualizations/game_board.png")
    
    # Dummy BayesNet for testing bayes net visualization.
    class BayesNet:
        def __init__(self):
            self.variables = {
                "pacman": {"domain": legalPositions, "parents": []},
                "ghost1": {"domain": legalPositions, "parents": []},
                "ghost2": {"domain": legalPositions, "parents": []},
                "obs1": {"domain": list(range(5)), "parents": ["pacman", "ghost1"]},
                "obs2": {"domain": list(range(5)), "parents": ["pacman", "ghost2"]}
            }
        def __str__(self):
            s = ""
            for var, info in self.variables.items():
                s += f"Variable: {var}\n Domain: {info['domain']}\n Parents: {info['parents']}\n"
            return s

    bayes_net = BayesNet()
    draw_bayes_net_structure(bayes_net, filename="visualizations/bayes_net_structure.png")

