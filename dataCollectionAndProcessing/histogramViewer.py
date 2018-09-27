import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as st

def getStatsFromCSV(team):
	#fr = open("summitFormattedData/"+team+".txt","r")
	fr = open("summitFormattedPerSetData/"+team+".txt","r")
	lines=fr.readlines()
	lines.pop(-1)
	newStats =[]
	for line in lines:		
		line=line.strip()		
		line = line.split(",")
		
		line = [float(i) for i in line]
		newStats.append(line)
	return newStats
stats = getStatsFromCSV('Denver')
a=stats[4]


plt.hist(a, bins=10)  # arguments are passed to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()
