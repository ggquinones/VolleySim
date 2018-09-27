class Team(object):
	def __init__(self,name):
		self.name = name
		self.wins=0
		self.losses=0
	def getName(self):
		return self.name
	def getWins(self):
		return self.wins
	def getLosses(self):
		return self.losses
	def setName(self,name):
		self.name = name
	def addWin(self):
		self.wins +=1
	def addLoss(self):
		self.losses += 1
	

