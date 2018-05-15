import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
import heapq



dfcf = pd.read_csv("C:/Users/fx168/Desktop/tmp/USDCNH60.csv")
ClosePrice = dfcf.loc[:, ['Close']]
ClosePrice = pd.Series(ClosePrice.values.ravel())
step = 2040

#HighPrice = dfcf.loc[:, ['High']]
#HighPrice = pd.Series(HighPrice.values.ravel())

#LowPrice = dfcf.loc[:, ['Low']]
#LowPrice = pd.Series(LowPrice.values.ravel())

aclose = np.array(ClosePrice[0:step])
#bhigh = np.array(HighPrice[0:step])

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


###2040/15=136组数据

dea = dea[0:step]
dayspan = 50
wax_x = []  # 波峰x  记录索引，为天数
wax_y = []  # 波峰y
wane_x = []  # 波谷x
wane_y = []  # 波谷y   记录索引为DEA值
for i in range(0, step, dayspan):
    tmp = dea[i:i + dayspan]
    wave_wax = max(enumerate(tmp), key=lambda x: x[1])
    wave_wane = min(enumerate(tmp), key=lambda x: x[1])

    wax_x.append(wave_wax[0] + i)

    wax_y.append(wave_wax[1])
    wane_y.append(wave_wane[1])
    wane_x.append(wave_wane[0] + i)




newWaneY = []
newWaneX = []
# 两个高坡间隔下确认一个min
for i in range(0, len(wax_y), 2):
    tmp = wane_y[i:i + 2]
    tmp = min(enumerate(tmp), key=lambda x: x[1])
    newWaneY.append(tmp[1])
    # newWaneX.append(wave_wane_y.index(newWaneY))
print('wax_y',len(wax_y))
print('newWaneY:',newWaneY)
print('len newWaneY',len(newWaneY))
for i in range(len(newWaneY)):
    a = wane_y.index(newWaneY[i])       #找到在低谷值中的索引，即天数
    newWaneX.append(wane_x.pop(a - i))  ###把ok的低谷数值取出，每pop一次，数据长度就减少1。记录索引，
                                        ### 为天数

connectx=wax_x+newWaneX       ##调整了所有低谷+未调整的高峰
connectx=sorted(connectx)
#######根据调整了的低谷去整理对应的y值
aaa=[]
for i in range(len(newWaneX)):        #低谷长度
   aaa.append(connectx.index(newWaneX[i]))   #所有天数中找出是第几天

for i in range(len(newWaneX)):
   wax_y.insert(aaa[i],newWaneY[i])         #不调整的高峰数据，+经过调整的低谷数据
############################低谷ok后把不合规的高峰删
newWaxX=[]
newWaxY=[]
a=[]
for i in range(len(newWaneX)):
    tmp=connectx.index(newWaneX[i])
    a.append(tmp)            #把处理好的波谷挑出，波谷之间的间隙就是要比较的波峰
'''
print('a',a)
print('newWaneX',newWaneX)
print('connectx',len(connectx))
print(len(wax_y))
'''
wax_y.pop(28)
connectx.pop(28)
wax_y.pop(30)
connectx.pop(30)
wax_y.pop(30)
connectx.pop(30)
wax_y.pop(33)
connectx.pop(33)

#print(connectx.index(913),connectx.index(983),connectx.index(1029),connectx.index(1116),connectx.index(1141),connectx.index(1150),connectx.index(1292))

Behind=[]
Above=[]
for i in range(len(wax_y)):
     tmp=wax_y[i]
     if (tmp>0):
         Above.append(tmp)
     else:
         Behind.append(tmp)
print('DEA>0 mean',sp.mean(Above))
print('DEA>0 std',sp.std(Above))

print('DEA<0 mean',sp.mean(Behind))
print('DEA<0 std',sp.mean(Behind))



wax_x2 = []  # 波峰x  记录索引，为天数
wax_y2 = []  # 波峰y
wane_x2 = []  # 波谷x
wane_y2 = []  # 波谷y   记录索引为DEA值
for i in range(0, 41, 2):
    tmp = wax_y[i:i + 2]
    wave_wax = max(enumerate(tmp), key=lambda x: x[1])
    wave_wane = min(enumerate(tmp), key=lambda x: x[1])

    wax_x2.append(wave_wax[0] + i)

    wax_y2.append(wave_wax[1])
    wane_y2.append(wave_wane[1])
    wane_x2.append(wave_wane[0] + i)
period=250*abs(sp.mean(wax_x2)-sp.mean(wane_x2))
print('cycle time is ' ,period)
day=[]
for i in range(len(wane_x2)-1):
    tmp=wane_x2[i+1]-wane_x2[i]
    day.append(tmp)
interval=sp.mean(day)*250
print('interval of behind ',interval)


######
#作图
#####
plt.figure(figsize=(6,6))
ax = plt.subplot(2, 1, 1)

ax.plot(aclose, label='closePrice', color='b')
plt.grid(True)
#plt.subplots_adjust(top=None, bottom=None)
ax2 = plt.subplot(2, 1, 2)
################
for i in range(len(connectx)-1):
    plt.plot([connectx[i], connectx[i + 1]], [wax_y[i], wax_y[i + 1]], color='black')
######################
plt.plot(dea, label='DEA', color='crimson')
plt.xlabel('working hours')

plt.grid(True)

plt.legend()
plt.show()

