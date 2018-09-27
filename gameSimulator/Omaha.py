from Team import Team
import numpy as np
import scipy.stats as st

import scipy as sp

class Omaha(Team):

	def generateKills(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.7472966802547036,loc=13.11671183073475,scale=0.9917324065239239))

	def generateHitErrors(self):
		return (st.gennorm.ppf(sp.random.uniform(),3.8847656291093693,loc=5.634276557010871,scale=2.579792934818464))

	def generateHitAttempts(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.9190363207286407,loc=38.97259733847758,scale=5.438804825601784))

	def generateHitEfficiency(self):
		return (st.t.ppf(sp.random.uniform(),1.4893822345213121,loc=0.04126776031321075,scale=0.011715591202172243))

	def generateAssists(self):
		return (st.dgamma.ppf(sp.random.uniform(),1.8446549980152722,loc=11.819082195664901,scale=0.8466793546277281))

	def generateAces(self):
		return (st.loglaplace.ppf(sp.random.uniform(),1.6381643454729786,loc=0.31184986099099504,scale=0.9381501255089277))

	def generateServeErrors(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),2.5160605918123222,loc=1.1999999991501211,scale=0.5271772006273626))

	def generateReceptionErrors(self):
		return (st.dweibull.ppf(sp.random.uniform(),2.167566800111749,loc=1.017568426343793,scale=0.6297521284866952))

	def generateDigs(self):
		return (st.gausshyper.ppf(sp.random.uniform(),1.5148705551364543,0.8468176848609184,0.6118602197050235,1.1202301356511857,loc=7.8648466556986785,scale=14.465153344301322))

	def generateBlockSolo(self):
		return (st.dweibull.ppf(sp.random.uniform(),2.0650494341317103,loc=0.47040241304250047,scale=0.32762475617289777))

	def generateBlockAssists(self):
		return (st.gausshyper.ppf(sp.random.uniform(),0.8098401881253808,1.2320197930638122,0.942615255530351,0.8820183917940483,loc=1.3299999999999998,scale=4.791688381454943))

	def generateBlockErrors(self):
		return (st.invgamma.ppf(sp.random.uniform(),5.643251992502286,loc=-0.42662146958196256,scale=4.073803080555447))

	def generateBallHandlingErrors(self):
		return (st.halflogistic.ppf(sp.random.uniform(),loc=-1.471379994627516e-08,scale=0.23105413115404028))

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