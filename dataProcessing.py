summitLeagueTeamsList = ['Oral Roberts','South Dakota State','North Dakota State','Denver','Omaha','Purdue Fort Wayne','Western Illinois','South Dakota']

SP = []
K = []
E = []
TA = []	
KEff = []
A= []
SA= []
SE= []
RE= []
DIGS= []
BS= []
BA= []
BE= []
BHE= []
PTS= []

team ="Oral Roberts"
file = open("summitData/"+team +".txt", "r") 
data =  file.readlines()
print(data[0])
