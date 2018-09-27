from Team import Team
import numpy as np
import scipy.stats as st

class SouthDakotaState(Team):

	def generateKills(self):
		return (st.exponnorm.ppf(sp.random.uniform(),2.7554704544130386,loc=8.199102662515191,scale=0.7484631591992759))

	def generateHitErrors(self):
		return (st.cauchy.ppf(sp.random.uniform(),loc=5.786081326393468,scale=0.547061072409393))

	def generateHitAttempts(self):
		return (st.laplace.ppf(sp.random.uniform(),loc=33.67000000932397,scale=3.1967153084846407))

	def generateHitEfficiency(self):
		return (st.hypsecant.ppf(sp.random.uniform(),loc=0.036212027090567145,scale=0.012666551933568991))

	def generateAssists(self):
		return (st.cauchy.ppf(sp.random.uniform(),loc=9.118849116884437,scale=1.0072097009998604))

	def generateAces(self):
		return (st.recipinvgauss.ppf(sp.random.uniform(),0.1611602550966384,loc=-0.7073514147310666,scale=0.22637718455981065))

	def generateServeErrors(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.669870661557278,loc=1.554390402136995,scale=0.6164685303136903))

	def generateReceptionErrors(self):
		return (st.laplace.ppf(sp.random.uniform(),loc=1.999999702622716,scale=0.6680763103357243))

	def generateDigs(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.6087444400467465,loc=13.38304978208723,scale=1.6641281443183797))

	def generateBlockSolo(self):
		return (st.fatiguelife.ppf(sp.random.uniform(),0.6773060334706106,loc=-0.18726920787027945,scale=0.5162782835972175))

	def generateBlockAssists(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.908994066291565,loc=2.2843497585932413,scale=0.5276070368225694))

	def generateBlockErrors(self):
		return (st.recipinvgauss.ppf(sp.random.uniform(),428948.81160092936,loc=-2.7152704177960136e-12,scale=0.34074896467966576))

	def generateBallHandlingErrors(self):
		return (st.recipinvgauss.ppf(sp.random.uniform(),1052423.767440367,loc=-1.9895073921441977e-13,scale=0.26374108540532937))

	def generatePoints(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),2.5769229055287513,loc=8.669999975342943,scale=1.352299501688802))

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