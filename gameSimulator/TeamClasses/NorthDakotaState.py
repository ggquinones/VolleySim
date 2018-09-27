from Team import Team
import numpy as np
import scipy.stats as st

class NorthDakotaState(Team):

	def generateKills(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),4.775348996779093,loc=8.999999984575972,scale=0.7705724151235773))

	def generateHitErrors(self):
		return (st.mielke.ppf(sp.random.uniform(),2.526059803448467,8.35312146425824,loc=1.6167322137766686,scale=5.20150618443822))

	def generateHitAttempts(self):
		return (st.beta.ppf(sp.random.uniform(),2.9857951693486213,1.368802261087399,loc=21.366414385394403,scale=26.091172883841864))

	def generateHitEfficiency(self):
		return (st.johnsonsu.ppf(sp.random.uniform(),-0.5206782839263,1.315480134961403,loc=0.03848555508154311,scale=0.02567341429554485))

	def generateAssists(self):
		return (st.laplace.ppf(sp.random.uniform(),loc=11.750000046312387,scale=1.2041312517756477))

	def generateAces(self):
		return (st.triang.ppf(sp.random.uniform(),0.14969247738554764,loc=0.07115423115188713,scale=4.000506140233473))

	def generateServeErrors(self):
		return (st.loglaplace.ppf(sp.random.uniform(),2.5268711411147677,loc=-0.0013541104603846453,scale=1.33135411420798))

	def generateReceptionErrors(self):
		return (st.semicircular.ppf(sp.random.uniform(),loc=1.0047389944441054,scale=1.0905121099642892))

	def generateDigs(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.9743038552467,loc=19.52032484835117,scale=1.4733813842665262))

	def generateBlockSolo(self):
		return (st.exponnorm.ppf(sp.random.uniform(),3.364771295222583,loc=0.24463516445926697,scale=0.17683482900826375))

	def generateBlockAssists(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.411766409193013,loc=2.7536271695458803,scale=1.0775494923052533))

	def generateBlockErrors(self):
		return (st.dgamma.ppf(sp.random.uniform(),2.1810731336224674,loc=0.5844564073955554,scale=0.16753176548223223))

	def generateBallHandlingErrors(self):
		return (st.exponnorm.ppf(sp.random.uniform(),5091.413903558818,loc=-0.00020282254362335875,scale=5.358425807847766e-05))

	def generatePoints(self):
		return (st.beta.ppf(sp.random.uniform(),1.6806655508455346,0.7236719244362813,loc=9.392934066269962,scale=9.60706593373004))

	def simulateStatLine(self):
		statLine=[]
		statLine.append(round(self.generateKills()))
		statLine.append(round(self.generateHitErrors()))
		statLine.append(round(self.generateHitAttempts()))
		statLine.append(round((statLine[0]-statLine[1])/float(statLine[2]),3))
		statLine.append(round(self.generateAssists()))
		statLine.append(round(self.generateAces()))
		statLine.append(round(self.generateServeErrors()))
		statLine.append(round(self.generateReceptionErrors()))
		statLine.append(round(self.generateDigs()))
		statLine.append(round(self.generateBlockSolo()))
		statLine.append(round(self.generateBlockAssists()))
		statLine.append(round(self.generateBlockErrors()))
		statLine.append(round(self.generateBallHandlingErrors()))
		statLine.append(round((statLine[0]+statLine[5]+statLine[9]+(statLine[10]/2.0))))
		return(statLine)