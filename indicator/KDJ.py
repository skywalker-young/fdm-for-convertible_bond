import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp

XYD=pd.read_csv("C:/Users/fx168/Desktop/tmp/100.csv")

#print(XYD[0:10])
ClosePrice=XYD.loc[:,['Close']]

ClosePrice=pd.Series(ClosePrice.values.ravel())


#print(a[-1]) 13.87  不把数据转成array类型，无法使用[-1]读取数据
#print(ClosePrice[99]) 13.87
#ClosePrice=ClosePrice[0:100] 复制数组时就是要右边多+1
aclose=np.array(ClosePrice[0:100])

window=10
RSV=[]
K=[]
D=[]
J=[]
K.append(0.5)
D.append(0.5)
for i in range(0,100-window):
     tmp1=aclose[i:i+window]
     high=np.max(tmp1)
     low=np.min(tmp1)
     #for i in range(window):
     RSVtmp=(tmp1[window-1]-low)/(high-low)

     RSV.append(RSVtmp)
     K.append(2 / 3 * K[-1] + 1 / 3 * RSV[-1])
     D.append(2 / 3 * D[-1] + 1 / 3 * K[-1])
     J.append(3 * K[-1] - 2 * D[-1])
'''
plt.plot(K,label='K')
plt.plot(D,label='D')
plt.plot(J,label='J')
#plt.plot(ClosePrice,label='收盘价')
#c1=ClosePrice.plot(secondary_y=True, color='r',linestyle='--')
plt.title('KDJ')
plt.ylabel('KDJ数值 ')
plt.xlabel('日期')
plt.grid(True)
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.legend()
plt.show()
'''
plt.plot(K )

plt.plot(D )
plt.ylabel("KDJ值")
c1=ClosePrice.plot(secondary_y=True, color='r',linestyle='--',label='收盘价')
plt.annotate( r'K线', xy=(21,16.0), xytext=(28,16), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"), \
             )
plt.annotate( r'D线', xy=(86.8,13.5), xytext=(68.8,12.8), \
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"), \
             )
plt.grid(True)
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
plt.legend()
plt.show()

print(len(K))
