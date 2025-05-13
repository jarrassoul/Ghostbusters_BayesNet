# particle_filter.py

import random
from discrete_distribution import DiscreteDistribution
from noisy_observations import getObservationProb
# We'll use the ghost transition function from elapse_time.
from elapse_time import getGhostTransitionDistribution

def initializeUniformly(legalPositions, numParticles):
    """
    Distributes particles evenly among the legal positions using the mod operator.
    """
    particles = []
    numPositions = len(legalPositions)
    for i in range(numParticles):
        particles.append(legalPositions[i % numPositions])
    return particles

def getBeliefDistribution(particles):
    """
    Converts a list of particles into a normalized DiscreteDistribution.
    """
    beliefDist = DiscreteDistribution()
    for p in particles:
        beliefDist[p] = beliefDist[p] + 1
    beliefDist.normalize()
    return beliefDist

def particleObserveUpdate(particles, noisyDistance, pacmanPos, jailPos, legalPositions, numParticles):
    """
    Updates particles based on a noisy observation.
    
    For each particle (representing a ghost position p), compute the weight:
      weight = getObservationProb(noisyDistance, pacmanPos, p, jailPos)
    Then resample to produce a new set of particles according to these weights.
    If the total weight is 0, reinitialize uniformly over legalPositions.
    
    Inputs:
      particles      - Current list of particles.
      noisyDistance  - The observed noisy distance.
      pacmanPos      - Pacman's current position.
      jailPos        - The ghost jail position.
      legalPositions - All legal ghost positions.
      numParticles   - Total number of particles.
    
    Returns:
      A new list of particles (of length numParticles).
    """
    weightedParticles = []
    totalWeight = 0.0
    for p in particles:
        weight = getObservationProb(noisyDistance, pacmanPos, p, jailPos)
        weightedParticles.append((p, weight))
        totalWeight += weight

    if totalWeight == 0:
        # Reinitialize uniformly if no particle receives weight.
        return initializeUniformly(legalPositions, numParticles)
    
    # Create a DiscreteDistribution for resampling.
    distribution = DiscreteDistribution()
    for p, weight in weightedParticles:
        distribution[p] = distribution[p] + weight
    distribution.normalize()

    newParticles = []
    for _ in range(numParticles):
        newParticles.append(distribution.sample())
    return newParticles

def particleElapseTime(particles, legalPositions):
    """
    Updates each particle by simulating ghost motion.
    
    For each particle p, sample a new position from the transition model 
    obtained by calling getGhostTransitionDistribution(p, legalPositions).
    
    Returns the updated list of particles.
    """
    newParticles = []
    for p in particles:
        transitionDist = getGhostTransitionDistribution(p, legalPositions)
        newParticles.append(transitionDist.sample())
    return newParticles

# Standalone test for particle filter functions:
if __name__ == '__main__':
    # Define a simple 5x5 grid.
    legalPositions = [(x, y) for x in range(5) for y in range(5)]
    numParticles = 500
    
    particles = initializeUniformly(legalPositions, numParticles)
    print("First 10 particles (Uniform initialization):", particles[:10])
    
    belief = getBeliefDistribution(particles)
    print("Belief distribution (sample counts normalized):")
    for pos, prob in sorted(belief.items()):
        print(f"{pos}: {prob:.3f}")
    
    # Test particle observation update.
    pacmanPos = (2, 2)
    jailPos = (0, 0)
    noisyDistance = 2
    particles_updated = particleObserveUpdate(particles, noisyDistance, pacmanPos, jailPos, legalPositions, numParticles)
    print("First 10 particles after observation update:", particles_updated[:10])
    
    # Test particle time elapse.
    particles_time = particleElapseTime(particles, legalPositions)
    print("First 10 particles after time elapse:", particles_time[:10])
