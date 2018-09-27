from Team import Team
import numpy as np
import scipy.stats as st

class OralRoberts(Team):

	def generateKills(self):
		return (st.loglaplace.ppf(sp.random.uniform(),426901.5915468705,loc=-751933.6904347753,scale=751947.4404129663))

	def generateHitErrors(self):
		return (st.mielke.ppf(sp.random.uniform(),1.202778058467199,6.357926077132121,loc=3.2939572269777275,scale=3.7253632213321195))

	def generateHitAttempts(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),2.8444258124465147,loc=25.99432538869766,scale=2.8546599046285515))

	def generateHitEfficiency(self):
		return (st.johnsonsu.ppf(sp.random.uniform(),-0.5471988650141528,1.0623906091480586,loc=0.049443132143705444,scale=0.022797760157466533))

	def generateAssists(self):
		return (st.powerlognorm.ppf(sp.random.uniform(),3.569409065723762,0.006474637231807651,loc=-456.6758657405288,scale=472.31762695884777))

	def generateAces(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.0880973555940552,loc=1.1436422679300264,scale=0.6832513394461852))

	def generateServeErrors(self):
		return (st.maxwell.ppf(sp.random.uniform(),loc=0.5397386055742939,scale=0.9285920215741081))

	def generateReceptionErrors(self):
		return (st.semicircular.ppf(sp.random.uniform(),loc=1.1324867688434095,scale=0.9560005174625054))

	def generateDigs(self):
		return (st.gennorm.ppf(sp.random.uniform(),0.8141333584124093,loc=13.32999999990493,scale=1.4191003971057037))

	def generateBlockSolo(self):
		return (st.gilbrat.ppf(sp.random.uniform(),loc=-0.03867581725271682,scale=0.1265623167339466))

	def generateBlockAssists(self):
		return (st.beta.ppf(sp.random.uniform(),2.260178116425948,2.0009713091707892,loc=-0.5939853511295894,scale=6.271007500157726))

	def generateBlockErrors(self):
		return (st.t.ppf(sp.random.uniform(),2.4814782484995117,loc=0.3726438971806972,scale=0.22226750591856928))

	def generateBallHandlingErrors(self):
		return (st.dgamma.ppf(sp.random.uniform(),0.27526604234940877,loc=0.32999999999999996,scale=0.30265478687076264))

	def generatePoints(self):
		return (st.mielke.ppf(sp.random.uniform(),5.454681395326389,21.714422244392214,loc=-0.17538594616397377,scale=19.161470546128157))

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