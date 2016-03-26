
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal

# creating a dice that has normally distributed sides

class Dice(object):
    sides = normal(size=1000)
    
    def roll(self):
        self.last_result = result = random.choice(self.sides)
        return result

def create_dice(number):
    return [Dice() for _ in xrange(number)]

maxlist = []
minlist = []
coinlist = []

#rolling a thousand dice a thousand times and counting how frequently 1 hits
dice = create_dice(1000)
for i in range(1000):
	dielist = []
	for die in dice:
		coinlist.append(die.roll())	
		dielist.append(die.roll())	
	maxlist.append(max(dielist))
	minlist.append(min(dielist))
	
#plotting histogram, looks somewhat normal 
hist, bin_edges = np.histogram(coinlist, density=True)
plt.bar(bin_edges[:-1], hist, width = .3)
plt.xlim(min(bin_edges), max(bin_edges))
plt.title('total results')
plt.show() 
	
#plotting histogram max, very skewed right
histm, bin_edgesm = np.histogram(maxlist, density=True)
plt.bar(bin_edgesm[:-1], histm, width = .3)
plt.xlim(min(bin_edgesm), max(bin_edgesm))
plt.title('max')
plt.show() 

#plotting histogram min, very skewed left
histmin, bin_edgesmin = np.histogram(minlist, density=True)
plt.bar(bin_edgesmin[:-1], histmin, width = .3)
plt.xlim(min(bin_edgesmin), max(bin_edgesmin))
plt.title('min')
plt.show() 

