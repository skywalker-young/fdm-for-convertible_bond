import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

FR=pd.read_csv("C:/Users/fx168/Desktop/tmp/FR.csv")


Account=FR.loc[:,['Account']]
Account=pd.Series(Account.values.ravel())

Add=FR.loc[:,['Add']]
Add=pd.Series(Add.values.ravel())

Withdraw=FR.loc[:,['Withdraw']]
Withdraw=pd.Series(Withdraw.values.ravel())

Profit=FR.loc[:,['Profit']]
Profit=pd.Series(Profit.values.ravel())

NAV=[]
share=[]
share.append(Account[0])

NAV.append(Account[0]/share[0])
#print(NAV)  #NAV=1 初始净值为1
#NAV 代表多少元1股份
a=0
b=0
for i in range(59):

     tmp=(Account[i]+Profit[i])/share[i] #计算每一个份额盈利或亏损后的价值
     a=Add[i]/tmp  #多加钱买到的股数
     b=Withdraw[i]/tmp #取现卖出的股数
     share.append(share[i]+a-b)
     #tmp2=(Account[i]+Profit[i]+Add[i]+Withdraw[i])
     tmp3=(Account[i+1])/(share[i+1])
     NAV.append(tmp3)



percent=[]
#print(len(NAV))60
for i in range(59):
    tmp=(NAV[i+1]-NAV[i])/NAV[i]
    percent.append(tmp)
'''
data=pd.DataFrame(percent)
data.to_csv('percent.csv' )
'''
print(Account)
print(NAV)
print(percent)
#plt.plot(NAV,label='net value')

#plt.legend()
#plt.show()








'''
testa=[]
testb=[]

test1=[-1,-1,-1,-2,-3,-4,5,6]
for i in range(0,7,2):
    a = []
    b = []
    tmp=(test1[i:i+2])
    print('tmp:',tmp)
    for aa in range(2):
       if (tmp[aa]>=0):
           a.append(tmp[aa])
       else:
           b.append(tmp[aa])

    if (a==[]):
          a=[0]
    if (b==[]):
        b=[0]
    testa.append(max(a))
    testb.append(min(b))
    print('testa ' , testa)
    print('testb', testb)

print()
'''