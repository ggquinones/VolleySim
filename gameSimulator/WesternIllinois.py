from Team import Team
import numpy as np
import scipy.stats as st

import scipy as sp

class WesternIllinois(Team):

	def generateKills(self):
		return (st.exponnorm.ppf(sp.random.uniform(),0.42979500547744476,loc=9.906887242456603,scale=2.0697081775929322))

	def generateHitErrors(self):
		return (st.gompertz.ppf(sp.random.uniform(),0.11760672971554662,loc=2.6699999873025733,scale=1.1623341601789143))

	def generateHitAttempts(self):
		return (st.powerlaw.ppf(sp.random.uniform(),2.0735464805199113,loc=20.968703400637903,scale=21.70129660018175))

	def generateHitEfficiency(self):
		return (st.beta.ppf(sp.random.uniform(),0.7282885529844242,2.0858208905596998,loc=0.019999999999999997,scale=0.09464084929579927))

	def generateAssists(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.4819232097176567,loc=10.215605177243809,scale=1.8867113401282982))

	def generateAces(self):
		return (st.truncexpon.ppf(sp.random.uniform(),1.1351085338125135,loc=0.3297789942339232,scale=1.6916640696885987))

	def generateServeErrors(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),2.813028215730471,loc=0.6699999984500669,scale=0.3909007984560715))

	def generateReceptionErrors(self):
		return (st.johnsonsb.ppf(sp.random.uniform(),0.4716946436833792,0.8439135259804513,loc=0.05498668189502057,scale=4.352768341865771))

	def generateDigs(self):
		return (st.burr.ppf(sp.random.uniform(),15.713022302514958,0.12088571716934121,loc=5.40732575197367,scale=15.730329405783209))

	def generateBlockSolo(self):
		return (st.tukeylambda.ppf(sp.random.uniform(),1.2469531227319564,loc=0.40000154189480586,scale=0.4987831717633302))

	def generateBlockAssists(self):
		return (st.gennorm.ppf(sp.random.uniform(),0.38995306211685987,loc=3.329999999990748,scale=0.06356499509062455))

	def generateBlockErrors(self):
		return (st.ncx2.ppf(sp.random.uniform(),1.8690859544350085,0.8964254538712773,loc=-1.0462686305408917e-30,scale=0.19199538085230133))

	def generateBallHandlingErrors(self):
		return (st.wald.ppf(sp.random.uniform(),loc=-0.07812385387314823,scale=0.3179154181541082))

	def generatePoints(self):
		return (st.gumbel_l.ppf(sp.random.uniform(),loc=15.360074059006038,scale=2.642504287785417))

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