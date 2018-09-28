from Team import Team
import numpy as np
import scipy.stats as st

import scipy as sp

class NorthDakotaState(Team):

	def generateKills(self):
		return (st.loglaplace.ppf(sp.random.uniform(),9.140362828908664,loc=-0.06133926630147376,scale=12.73133926805141))

	def generateHitErrors(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),0.9039371666869455,loc=5.975659328116483,scale=1.067719815541137))

	def generateHitAttempts(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.0827683323717796,loc=39.86518394037607,scale=3.645746241796284))

	def generateHitEfficiency(self):
		return (st.dgamma.ppf(sp.random.uniform(),0.8311253136582613,loc=0.05000000000000002,scale=0.024228418419151673))

	def generateAssists(self):
		return (st.loglaplace.ppf(sp.random.uniform(),9.690810421800144,loc=-0.08813019125264077,scale=11.838130191319449))

	def generateAces(self):
		return (st.johnsonsb.ppf(sp.random.uniform(),0.4282314217105115,0.6853047660891407,loc=0.18954343528598433,scale=3.677371271114252))

	def generateServeErrors(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),2.5132165586512976,loc=0.32999999901390253,scale=0.3968782970600422))

	def generateReceptionErrors(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),0.2540138072930136,loc=0.9987842428524847,scale=0.3186968738902657))

	def generateDigs(self):
		return (st.burr.ppf(sp.random.uniform(),34.4030841627804,0.1339898874708293,loc=-0.19568977992651165,scale=23.27982338751832))

	def generateBlockSolo(self):
		return (st.mielke.ppf(sp.random.uniform(),1.5213571974754911,3.54796920878613,loc=-0.039063363357272965,scale=1.1331381363752724))

	def generateBlockAssists(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),3.701557688639376,loc=-6.608027406779798e-11,scale=0.7712747158192153))

	def generateBlockErrors(self):
		return (st.foldnorm.ppf(sp.random.uniform(),1.1316340905658877,loc=-8.903321644339667e-10,scale=0.48373271039104493))

	def generateBallHandlingErrors(self):
		return (st.t.ppf(sp.random.uniform(),4.280689210670266,loc=0.22532903637589324,scale=0.22180149313249545))

	def generatePoints(self):
		return (st.burr.ppf(sp.random.uniform(),2984.1720380137444,0.004638851244009967,loc=-22.26576683693956,scale=41.308631301991866))

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