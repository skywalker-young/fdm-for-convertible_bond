import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns

XYD=pd.read_csv("C:/Users/User/Desktop/TC/600571.csv")
'''
print(XYD.iloc[0:2]) 
iloc [0:2]提取前两行数据
 ClosePrice=XYD.loc[:,['Close']] 提取标签为close的所有行;loc[行标签,列标签]
'''

ClosePrice=XYD.loc[:,['Close']]
ClosePrice=pd.Series(ClosePrice.values.ravel())
'''
把数据序列化，这样才能去掉表名好好操作
'''

SC=pd.read_csv("C:/Users/User/Desktop/TC/000001.csv")
Close=SC.loc[:,['Close']]
Close=pd.Series(Close.values.ravel())

daily_returnXYD=[0]*len(ClosePrice)

for i in range(0,len(ClosePrice)-1):
    daily_returnXYD[i]=(ClosePrice[i+1]-ClosePrice[i])/ClosePrice[i]

daily_returnSC=[0]*len((Close))
for i in range(0,len(Close)-1):
    daily_returnSC[i]=(Close[i+1]-Close[i])/Close[i]

#标准化，趋近于正态分布
meanXYD=sp.mean(daily_returnXYD)
sdXYD=sp.sqrt(sp.var(daily_returnXYD))

daily_returnXYD=(daily_returnXYD-meanXYD)/sdXYD

meanSC=sp.mean((daily_returnSC))
sdSC=sp.sqrt(sp.var(daily_returnSC))
daily_returnSC=(daily_returnSC-meanSC)/sdSC
DR= pd.DataFrame({'XYD':daily_returnXYD,'SC':daily_returnSC})

sns.lmplot(x='XYD',y='SC',data=DR)
plt.show()
