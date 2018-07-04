import scipy as sp
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_finance as mpf #just using pip install in conda prompt

dfcf=pd.read_csv("C:/Users/fx168/Desktop/tmp/cebm.csv")
ClosePrice=dfcf.loc[:,['Close']]
ClosePrice=pd.Series(ClosePrice.values.ravel())
aclose=np.array(ClosePrice   )

OpenPrice=dfcf.loc[:,['Open']]
OpenPrice=pd.Series(OpenPrice.values.ravel())
bopen=np.array(OpenPrice)

HighPrice=dfcf.loc[:,['High']]
HighPrice=pd.Series(HighPrice.values.ravel())
chigh=np.array(HighPrice)

LowPrice=dfcf.loc[:,['Low']]
LowPrice=pd.Series(LowPrice.values.ravel())
dlow=np.array(LowPrice)




X=[1,2,3,4,5]

#print(Y)

#slope,intercept,rvalue,pvalue,stderr=sp.stats.linregress(X,Y)
#a=[1]*5
#a=[intercept for i in range(5)]
#k=[slope for i in range(5)]
#fitY=slope*X+intercept


long=len(aclose)
outcome=[]
for i in range(long-5):
    tmp=aclose[i:i+5]
    slope, intercept, rvalue, pvalue, stderr = sp.stats.linregress(X, tmp)
    #c=[intercept for i in range(5)]
    tmpFIT=slope*X[4]+intercept
    outcome.append(tmpFIT )
#print(len(outcome))
print('LRC5',outcome[-1])
print('LAST',aclose[-1])
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
plt.plot(np.linspace(4,22,len(outcome)),outcome,label='LRC5')
mpf.candlestick2_ohlc(ax=ax,opens=bopen,closes=aclose,highs=chigh,lows=dlow,colorup='red',colordown='green',alpha=1,width=0.5)
plt.show()
