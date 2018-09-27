from Team import Team
import numpy as np
import scipy.stats as st

class WesternIllinois(Team):

	def generateKills(self):
		return (st.burr.ppf(sp.random.uniform(),10.908407214580661,0.5249954618539499,loc=0.0026720283236863485,scale=11.862862304712063))

	def generateHitErrors(self):
		return (st.burr.ppf(sp.random.uniform(),28.221195415546816,0.04351681226076361,loc=2.6247514342326532,scale=3.890886791851254))

	def generateHitAttempts(self):
		return (st.genextreme.ppf(sp.random.uniform(),0.7279355176179068,loc=34.99316119912194,scale=5.792054294085264))

	def generateHitEfficiency(self):
		return (st.fisk.ppf(sp.random.uniform(),2.5110106648178045,loc=0.01217064610084009,scale=0.02758481108717045))

	def generateAssists(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.4819232097176567,loc=10.215605177243809,scale=1.8867113401282982))

	def generateAces(self):
		return (st.bradford.ppf(sp.random.uniform(),5.07205950264985,loc=0.3299999999951898,scale=1.9566392615128663))

	def generateServeErrors(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.792531764580098,loc=1.8443020270083952,scale=0.264563759130207))

	def generateReceptionErrors(self):
		return (st.triang.ppf(sp.random.uniform(),0.3058094230922519,loc=-0.10391138707788608,scale=4.427303620441757))

	def generateDigs(self):
		return (st.triang.ppf(sp.random.uniform(),0.7043045824862135,loc=5.138199142464936,scale=19.212995634708474))

	def generateBlockSolo(self):
		return (st.genlogistic.ppf(sp.random.uniform(),0.35855540183683665,loc=0.6738569159929343,scale=0.09571180311655693))

	def generateBlockAssists(self):
		return (st.gennorm.ppf(sp.random.uniform(),0.38995306211685987,loc=3.329999999990748,scale=0.06356499509062455))

	def generateBlockErrors(self):
		return (st.ncx2.ppf(sp.random.uniform(),1.8690859544350085,0.8964254538712773,loc=-1.0462686305408917e-30,scale=0.19199538085230133))

	def generateBallHandlingErrors(self):
		return (st.gausshyper.ppf(sp.random.uniform(),0.45490192237673976,1.4525034188445871,3.1053289571032963,1.539637578425019,loc=-4.470903938480372e-32,scale=1.1361366067283347))

	def generatePoints(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.2841889335037266,loc=13.963755406523253,scale=2.2979126926136133))

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