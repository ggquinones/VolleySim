from Team import Team
import numpy as np
import scipy.stats as st

import scipy as sp

class SouthDakotaState(Team):

	def generateKills(self):
		return (st.powerlognorm.ppf(sp.random.uniform(),0.004300938230421624,0.028679642500809413,loc=3.348411632861541,scale=3.847031161883283))

	def generateHitErrors(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),2.5255417410846563,loc=3.999999984035714,scale=0.6942640058562178))

	def generateHitAttempts(self):
		return (st.kstwobign.ppf(sp.random.uniform(),loc=20.784895149323244,scale=16.44800500439353))

	def generateHitEfficiency(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.7730207206383857,loc=0.03538420789392949,scale=0.008452028722824825))

	def generateAssists(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.7024399625164692,loc=9.382586035126202,scale=0.8726684253519537))

	def generateAces(self):
		return (st.burr.ppf(sp.random.uniform(),4.620441722036089,0.1643841325298348,loc=-5.786276094056286e-28,scale=1.6814177284602594))

	def generateServeErrors(self):
		return (st.gompertz.ppf(sp.random.uniform(),0.16061547115507752,loc=0.32999998653773155,scale=0.7796271027665389))

	def generateReceptionErrors(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),0.4523629107768415,loc=1.9997376008930194,scale=0.5316610345275974))

	def generateDigs(self):
		return (st.vonmises_line.ppf(sp.random.uniform(),0.5047445862300082,loc=13.665000021292364,scale=2.1215354075475323))

	def generateBlockSolo(self):
		return (st.frechet_l.ppf(sp.random.uniform(),55364221.89555077,loc=16006120.989893766,scale=16006120.714681223))

	def generateBlockAssists(self):
		return (st.gumbel_l.ppf(sp.random.uniform(),loc=2.880562252960062,scale=1.2905125703476044))

	def generateBlockErrors(self):
		return (st.chi2.ppf(sp.random.uniform(),1.8206012100861269,loc=-1.4842498146960767e-30,scale=0.23059100904060556))

	def generateBallHandlingErrors(self):
		return (st.loglaplace.ppf(sp.random.uniform(),0.7849263730843716,loc=-3.0199720147208965e-26,scale=0.3308448438751081))

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