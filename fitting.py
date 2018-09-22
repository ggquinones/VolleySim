
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def getStat():
	file = open("summitFormattedData/Denver.txt", "r") 
	data= file.readlines()	
	file.close()
	kills = data[0]
	kills = kills.split(",")
	kills = [int(i) for i in kills]
	return kills
	


plt.xlabel("Denver Team Kills Distribution 2017")
plt.ylabel("Frequency")
plt.hist(getStat(),rwidth=0.95,bins=7)

plt.show()
