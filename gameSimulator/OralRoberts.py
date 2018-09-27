from Team import Team
import numpy as np
import scipy.stats as st

import scipy as sp

class OralRoberts(Team):

	def generateKills(self):
		return (st.loglaplace.ppf(sp.random.uniform(),426901.5915468705,loc=-751933.6904347753,scale=751947.4404129663))

	def generateHitErrors(self):
		return (st.gompertz.ppf(sp.random.uniform(),0.4092038344172457,loc=3.3299999997186607,scale=2.1151905360936194))

	def generateHitAttempts(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),0.38283335274296393,loc=34.37499934718585,scale=2.665845681951714))

	def generateHitEfficiency(self):
		return (st.recipinvgauss.ppf(sp.random.uniform(),0.09890323392174019,loc=-0.06066811950507461,scale=0.011506951820527002))

	def generateAssists(self):
		return (st.gengamma.ppf(sp.random.uniform(),3.5025397729809704,41.593559122649566,loc=-151.80336358619957,scale=160.12875786638722))

	def generateAces(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),1.4786562792775686,loc=0.24999999909918053,scale=0.508898189000853))

	def generateServeErrors(self):
		return (st.laplace.ppf(sp.random.uniform(),loc=2.0000000041317385,scale=0.4971956367185568))

	def generateReceptionErrors(self):
		return (st.fisk.ppf(sp.random.uniform(),3.079776662277532,loc=-0.046205810852082654,scale=1.047434544174652))

	def generateDigs(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),6.871568959706369,loc=4.669999994934597,scale=1.2626538001213774))

	def generateBlockSolo(self):
		return (st.expon.ppf(sp.random.uniform(),loc=0.0,scale=0.237586206897))

	def generateBlockAssists(self):
		return (st.johnsonsb.ppf(sp.random.uniform(),-0.19800625207571357,1.168501753735153,loc=-1.1834221998757841,scale=7.30555450117952))

	def generateBlockErrors(self):
		return (st.t.ppf(sp.random.uniform(),2.4814782484995117,loc=0.3726438971806972,scale=0.22226750591856928))

	def generateBallHandlingErrors(self):
		return (st.dgamma.ppf(sp.random.uniform(),0.27526604234940877,loc=0.32999999999999996,scale=0.30265478687076264))

	def generatePoints(self):
		return (st.gumbel_l.ppf(sp.random.uniform(),loc=17.716635504989682,scale=2.4462866857075793))

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