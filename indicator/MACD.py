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

for i in range(step-1):
    ema26[i+1]=(25/27*ema26[i]+2/27*s1[i+1])

dif=[0]*step
for i in range (step):
    dif[i]=(ema12[i]-ema26[i])
dea=[0]*step
for i in range(step-1):
    dea[i+1]=8/10*dea[i]+2/10*dif[i+1]

for i in range(step-1):
    macd[i+1]=2*(dif[i+1]-dea[i+1])

plt.plot(ema12)
plt.plot(ema26)
#plt.plot(macd)
plt.plot(s1)
plt.show()
