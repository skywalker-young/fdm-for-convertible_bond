import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

index=pd.read_csv("C:/Users/fx168/Desktop/tmp/000001.csv")

ClosePrice=index.loc[:,['Close']]

#ClosePrice=pd.Series(ClosePrice.values.ravel())

aclose=np.array(ClosePrice)
alpha=0.05  #在0，1之间的参数
length=len(aclose)

simpleAVE=[0]*length
simpleAVE[0:30]= [aclose[0] for i in range(30) ]



for i in range(0,length-30):
    simpleAVE[i+30 ]= np.mean(aclose[i:i+30])



EMA=[0]*length
EMA[0]=(aclose[0])

for i in range(length-1):
    EMA[i+1]=0.5*alpha*(aclose[i+1]+aclose[i])+(1-alpha)*EMA[i]


LLT=[0]*length
LLT[0]=aclose[0]
LLT[1]=(1-alpha)*aclose[1]  +alpha*aclose[0]
for i in range(length-2):
    LLT[i+2]=(alpha-alpha**2*0.25)*aclose[i+2]+0.5*alpha**2*aclose[i+1]-(alpha-0.75*alpha**2)*(aclose[i]) \
    +2*(1-alpha)*LLT[i+1]-(1-alpha)**2*LLT[i]
   # LLT[i]=((alpha-alpha**2*0.25)*aclose[i]*aclose[i]+0.5*alpha*aclose[i]- \
           #(alpha-0.75*alpha**2))/(aclose[i]*aclose[i]-2*(1-alpha)*aclose[i]+(1-alpha*alpha))


####
#根据LLT，斜率大于0 的地方买，等于0 持有，小于0 卖
###
k=[0]*108
for i in range(107):
    k[i]=LLT[i+1]-LLT[i]
print(k)
print(LLT)

plt.plot(aclose,label='index close price')
plt.plot(EMA,label='EMA',color='purple')
plt.plot(LLT,label='LLT',color='r')
plt.plot(simpleAVE,label='30_days',color='orange')
plt.yticks([1800,1900,2000,2100,2200,2300,2400,2500], ['1800','1900','2000','2100','2200','2300','2400','2500'])

#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())



plt.grid(True)
plt.legend()
plt.show()

