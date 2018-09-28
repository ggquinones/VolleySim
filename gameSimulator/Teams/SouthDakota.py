from Team import Team
import numpy as np
import scipy.stats as st

import scipy as sp

class SouthDakota(Team):

	def generateKills(self):
		return (st.burr.ppf(sp.random.uniform(),11.566881670659948,0.18101793231644014,loc=6.66602687089542,scale=9.205842463274575))

	def generateHitErrors(self):
		return (st.invweibull.ppf(sp.random.uniform(),81658625.1729751,loc=-91556933.41723824,scale=91556937.99757403))

	def generateHitAttempts(self):
		return (st.foldnorm.ppf(sp.random.uniform(),1.3146722131833055,loc=29.329999948628103,scale=6.175872226517692))

	def generateHitEfficiency(self):
		return (st.dgamma.ppf(sp.random.uniform(),2.0361211858853263,loc=0.05720362238383049,scale=0.012004818759949323))

	def generateAssists(self):
		return (st.genextreme.ppf(sp.random.uniform(),0.43125143814958466,loc=11.686346097924954,scale=2.560818920700303))

	def generateAces(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.597384087437942,loc=1.141011894939099,scale=0.6323991719144926))

	def generateServeErrors(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),0.10333593742779829,loc=1.3350021736885087,scale=0.42494439030176767))

	def generateReceptionErrors(self):
		return (st.bradford.ppf(sp.random.uniform(),0.8695582226360543,loc=0.19999850892723026,scale=2.1300025906580684))

	def generateDigs(self):
		return (st.johnsonsb.ppf(sp.random.uniform(),-0.006976841247407178,0.5973883006985401,loc=10.77079279484494,scale=14.461071918537092))

	def generateBlockSolo(self):
		return (st.gilbrat.ppf(sp.random.uniform(),loc=-0.06732258625910767,scale=0.2787134670420349))

	def generateBlockAssists(self):
		return (st.maxwell.ppf(sp.random.uniform(),loc=-0.40483213465156587,scale=1.6274724251308248))

	def generateBlockErrors(self):
		return (st.genpareto.ppf(sp.random.uniform(),-0.3805432790192681,loc=-5.507778438040151e-09,scale=0.6492925143478151))

	def generateBallHandlingErrors(self):
		return (st.genexpon.ppf(sp.random.uniform(),2.4133724037699373,1.327061103068159,9.826188402261762e-09,loc=-9.329453045608943e-10,scale=0.3127635100219923))

	def generatePoints(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.8144515550768805,loc=15.963466663585212,scale=2.6776115306247585))

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