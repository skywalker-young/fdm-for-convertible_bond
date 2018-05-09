import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

dfcf=pd.read_csv("C:/Users/fx168/Desktop/tmp/300059.csv")
ClosePrice=dfcf.loc[:,['Close']]
ClosePrice=pd.Series(ClosePrice.values.ravel())


aclose=np.array(ClosePrice[0:150])


window=10#N days
f=(window-1)/(window+1)
TRIX=[]
coefficient=np.linspace(1,window,window)
for i in range(window):
    coefficient[i]=(coefficient[i]*(coefficient[i]+1))/2
ff=[1,f,f**2,f**3,f**4,f**5,f**6,f**7,f**8,f**9]


for i in range(140):
   tmp=aclose[i:i+window]
   TRIX.append( \
       (1-f)**3*(tmp[9]+coefficient[1]*ff[1]*tmp[8]+coefficient[2]*ff[2]*tmp[7] \
                    +coefficient[3]*ff[3]*tmp[6]+coefficient[4]*ff[4]*tmp[5]\
                 +coefficient[5]*ff[5]*tmp[4]+coefficient[6]*ff[6]*tmp[3] \
                 +coefficient[7]*ff[7]*tmp[2]+coefficient[8]*ff[8]*tmp[1] \
                 +coefficient[9]*ff[9]*tmp[0]\
                                  )
       )


print(len(TRIX))
TRMA=[]
for i in range(130):
    tmp=TRIX[i:i+window]
    TRMA.append(np.mean(tmp))
xx=np.linspace(1,150,150)
xxx=np.linspace(10,150,140)
x=np.linspace(20,150,130)
plt.plot(xxx,TRIX,label='TRIX')
plt.plot(x,TRMA,label='TRMA')

plt.xlabel('日期')
pp=pd.Series(aclose)
pp.plot(secondary_y=True, color='r',linestyle='--',label='收盘价')

plt.ylabel('资产价格')

plt.annotate( r'TRIX', xy=(87.45,12), xytext=(55.37,12.44), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
plt.annotate( r'TRMA', xy=(140,11), xytext=(132,10), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.grid(True)
plt.legend()
plt.show()
