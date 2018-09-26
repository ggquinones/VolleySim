summitLeagueTeamsList = ['Oral Roberts','South Dakota State','North Dakota State','Denver','Omaha','Purdue Fort Wayne','Western Illinois','South Dakota']


def collectStats(team):
	stats = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	#file = open("summitRawData/"+team +".txt", "r") 
	file = open("summitRawPerSetData/"+team +".txt", "r") 
	data =  file.readlines()
	for statLine in data:
		statLine = statLine.strip()
		statList = statLine.split(",")
		index=0
		for stat in statList:
			stats[index].append(stat)
			index+=1
	file.close()
	return stats

def makeNewStatsFile(team,stats):
	#file = open("summitFormattedData/"+team+".txt","a+")
	file = open("summitFormattedPerSetData/"+team+".txt","a+")
	for line in stats:
		file.write(",".join(line) + "\n")
	file.close()
	
def Runner():
	for team in summitLeagueTeamsList:
		stats = collectStats(team)
		makeNewStatsFile(team,stats)
	
Runner();
