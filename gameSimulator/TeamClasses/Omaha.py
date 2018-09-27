from Team import Team
import numpy as np
import scipy.stats as st

class Omaha(Team):

	def generateKills(self):
		return (st.burr.ppf(sp.random.uniform(),26.973813089202267,0.1505688088158348,loc=2.3710776730142937,scale=12.719296393601937))

	def generateHitErrors(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.4652500874528203,loc=5.895497652592352,scale=1.3909275173752644))

	def generateHitAttempts(self):
		return (st.johnsonsb.ppf(sp.random.uniform(),0.021359735011360848,0.6882112715971311,loc=28.070982941505086,scale=20.87077979614709))

	def generateHitEfficiency(self):
		return (st.johnsonsu.ppf(sp.random.uniform(),-0.6298164474030736,0.8197074312030797,loc=0.035012057715403895,scale=0.00929119005495661))

	def generateAssists(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.8446549980152722,loc=11.819082195664901,scale=0.8466793546277281))

	def generateAces(self):
		return (st.exponnorm.ppf(sp.random.uniform(),3.171670244258717,loc=0.6493698321307488,scale=0.2524295560932943))

	def generateServeErrors(self):
		return (st.dweibull.ppf(sp.random.uniform(),0.9446995363416097,loc=2.670000000000001,scale=0.6813843655001979))

	def generateReceptionErrors(self):
		return (st.dweibull.ppf(sp.random.uniform(),2.167566800111749,loc=1.017568426343793,scale=0.6297521284866952))

	def generateDigs(self):
		return (st.johnsonsb.ppf(sp.random.uniform(),-0.3915584658374403,0.68771635274378,loc=7.611686204963272,scale=14.984403586503765))

	def generateBlockSolo(self):
		return (st.tukeylambda.ppf(sp.random.uniform(),1.0995965695865157,loc=0.500000182812081,scale=0.5497984858127958))

	def generateBlockAssists(self):
		return (st.truncexpon.ppf(sp.random.uniform(),1.064981266914188,loc=1.3299974119775504,scale=4.385056973094125))

	def generateBlockErrors(self):
		return (st.fatiguelife.ppf(sp.random.uniform(),0.8658730839842746,loc=-0.11022248740059826,scale=0.3991697593383258))

	def generateBallHandlingErrors(self):
		return (st.exponnorm.ppf(sp.random.uniform(),4349.172657471143,loc=-0.00024167810476004677,scale=6.717934842649237e-05))

	def generatePoints(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.5898226053909916,loc=16.114149548844043,scale=2.672666151486057))

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