import requests
import re
from bs4 import BeautifulSoup
from pyexcel_ods import save_data
from collections import OrderedDict

# This page has the code to process a BoxScore page from the Summit League

def getSoup(link):
	url = link
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'html.parser')
	return soup



def getTeamBoxscore(teamNum,allDivTables):
	currTable = allDivTables[teamNum].find("table") # First table is game overview stuff, Second is Team1 then Team2.
	tableRows = currTable.find_all("tr")
	sheet =[]
	for tr in tableRows:
		td = tr.find_all("td")
		th = tr.find_all("th")
		data = td + th
		row = []
		for cell in data:
			noWeirdSpacing = re.sub("(\s)+[*]"," ",cell.text.strip().encode("utf-8"),0, re.DOTALL)			
			row.append(noWeirdSpacing)		
		sheet.append(row)
	return sheet

def extractTotalsRow(varSheet):
	totalsRow = varSheet[-1]
	totalsRow.pop(0)
	totalsRow = [float(i) for i in totalsRow]
	return totalsRow

def extractBoxScoreLinks():
	with open("linksToBoxScores.txt") as f:
		links = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
		links = [x.strip() for x in links] 
		return links

def extractTeam(boxscore):
	return boxscore[0][0]

def isSummitLeagueTeam(boxscore):
	summitLeagueTeamsList = ['Oral Roberts','South Dakota State','North Dakota State','Denver','Omaha','Purdue Fort Wayne','Western Illinois','South Dakota']
	return( extractTeam(boxscore) in summitLeagueTeamsList)

def getSetsPlayed(spans):
	team1 = re.sub( '\s+', ' ', spans[0].text ).strip()
	sets = []
	sets.append(team1[-1])
	team2 = re.sub( '\s+', ' ', spans[1].text ).strip()
	sets.append(team2[-1])
	setsPlayed = int(sets[0])+int(sets[1])
	return setsPlayed

def addToCSV(teamName,totals):
	f=open("summitRawPerSetData/"+teamName+".txt", "a+")
	totals = [str(i) for i in totals]
	line = ','.join(totals)
	#line = line[:-1]
	f.write(line + "\n")
	f.close()

def makeMatchTotalsPerSet(matchTotals,sets):
	return [round((i/sets),2) for i in matchTotals]

def processLinks():	
		
	links = extractBoxScoreLinks()
	ct = 0
	for link in links:		
		soup = getSoup(link)
		sauce = soup.find_all("div",class_="stats-fullbox clearfix")
		setsPlayed = getSetsPlayed(soup.find_all("span", class_="stats-header"))
		team1BXSC = getTeamBoxscore(1,sauce)
		team2BXSC = getTeamBoxscore(2,sauce)
		print("Processing: "+ extractTeam(team1BXSC) +" vs. "+ extractTeam(team2BXSC))
		print("Sets played " + str(setsPlayed))
		if isSummitLeagueTeam(team1BXSC):			
			addToCSV(extractTeam(team1BXSC),makeMatchTotalsPerSet(extractTotalsRow(team1BXSC),setsPlayed))
			# For match totals
			#addToCSV(extractTeam(team1BXSC),extractTotalsRow(team1BXSC))
		if isSummitLeagueTeam(team2BXSC):		
			addToCSV(extractTeam(team2BXSC),makeMatchTotalsPerSet(extractTotalsRow(team2BXSC),setsPlayed))
			# For match totals
			#addToCSV(extractTeam(team2BXSC),extractTotalsRow(team2BXSC))
	

processLinks()
