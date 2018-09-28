from Team import Team
import numpy as np
import scipy.stats as st

import scipy as sp

class Denver(Team):

	def generateKills(self):
		return (st.burr.ppf(sp.random.uniform(),26.132890114087445,0.298383438019976,loc=-0.06798370448008645,scale=15.560036540951135))

	def generateHitErrors(self):
		return (st.kstwobign.ppf(sp.random.uniform(),loc=-0.054342780146787936,scale=5.871852483695605))

	def generateHitAttempts(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),0.2099020855847405,loc=36.30000000919913,scale=2.0053522922119518))

	def generateHitEfficiency(self):
		return (st.genlogistic.ppf(sp.random.uniform(),0.32755015311311736,loc=0.09897211153602853,scale=0.008574191218758874))

	def generateAssists(self):
		return (st.mielke.ppf(sp.random.uniform(),8.358101352389607,21.329757349283906,loc=-0.10035051019717672,scale=14.368528713614154))

	def generateAces(self):
		return (st.johnsonsu.ppf(sp.random.uniform(),-0.6754802484676561,1.50443382538083,loc=1.0562955579589048,scale=0.8313743687299144))

	def generateServeErrors(self):
		return (st.mielke.ppf(sp.random.uniform(),1.5861898668307681,646759.7255325902,loc=0.2094408346795028,scale=3.1206107431172168))

	def generateReceptionErrors(self):
		return (st.cauchy.ppf(sp.random.uniform(),loc=0.882327743906353,scale=0.3355245224064639))

	def generateDigs(self):
		return (st.genhalflogistic.ppf(sp.random.uniform(),0.48475199268438973,loc=10.999999999360263,scale=6.042840112550186))

	def generateBlockSolo(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),1.609596198984497,loc=-1.6390560307163982e-10,scale=0.14745597062087623))

	def generateBlockAssists(self):
		return (st.burr.ppf(sp.random.uniform(),8.121570526789764,0.1934559213787529,loc=1.1189625375499384,scale=4.382482692234262))

	def generateBlockErrors(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.662244083356633,loc=0.40390411458873776,scale=0.3070788615057158))

	def generateBallHandlingErrors(self):
		return (st.loglaplace.ppf(sp.random.uniform(),2.92128730934994,loc=-0.2558765006591212,scale=0.585876500618718))

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