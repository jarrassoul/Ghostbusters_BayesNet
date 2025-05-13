# discrete_distribution.py
import random

class DiscreteDistribution(dict):
    """
    A DiscreteDistribution models belief distributions (or weight distributions) by extending a Python dictionary.
    Keys are elements of the distribution (e.g. positions), and values are the unnormalized weights.
    """
    def __getitem__(self, key):
        # Return 0 for keys not present in the dictionary
        return super().get(key, 0)

    def copy(self):
        return DiscreteDistribution(dict(self))

    def total(self):
        """
        Returns the sum of the weights in the distribution.
        """
        return sum(self.values())

    def normalize(self):
        """
        Normalizes the distribution such that the total probability sums to 1.
        If the total equals zero, the distribution remains unchanged.
        """
        total = self.total()
        if total == 0:
            return
        for key in self:
            self[key] = self[key] / total

    def sample(self):
        """
        Returns a random sample from the distribution (weighted by the values).
        Raises an exception if the total weight is 0.
        """
        total = self.total()
        if total == 0:
            raise Exception("Cannot sample from an empty or zero-weight distribution.")
        r = random.uniform(0, total)
        cumulative = 0.0
        for key, weight in self.items():
            cumulative += weight
            if r <= cumulative:
                return key
        # Should not reach here; return last key as a fallback.
        return key

# Standalone test for DiscreteDistribution:
if __name__ == '__main__':
    dd = DiscreteDistribution({'a': 2, 'b': 3, 'c': 5})
    print("Before normalization:", dd)
    dd.normalize()
    print("After normalization:", dd)
    print("Sampled key:", dd.sample())
