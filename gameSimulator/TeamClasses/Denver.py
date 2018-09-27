from Team import Team
import numpy as np
import scipy.stats as st

class Denver(Team):

	def generateKills(self):
		return (st.laplace.ppf(sp.random.uniform(),loc=14.329999835706213,scale=1.4165962346217467))

	def generateHitErrors(self):
		return (st.laplace.ppf(sp.random.uniform(),loc=4.669999982857521,scale=1.0909876013922444))

	def generateHitAttempts(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),0.2099020855847405,loc=36.30000000919913,scale=2.0053522922119518))

	def generateHitEfficiency(self):
		return (st.burr.ppf(sp.random.uniform(),14.538020602064085,0.11387263767300589,loc=0.014823235520603332,scale=0.09521329799751578))

	def generateAssists(self):
		return (st.mielke.ppf(sp.random.uniform(),8.358101352389607,21.329757349283906,loc=-0.10035051019717672,scale=14.368528713614154))

	def generateAces(self):
		return (st.johnsonsu.ppf(sp.random.uniform(),-0.6754802484676561,1.50443382538083,loc=1.0562955579589048,scale=0.8313743687299144))

	def generateServeErrors(self):
		return (st.tukeylambda.ppf(sp.random.uniform(),1.1145845435061423,loc=2.165007201763923,scale=1.2984990201594213))

	def generateReceptionErrors(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),2.3140296442964123,loc=-2.920587993995034e-09,scale=0.3721309832661599))

	def generateDigs(self):
		return (st.genhalflogistic.ppf(sp.random.uniform(),0.48475199268438973,loc=10.999999999360263,scale=6.042840112550186))

	def generateBlockSolo(self):
		return (st.genpareto.ppf(sp.random.uniform(),-0.3108465894496203,loc=-2.3918272135981217e-09,scale=0.41233790015918226))

	def generateBlockAssists(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.5746825199874679,loc=3.777581247529353,scale=1.2974016811033726))

	def generateBlockErrors(self):
		return (st.gengamma.ppf(sp.random.uniform(),0.3720451175987246,1.6267731475944769,loc=-1.2256516131135416e-31,scale=1.095307256532682))

	def generateBallHandlingErrors(self):
		return (st.gennorm.ppf(sp.random.uniform(),0.5291666348565658,loc=0.329999999852138,scale=0.08174360808134382))

	def generatePoints(self):
		return (st.powerlaw.ppf(sp.random.uniform(),1.8536647366556787,loc=11.681243024658873,scale=9.31875700448797))

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