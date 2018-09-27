from Team import Team
import numpy as np
import scipy.stats as st

class SouthDakota(Team):

	def generateKills(self):
		return (st.gompertz.ppf(sp.random.uniform(),0.06726136628158016,loc=7.599999973260443,scale=2.405060313521884))

	def generateHitErrors(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),1.0811048665265763,loc=5.118932291646935,scale=1.0221145974316204))

	def generateHitAttempts(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.5729243328333389,loc=36.34207005384653,scale=5.233050122520418))

	def generateHitEfficiency(self):
		return (st.dgamma.ppf(sp.random.uniform(),2.0361211858853263,loc=0.05720362238383049,scale=0.012004818759949323))

	def generateAssists(self):
		return (st.beta.ppf(sp.random.uniform(),2.8250253508791188,1.7698004579129731,loc=4.955552777776475,scale=12.077732173193075))

	def generateAces(self):
		return (st.dgamma.ppf(sp.random.uniform(),2.31090686893777,loc=1.1326798219372052,scale=0.2444216507298726))

	def generateServeErrors(self):
		return (st.genpareto.ppf(sp.random.uniform(),-1.2137789267604004,loc=-0.010676270053824767,scale=3.253748366058005))

	def generateReceptionErrors(self):
		return (st.genexpon.ppf(sp.random.uniform(),4.268485924337527,12.738470497820629,9.477022963882748,loc=0.19999999972406748,scale=9.242477349966542))

	def generateDigs(self):
		return (st.gennorm.ppf(sp.random.uniform(),13.559265813652111,loc=18.04587819770307,scale=7.050691188896964))

	def generateBlockSolo(self):
		return (st.gausshyper.ppf(sp.random.uniform(),0.7179450794782269,1.7244661499459655,1.5556958760894994,1.344320120547958,loc=-2.1217189001916225e-31,scale=1.5466288678888593))

	def generateBlockAssists(self):
		return (st.mielke.ppf(sp.random.uniform(),2.001435918818234,8.443425282977927,loc=-0.2975728019624655,scale=3.560414416460757))

	def generateBlockErrors(self):
		return (st.chi.ppf(sp.random.uniform(),0.6028476453249539,loc=-5.627382150985979e-31,scale=0.8976693731712775))

	def generateBallHandlingErrors(self):
		return (st.gilbrat.ppf(sp.random.uniform(),loc=-0.01562975041541776,scale=0.046167162541853796))

	def generatePoints(self):
		return (st.triang.ppf(sp.random.uniform(),0.8298241993297742,loc=8.929408249583366,scale=11.834544863974884))

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