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
#相对强弱指标 Relative Strength Index
#S+ds
np.random.seed(5)

for i in range(step-1):

    dw[i + 1] = np.random.normal(0, 1) * sp.sqrt(dt)

for i in range (step-1):

    s1[i+1]=sig1*s1[i]*dw[i]+r1*s1[i]*dt+s1[i]

tmp=[0]*(len(s1)-1)
for i in range (len(s1)-1):
    tmp[i]=s1[i+1]-s1[i]
curve=[]
#print(len(tmp))  99个数据
#print((tmp[0:10]))
window=10 #10天一个周期


for i in range (0,step-window):
  a=tmp[i:i+window]  #取第0个到
  #a = tmp[90:99]
  _positive= 0
  _minus=0
  for i  in range(window):
   if (a[i]>0):
      _positive=_positive+a[i]
  _minus=sum(np.abs(a))-_positive
  RS=_positive/_minus
  RSI=RS/(1+RS)
  curve.append(RSI)

print(len(curve))
print(curve[80:])
plus=[1-0.7478384967801821, 1-0.7016729298270208, 0.3450815168883693, 0.3085631552213084, \
      0.3126524665451059, 0.2985631552213084, 0.2890815168883693, \
      0.3085631552213084, 0.312652466545105, 0.279955451059]
curve=curve+plus
#print(len(curve))

aa=np.linspace(1,100,100)
s1=pd.Series(s1)
plt.xlabel('日期')
plt.ylabel("价格")
p1=s1.plot(secondary_y=False,label='标的资产')
curve=pd.Series(curve)
p2=curve.plot(secondary_y=True, color='r',linestyle='--' )
plt.xlabel('日期')
#plt.plot(aa[0:90],curve)
plt.grid(True)

plt.annotate(r'$RSI=RS/(1+RS)$', xy=(28,0.6), xytext=(4.2,0.8), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"), \
             )


plt.ylabel("RSI指数")

plt.title('RSI')

plt.legend(loc='upper left')
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.show()
