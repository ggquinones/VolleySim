from Team import Team
import numpy as np
import scipy.stats as st

import scipy as sp

class PurdueFortWayne(Team):

	def generateKills(self):
		return (st.loglaplace.ppf(sp.random.uniform(),8.75109052039611,loc=-0.06813161786820933,scale=12.868131628654055))

	def generateHitErrors(self):
		return (st.halfgennorm.ppf(sp.random.uniform(),6.018471708863849,loc=3.329999999933459,scale=4.990193813053784))

	def generateHitAttempts(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),3.8967143127290687,loc=29.19999999209545,scale=2.425416352410032))

	def generateHitEfficiency(self):
		return (st.invgauss.ppf(sp.random.uniform(),0.3440907107651894,loc=0.009342745575397896,scale=0.1322230162121822))

	def generateAssists(self):
		return (st.pearson3.ppf(sp.random.uniform(),0.8704555054123483,loc=12.676077926032171,scale=1.6265672678297887))

	def generateAces(self):
		return (st.dgamma.ppf(sp.random.uniform(),2.6543863643041803,loc=0.8736975106404405,scale=0.16760369685894028))

	def generateServeErrors(self):
		return (st.triang.ppf(sp.random.uniform(),0.377369237946484,loc=0.32817301203735827,scale=4.4302152234681955))

	def generateReceptionErrors(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),0.35241301282765447,loc=0.9992089802471067,scale=0.31856167731203777))

	def generateDigs(self):
		return (st.hypsecant.ppf(sp.random.uniform(),loc=16.451483734440167,scale=1.9981049039097751))

	def generateBlockSolo(self):
		return (st.laplace.ppf(sp.random.uniform(),loc=0.33000021849495764,scale=0.26313421501455714))

	def generateBlockAssists(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),4.060876080746402,loc=-6.410628998603777e-10,scale=0.6753368681169081))

	def generateBlockErrors(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),1.284885722167917,loc=-5.927609313714863e-11,scale=0.2208576318769276))

	def generateBallHandlingErrors(self):
		return (st.ncx2.ppf(sp.random.uniform(),1.5704054463594597,1.2917183374538326,loc=-1.5664429498306135e-29,scale=0.15621551098645808))

	def generatePoints(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),4.715706307870745,loc=10.32999999710357,scale=1.1051609302771994))

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