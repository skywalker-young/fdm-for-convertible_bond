import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import heapq
from scipy.interpolate import interp1d
# step=200

dfcf = pd.read_csv("C:/Users/User/Desktop/TC/000001.csv")
ClosePrice = dfcf.loc[:, ['Close']]
ClosePrice = pd.Series(ClosePrice.values.ravel())
step = 550

HighPrice = dfcf.loc[:, ['High']]
HighPrice = pd.Series(HighPrice.values.ravel())

LowPrice = dfcf.loc[:, ['Low']]
LowPrice = pd.Series(LowPrice.values.ravel())

aclose = np.array(ClosePrice[0:550])
bhigh = np.array(HighPrice[0:550])

# s1=aclose
s1 = ClosePrice
macd = [0] * step

ema12 = [0] * step
ema12[0] = s1[0]

ema26 = [0] * step
ema26[0] = s1[0]

for i in range(step - 1):
    ema12[i + 1] = (11 / 13 * ema12[i] + 2 / 13 * s1[i + 1])
    ema26[i + 1] = (25 / 27 * ema26[i] + 2 / 27 * s1[i + 1])

dif = [0] * step

for i in range(step):
    dif[i] = (ema12[i] - ema26[i])

dea = [0] * step

for i in range(step - 1):
    dea[i + 1] = 8 / 10 * dea[i] + 2 / 10 * dif[i + 1]
    macd[i + 1] = 2 * (dif[i + 1] - dea[i + 1])

UpperDEA = []
LowerDEA = []

window = 10

for i in range(0, 550 - 1, window):
    tmp = dea[i:i + window]
    a = []
    b = []
    for i in range(window):
        if (tmp[i] >= 0):
            a.append(tmp[i])
        else:
            b.append(tmp[i])
    if (a == []):
        a = [0]  # 如果a是空说明该区间全为负数，b不为空，可以找到min
    if (b == []):
        b = [0]  # 如果是空说明该区间全为正数，a不为空，可以找到max
    UpperDEA.append(max(a))  # 空数组无法比较大小，UpperDEA数据为0
    LowerDEA.append(min(b))

#print(len(UpperDEA)) #55
# print(np.count_nonzero(UpperDEA))
#

Volatility = [0] * step
Volatility[0] = 0
Volatility[1] = abs(dea[1])
# SD中头两个设定好了所以2040-2
for i in range(548):
    Volatility[i + 2] = (abs(dea[i + 2]) - abs(dea[i + 1])) / abs(dea[i + 1])
##去掉5%的极大极小值以获得稳定的波幅
Volatility1 = sorted(Volatility)
# 为了让数组整除，124*15=1860，2040-1860=180，原本要头尾各区102个数据的，现在改成90

Volatility1 = Volatility1[50:500]
# print(Volatility[-1])
#print(len(Volatility1)) #450
aveVol = sp.mean(Volatility1)
#print(aveVol) #0.0046
# 在此基础上认为波幅小于0.0046的不构成波段
stdVol = sp.std(Volatility1)
#print(stdVol) #0.092

#print(len(Volatility)) #550

x=np.linspace(0,550,550)
'''
z1=np.polyfit(x,aclose,8)
p1=np.poly1d(z1)
##插值，没啥大用
ff=interp1d(x,dea)
xnew=np.linspace(min(x),max(x),num=550)
'''
#print(len(Volatility))#550

def wave_guess(arr):
    wn = int(len(arr)/4) #没有经验数据，先设置成1/4。
    print(wn)
    #计算最小的N个值，也就是认为是波谷
    wave_crest = heapq.nlargest(wn, enumerate(arr), key=lambda x: x[1])
    wave_crest_mean = pd.DataFrame(wave_crest).mean()

    #计算最大的5个值，也认为是波峰
    wave_base = heapq.nsmallest(wn, enumerate(arr), key=lambda x: x[1])
    wave_base_mean = pd.DataFrame(wave_base).mean()

    print("######### result #########")
    #波峰，波谷的平均值的差，是波动周期，对于股票就是天。
    wave_period = abs(int( wave_crest_mean[0] - wave_base_mean[0]))
    print("wave_period_day:", wave_period)
    print("wave_crest_mean:", round(wave_crest_mean[1],2))
    print("wave_base_mean:", round(wave_base_mean[1],2))


    ############### 以下为画图显示用 ###############
    wave_crest_x = [] #波峰x
    wave_crest_y = [] #波峰y
    for i,j in wave_crest:
        wave_crest_x.append(i)
        wave_crest_y.append(j)

    wave_base_x = [] #波谷x
    wave_base_y = [] #波谷y
    for i,j in wave_base:
        wave_base_x.append(i)
        wave_base_y.append(j)

    #将原始数据和波峰，波谷画到一张图上
    plt.figure(figsize=(20,10))
    plt.plot(arr)
    plt.plot(wave_base_x, wave_base_y, 'go')#红色的点
    plt.plot(wave_crest_x, wave_crest_y, 'ro')#蓝色的点
    plt.grid()
    plt.show()

'''




ax=plt.subplot(2,1,1)

ax.plot(x,aclose,label='closePrice',color='b')
plt.grid(True)
plt.subplots_adjust(top=None,bottom=None)
ax2=plt.subplot(2,1,2)
plt.plot(x,dea,label='DEA')
#plt.plot(xnew,ff(xnew)) #绘制插值函数，求导母鸡啊

plt.xlabel('weekdays')
#plt.subplots_adjust(   wspace=None, hspace=0)
plt.grid(True)

plt.legend()
plt.show()

'''
wave_guess(dea)
###http://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p04_find_largest_or_smallest_n_items.html
