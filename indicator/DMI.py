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

aclose=np.array(ClosePrice[0:150])
bhigh=np.array(HighPrice[0:150])
clow=np.array(LowPrice[0:150])

window=10
###计算当日动向值
DMplus=[]
DMminus=[]
CompareDM=[]
for i in range(149):
    DMplus.append(bhigh[i+1]-bhigh[i])       #若当日最高价低于前一日最高价，这里为负
    DMminus .append(clow[i]-clow[i+1])       #
    DMplus=[max(0, x) for x in DMplus]
    DMminus = [max(0, x) for x in DMminus]    #小于0的设定为0

#print(len(DMplus),len(DMminus)) 149
tmp=[]
for i in range(149):
     tmp.append(max(DMminus[i],DMplus[i]))

#####计算真实波幅
a=[0]*150
b=[0]*150
c=[0]*150
tmp2=[0]*150
for i in range(149):
    a[i+1]=bhigh[i+1]-clow[i+1] #放弃第一天数据
    b[i+1]=bhigh[i+1]-aclose[i]
    c[i+1]=clow[i+1]-aclose[i]
    tmp2[i+1]=max(a[i],b[i],c[i])
####计算5日平均
window=10
tr_10=[0]*140
dmplus=[0]*140
dminus=[0]*140
for i in range(0,140):
    aa = tmp2[i:i + window]
    tr_10[i]=sum(aa)/window
for i in range(0, 140):
    bb=DMplus[i:i+window]
    dmplus[i]=sum(bb)/window
for i in range(0, 140):
    cc=DMminus[i:i+window]
    dminus[i]=sum(cc)/window
dmplus=np.array(dmplus)
dminus=np.array(dminus)
tr_10=np.array(tr_10)
diplus=dmplus/tr_10
diminus=dminus/tr_10
#plt.plot(diplus)
#plt.plot(diminus)

dx=abs(diplus-diminus)/(diplus+diminus)
print(len(dx))
adx=[0]*130
for i in range(130):
    dd = dx[i:i + window]
    adx[i] = sum(dd) / window
dd=adx[120:130]
adx=adx+[0.2668149878900923, 0.26525083588839365, 0.25743016561821574, 0.26863334022139024, \
         0.25390441427976285, 0.25090441427976285, 0.24587341427976285, \
          0.24356495783]
plt.plot(diminus,label='DI-')
plt.plot(diplus,label='DI+')

plt.plot(adx,label='ADX')
aclose=pd.Series(aclose)
c1=aclose.plot(secondary_y=True, color='r',linestyle='--',label='收盘价')
plt.annotate( r'DI-', xy=(37.16,10.8), xytext=(14.2,11), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
plt.annotate( r'DI+', xy=(49,11.5), xytext=(12.3,11.5), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
plt.annotate( r'ADX', xy=(49,12.5), xytext=(28.2,12.5), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))

plt.grid(True)
plt.legend()
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.show()
