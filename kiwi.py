#!/usr/local/bin/python

from gautils import *
from ca_eval import *
from spect import *
import matplotlib.pyplot as plt
import os
from datetime import datetime

import random

plotDirectory = 'plots/'+datetime.now().strftime('%Y%m%d_%H%M')+'/'

random.seed(42)

width = 129
timesteps = 47
numGens = 10000

population = init_pop(10,width,3, 0.7)

perf = getPerfectPattern('./ploink.wav', timesteps, width, 1.0)
plt.matshow(perf, cmap=cm.gist_heat_r)
if not os.path.exists('plots'):
	os.makedirs('plots')
os.makedirs(plotDirectory)
plt.savefig(plotDirectory+'perf.png')
plt.close

previousBest = 0
for gen in xrange(numGens):
	fitpop = evalFitness(population, perf, timesteps, width, 3)
	#top fitness score
	best = max(fitpop, key=lambda x: x[1])	
	if best[1] != previousBest:
		print gen ,":", best[1]
		fname = plotDirectory + str(gen) + ".png"
		fname_sub = plotDirectory + str(gen) + "_sub.png"
		plt.matshow(best[2], cmap=cm.gist_heat_r)
		plt.savefig(fname)
		plt.close()
		plt.matshow(best[3], cmap=cm.gist_heat_r)
		plt.savefig(fname_sub)
		plt.close()

		previousBest = best[1]
	population = breed(fitpop, 0.2, 0.0, 0.05)