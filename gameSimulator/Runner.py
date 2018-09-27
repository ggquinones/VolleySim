from itertools import combinations 
import numpy as np
import scipy.stats as st
from OralRoberts import OralRoberts
from Denver import Denver
from PurdueFortWayne import PurdueFortWayne
from WesternIllinois import WesternIllinois
from SouthDakota import SouthDakota
from SouthDakotaState import SouthDakotaState
#from NorthDakota import NorthDakota
from NorthDakotaState import NorthDakotaState
from Omaha import Omaha

def makeTeamList():
	teams = []
	teams.append(OralRoberts("Oral Roberts"))
	teams.append(Denver("Denver"))
	teams.append(PurdueFortWayne("Purdue Fort Wayne"))
	teams.append(WesternIllinois("Western Illinois"))
	teams.append(SouthDakota("South Dakota"))
	teams.append(SouthDakotaState("South Dakota State"))
	#teams.append(NorthDakota("North Dakota"))
	teams.append(NorthDakotaState("North Dakota State"))
	teams.append(Omaha("Omaha"))
	return teams

def makeMatchUps(teams):
	return list(combinations(teams, 2))
	
def calcStats(statsA,statsB):
	statsA[3] = (statsA[0]-statsA[1]) / statsA[2] #Hitting Efficiency
	statsA[12] = statsA[0] + statsA[5] + statsA[9] + (statsA[10]/2) + statsB[1] + statsB[6]
	return statsA

def gameValid(stats1,stats2):
	team1Points = stats1[13]
	team2Points = stats2[13]
	kills1 = stats1[0]
	kills2 = stats2[0]
	errors1 = stats1[1]
	errors2 = stats2[1]
	attempts1 = stats1[2]
	attempts2 = stats2[2]
	assists1 = stats1[4]
	assists2 = stats2[4]
	digs1 = stats1[8]
	digs2 = stats2[8]
	if team1Points < 25 and team2Points < 25:
		print("PF1"+str(team1Points) + " " + str(team2Points))
		return False
	elif team1Points == 25 and team2Points > 23:
		print("PF2"+str(team1Points) + " " + str(team2Points))
		return False
	elif team2Points == 25 and team1Points > 23:
		print("PF3"+str(team1Points) + " " + str(team2Points))
		return False
	elif team1Points > 25 and team2Points != (team1Points-2):
		print("PF4"+str(team1Points) + " " + str(team2Points))
		return False
	elif team2Points > 25 and team1Points != (team2Points-2):
		print("PF5"+str(team1Points) + " " + str(team2Points))
		return False
	elif kills1 + errors1 > attempts1:
		print("GF1"+str(kills1) + " " + str(errors1) + " " + str(attempts1))
		return False
	elif kills2 + errors2 > attempts2:
		print("GF2"+str(kills2) + " " + str(errors2) + " " + str(attempts2))
		return False
	elif digs1 > attempts2 - kills2 - errors2:
		print("GF3"+str(digs1)+" "+str(kills2) + " " + str(errors2) + " " + str(attempts2))
		return False
	elif digs2 > attempts1 - kills1 - errors1:
		print("GF4"+str(digs2)+" "+str(kills1) + " " + str(errors1) + " " + str(attempts1))
		return False
	elif kills1 < assists1:
		print("GF5"+str(kills1)+" "+str(assists1) )
		return False
	elif kills2 < assists2:
		print("GF6"+str(kills2)+" "+str(assists2 ))
		return False
	else:
		return True
def updateSetsWon(stats1,stats2,team1,team2):
	if stats1[13] > stats2[13]:
		team1.addWin()
		team2.addLoss()
	else:
		team2.addWin()
		team1.addLoss()
	teams = []
	teams.append(team1)
	teams.append(team2)
	return teams

def Runner():
	teams = makeTeamList()
	matchUps = makeMatchUps(teams)

	for matchUp in matchUps:
		print(matchUp[0].getName() + " vs " + matchUp[1].getName())
		team1 = matchUp[0]
		sets1 = 0
		team2 = matchUp[1]
		sets2 = 0
		while sets1 < 3 and sets2 < 3:
			stats1= team1.simulateStatLine()
			stats2= team2.simulateStatLine()
			print(stats1)
			if gameValid(stats1,stats2):
				winner = updateSetsWon(stats1,stats2,team1,team2)
				if winner:
					sets1+=1
				else:
					sets2+=1
			else:
				continue
		print(str(sets1) + " to " + str(sets2))	


	#displayWinPct()
	
Runner()
