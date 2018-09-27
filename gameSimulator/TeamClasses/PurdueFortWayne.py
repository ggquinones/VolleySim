from Team import Team
import numpy as np
import scipy.stats as st

class PurdueFortWayne(Team):

	def generateKills(self):
		return (st.dweibull.ppf(sp.random.uniform(),1.4341476257415264,loc=13.226699547615187,scale=1.6928937264191548))

	def generateHitErrors(self):
		return (st.dgamma.ppf(sp.random.uniform(),2.3174735309426886,loc=5.603175323898627,scale=0.5011616102060712))

	def generateHitAttempts(self):
		return (st.rdist.ppf(sp.random.uniform(),1.0033826716430227,loc=28.37936569869501,scale=11.620634301304992))

	def generateHitEfficiency(self):
		return (st.wald.ppf(sp.random.uniform(),loc=0.015634256782858565,scale=0.04536124298174221))

	def generateAssists(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),5.15904016265333,loc=7.99379434155118,scale=0.8109588851192022))

	def generateAces(self):
		return (st.dgamma.ppf(sp.random.uniform(),2.6543863643041803,loc=0.8736975106404405,scale=0.16760369685894028))

	def generateServeErrors(self):
		return (st.ncx2.ppf(sp.random.uniform(),0.009315432138844126,21.271655422935908,loc=0.10402011186885884,scale=0.10611741626948068))

	def generateReceptionErrors(self):
		return (st.johnsonsb.ppf(sp.random.uniform(),-0.02213937077415895,0.8683689509413712,loc=-0.12423842740080404,scale=2.2607115141205636))

	def generateDigs(self):
		return (st.mielke.ppf(sp.random.uniform(),10.015693072050121,9.799800359554865,loc=-0.10723469698792251,scale=16.436090959568325))

	def generateBlockSolo(self):
		return (st.laplace.ppf(sp.random.uniform(),loc=0.33000021849495764,scale=0.26313421501455714))

	def generateBlockAssists(self):
		return (st.foldcauchy.ppf(sp.random.uniform(),4.060876080746402,loc=-6.410628998603777e-10,scale=0.6753368681169081))

	def generateBlockErrors(self):
		return (st.foldnorm.ppf(sp.random.uniform(),0.01541695736123275,loc=-1.057566932367452e-11,scale=0.515969918973695))

	def generateBallHandlingErrors(self):
		return (st.invgamma.ppf(sp.random.uniform(),3.1508397248213678,loc=-0.26988840432381,scale=1.5551980343028902))

	def generatePoints(self):
		return (st.johnsonsu.ppf(sp.random.uniform(),-0.41069007834115423,1.4174376120164769,loc=15.072250589899086,scale=2.544464769605876))

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