import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

dfcf=pd.read_csv("C:/Users/fx168/Desktop/tmp/300059.csv")
ClosePrice=dfcf.loc[:,['Close']]
ClosePrice=pd.Series(ClosePrice.values.ravel())

HighPrice=dfcf.loc[:,['High']]
HighPrice=pd.Series(HighPrice.values.ravel())

LowPrice=dfcf.loc[:,['Low']]
LowPrice=pd.Series(LowPrice.values.ravel())

OpenPrice=dfcf.loc[:,['Open']]
OpenPrice=pd.Series(OpenPrice.values.ravel())
aclose=np.array(ClosePrice[0:150])
bhigh=np.array(HighPrice[0:150])
clow=np.array(LowPrice[0:150])
dopen=np.array(OpenPrice[0:150])

AR=[]
BR=[]

window=10

for i in range(140):
    a=0
    b=0
    tmpO=dopen[i:i+window]
    tmpL=clow[i:i+window]
    tmpH=bhigh[i:i+window]
    tmpC=aclose[i:i+window]
    AR.append(np.sum(tmpH-tmpO)/np.sum(tmpO-tmpL))
    for i in range(8):
        a=a+(tmpH[i+1]-tmpC[i])
        b=b+(tmpC[i]-tmpL[i+1])
    BR.append(a/b)

xx=np.linspace(10,150,140)
plt.plot(xx,AR,label='AR')
plt.plot(xx,BR,label='BR')

pp=pd.Series(aclose)
pp.plot(secondary_y=True, color='r',linestyle='--',label='收盘价')

plt.ylabel('资产价格')

plt.annotate( r'AR人气', xy=(63,12), xytext=(43.4,12.5), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
plt.annotate( r'BR意愿', xy=(62.7,10.5), xytext=(37.7,11.5), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.grid(True)
plt.legend()
plt.show()
