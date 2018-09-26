# VolleySim
<<<<<<< HEAD

=======
VolleySim is a volleyball simulator built with Python.<br>

Currently I am using data from the 2017 Summit League.<br>

Data Collection:<br>
All the data was collected from the Summit League website(http://www.thesummitleague.org/sports/wvball/2017-18).
Web crawlers extract all the data and saved it into CSV files. Only the TOTALS row is taken from each boxscore.

Data Processing:<br>
The data had to be transformed before being processed. I had to go through and group all stats (such as kills,digs,etc) into the same comma-separated line.

Distribution Fitting:<br>
Used SciPy to figure out best fitting continuos distribution for each and the stat parameters.

Game Simulator:<br>


Order of Stats<br>

SP	K	E	TA	K%	A	SA	SE	RE	DIGS	BS	BA	BE	BHE	PTS<br>

SP = Sets Played<br>
K = kills<br>
E = hitting error<br>
TA = Total hitting Attempts<br>
K% = Kill Efficiency<br>
A = Assists<br>
SA = Service Ace<br>
SE = Service Error<br>
RE = Reception Error<br>
DIGS = Digs<br>
BS = Block Solo<br>
BA = Block Assists<br>
BE = Blocking Error<br>
BHE = Ball Handling Error<br>
PTS = Points<br>
>>>>>>> 52a2a2f63dedcc936a44c0e45766c4032d6a8dce
