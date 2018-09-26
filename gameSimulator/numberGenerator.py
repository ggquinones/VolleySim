import numpy as np
import scipy.stats as st

q=np.random.rand(1000)
a=1.3411088915379294
result=st.powerlaw.ppf(q,a,loc=28.320654428184774,scale=35.6793455750062)
# Denver Kills
# powerlaw,1.3411088915379294,28.320654428184774,35.6793455750062
for item in result:
	print(int(item))
