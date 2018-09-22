# VolleySim
VolleySim is a volleyball simulator built with Python.

Currently I am using data from the 2017 Summit League.

Data Collection:
All the data was collected from the Summit League website(http://www.thesummitleague.org/sports/wvball/2017-18).
Web crawlers extract all the data and saved it into CSV files. Only the TOTALS row is taken from each boxscore.

Data Processing:
The data had to be transformed before being processed. I had to go through and group all stats (such as kills,digs,etc) into the same comma-separated line.

Distribution Fitting:
Used SciPy to figure out best fitting continuos distribution for each and the stat parameters.

Game Simulator:
