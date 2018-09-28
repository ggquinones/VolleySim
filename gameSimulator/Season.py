from itertools import combinations 
import numpy as np
import scipy.stats as st
from Teams.OralRoberts import OralRoberts
from Teams.Denver import Denver
from Teams.PurdueFortWayne import PurdueFortWayne
from Teams.WesternIllinois import WesternIllinois
from Teams.SouthDakota import SouthDakota
from Teams.SouthDakotaState import SouthDakotaState
from Teams.NorthDakotaState import NorthDakotaState
from Teams.Omaha import Omaha

class Season:
	def __init__(self):
		self.teams = self.makeTeamList()
		self.matchUps=list(combinations(self.teams,2))

	def simulateSeason(self):
		for match in self.matchUps:
			self.simulateMatch(match)
			self.simulateMatch(match)
		return teams
	
	def processMatch(self,sets1,sets2,match):
		if sets1>sets2:
			match[0].addWin()
			match[1].addLoss()
		else:
			match[1].addWin()
			match[0].addLoss()
		
	def simulateMatch(self,match):
		team1 = match[0]
		team2 = match[1]
		print("Processing..."+team1.getName()+" vs. "+team2.getName())
		sets1=0
		sets2=0
		stats1 = team1.simulateStatLine()
		stats2 = team2.simulateStatLine()
		while sets1 < 3 and sets2 < 3:
			while not self.setIsValid(stats1,stats2):
				stats1 = team1.simulateStatLine()
				stats2 = team2.simulateStatLine()
			if self.determineWinner(stats1,stats2) == 1:
				sets1+=1
			else:
				sets2+=1
			stats1 = team1.simulateStatLine()
			stats2 = team2.simulateStatLine()	
				
		if sets1>sets2:
			print(team1.getName() + " wins! " + str(sets1) +" to "+str(sets2))
		else:
			print(team2.getName() + " wins! " + str(sets2) +" to "+str(sets1))
		
		self.processMatch(sets1,sets2,match)
		
	def makeTeamList(self):
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
	def setIsValid(self,stats1,stats2):
		pts1 = stats1[13]+ stats2[1]+stats2[6]
		pts2 = stats2[13]+ stats1[1]+stats1[6]
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
		
		if pts1 < 25 and pts2 < 25:
			#print("pts1 < 25 and pts2 < 25: "+ str(pts1)+"/"+str(pts2))
			return(False)
		elif pts1 > 25 and pts2 != (pts1-2):
			#print("Pts1 > 25 and pts2 != (pts1-2): "+ str(pts1)+"/"+str(pts2))
			return(False)
		elif pts1 == 25 and pts2 > 23:
			#print("Pts1 = 25 and pts2 > 23: "+ str(pts2))
			return(False)
		elif pts2 > 25 and pts1 != (pts2-2):
			#print("pts2 > 25 and pts1 != (pts2-2): "+ str(pts1)+"/"+str(pts2))
			return(False)
		elif pts2 == 25 and pts1 > 23:
			#print("pts2 == 25 and pts1 > 23: "+ str(pts2))
			return(False)
		elif kills1 + errors1 > attempts1:
			#print("kills1 + errors1 > attempts1"+str(kills1) + "/" + str(errors1) + "/" + str(attempts1))
			return False
		elif kills2 + errors2 > attempts2:
			#print("kills2 + errors2 > attempts2"+str(kills2) + "/" + str(errors2) + "/" + str(attempts2))
			return False
		elif digs1 > attempts2 - kills2 - errors2:
			#print("digs1 > attempts2 - kills2 - errors2"+str(digs1)+"/"+str(kills2) + "/" + str(errors2) + "/" + str(attempts2))
			return False
		elif digs2 > attempts1 - kills1 - errors1:
			#print("digs2 > attempts1 - kills1 - errors1"+str(digs2)+"/"+str(kills1) + "/" + str(errors1) + "/" + str(attempts1))
			return False
		elif kills1 < assists1:
			#print("kills1 < assists1"+str(kills1)+" "+str(assists1) )
			return False
		elif kills2 < assists2:
			#print("kills2 < assists2"+str(kills2)+" "+str(assists2 ))
			return False
		else:
			#print("Game Valid: "+ str(pts1)+"/"+str(pts2))
			return(True)

	def determineWinner(self,stats1,stats2):
		if stats1[13] > stats2[13]:
			return 1
		else:
			return 2
