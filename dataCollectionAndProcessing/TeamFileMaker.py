
import os
for filename in os.listdir("summitFormattedPerSetData/"):
	teamName=filename[:-4].replace(" ", "")
	fw = open("TeamClasses/"+teamName+".py","w")
	fr = open("summitTest/"+filename,"r")
	stats = ['Kills','HitErrors','HitAttempts','HitEfficiency','Assists','Aces','ServeErrors','ReceptionErrors','Digs','BlockSolo','BlockAssists','BlockErrors','BallHandlingErrors','Points']
	
	content="from Team import Team\nimport numpy as np\nimport scipy.stats as st\n\nimport scipy as sp\n\n"
	content += "class "+teamName+"(Team):\n\n\t"
	
	
	lines = fr.readlines()
	distParams = []
	for line in lines:
		distParams.append(line.split(","))
	
	for params in distParams:
		params[-2]="loc="+params[-2]
		params[-1]="scale="+params[-1]
	
	for i in range(len(stats)):
		currDistParams = distParams[i]
		content+= "def generate"+stats[i]+"(self):\n\t\treturn (st."+currDistParams[0]+".ppf(sp.random.uniform(),"
		currDistParams.pop(0)		
		content+=",".join(currDistParams).strip()+"))\n\n\t"
	
	content+="def simulateStatLine(self):\n\t\tstatLine=[]\n\t\t"
	for stat in stats:
		if stat == 'HitEfficiency':
			content+="statLine.append(round((statLine[0]-statLine[1])/float(statLine[2]),3))\n\t\t"
		elif stat == 'Points':
			content+="statLine.append(round((statLine[0]+statLine[5]+statLine[9]+(statLine[10]/2.0))))\n\t\t"
		else:
			content+="statLine.append(round(self.generate"+stat+"()))\n\t\t"
	content+="return(statLine)"	
		
	fw.write(content)
	fw.close()
