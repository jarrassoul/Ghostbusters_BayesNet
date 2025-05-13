# bayes_net.py

class BayesNet:
    def __init__(self):
        # Dictionary to store variable info.
        # Each key is a variable name, and its value is a dict with 'domain', 'parents'
        self.variables = {}
        # Ordered representation of dependencies, if needed.
        self.edges = {}

    def addVariable(self, varName, domain, parents):
        """
        Adds a variable (node) to the Bayesian network.

        Parameters:
            varName (str): The variable name.
            domain (list): List of possible values (for positions or observations).
            parents (list): List of parent variable names.
        """
        self.variables[varName] = {
            'domain': domain,
            'parents': parents,
            'CPT': None  # We'll set conditional probability tables later.
        }
        self.edges[varName] = parents

    def __str__(self):
        # Return a string representation of the Bayes Net.
        output = "BayesNet Structure:\n"
        for var, info in self.variables.items():
            output += f" Variable: {var}\n"
            output += f"  Domain: {info['domain']}\n"
            output += f"  Parents: {info['parents']}\n"
        return output
