'''This script demonstrates simulations of coin flipping'''
import random
import matplotlib.pyplot as plt
import numpy as np

# creating a six sided die, was not sure what the question was asking given that the 
# results of the coin flip were normally distributed

class Dice(object):
    mu, sigma = 0, 0.1
    sides = (1 , 2, 3, 4, 5, 6)
    last_result = None

    def roll(self):
        self.last_result = result = random.choice(self.sides)
        return result

def create_dice(number):
    return [Dice() for _ in xrange(number)]

coinlist = []

#rolling a thousand dice a thousand times and counting how frequently 1 hits
dice = create_dice(1000)
for i in range(1000):
	dielist = []
	for die in dice:
		dielist.append(die.roll())	
	coinlist.append(dielist.count(1))

	
#plotting histogram, looks somewhat normal 
hist, bin_edges = np.histogram(coinlist, density=True)
plt.bar(bin_edges[:-1], hist, width = .3)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show() 

