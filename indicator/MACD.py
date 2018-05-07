import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import scipy as sp

T=1

step=100

dt=T/step

sig1=0.38

s1=[0]*step

r1=0.05

s1[0]=20



dw=[0]*step

#S+ds

np.random.seed(5348353)

for i in range(step-1):

    dw[i + 1] = np.random.normal(0, 1) * sp.sqrt(dt)

for i in range (step-1):

    s1[i+1]=sig1*s1[i]*dw[i]+r1*s1[i]*dt+s1[i]



window=12

bigwindow=26



macd=[0]*step

ema12=[0]*step

ema12[0]=s1[0]

ema26=[0]*step

ema26[0]=s1[0]


for i in range(step-1):

    ema12[i+1]=(11/13*ema12[i]+2/13*s1[i+1])
    ema26[i + 1] = (25 / 27 * ema26[i] + 2 / 27 * s1[i + 1])

dif=[0]*step

for i in range (step):

    dif[i]=(ema12[i]-ema26[i])

dea=[0]*step

for i in range(step-1):

    dea[i+1]=8/10*dea[i]+2/10*dif[i+1]
    macd[i + 1] = 2 * (dif[i + 1] - dea[i + 1])






a=np.linspace(1,100,100)
plt.grid(True)
#plt.rcParams['font.sans-serif']=['SimHei']#用来显示中文
plt.ylabel('标的资产价格')
plt.title('MACD')
plt.xlabel('日期')
plt.plot( a,ema12,label='EMA12')


plt.plot( a,ema26,label='EMA26')
plt.annotate('MACD由这根EMA26 ', xy=(40, 14.5), xytext=(50, 16), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"), \
             )
plt.annotate('和这根EMA12计算出 ', xy=(40, 13.5), xytext=(60, 14), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"), \
             )

plt.plot(a,s1,label='标的资产价格')
plt.legend(loc="upper right")


#plt.plot(a,macd,label='MACD')
plt.show()

plt.plot( a,dea,label='DEA')


plt.plot( a,dif,label='DIF')
plt.plot(a,macd,label='MACD')
plt.title("MACD")
plt.grid(True)
plt.annotate(r'$DIF=EMA12-EMA26$',xy=(40, -1.00), xytext=(31, -0.75), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"), \
             )
plt.annotate(r'$DEA=preDEA*(8/10)+DEA*(2/10)$',xy=(40, -1.10), xytext=(50, -1.26), \
            arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2")             \
             )
plt.annotate(r'$MACD=2*(DIF-DEA)$',xy=(40, 0.01), xytext=(40, -0.4), \
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

plt.legend()
plt.show()

