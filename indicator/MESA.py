import  scipy.signal as signal
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
from spectrum import arma2psd,arburg,arma_estimate

dfcf=pd.read_csv("C:/Users/fx168/Desktop/tmp/000300.csv")
ClosePrice=dfcf.loc[:,['Close']]
ClosePrice=pd.Series(ClosePrice.values.ravel())
aclose=np.array(ClosePrice[0:720])

long=40
#plt.subplot(2,1,1)
#plt.plot(aclose)
aclose=sp.log(aclose)*10
pi=sp.pi
'''
A,P,k=arburg(X=aclose[500:560],order=2)
print(A)
print(P)
print(k)

'''
def s(f):
    a = [0] * long
    for i in range (long):
          a[i]=((P))/abs(1-A[0]*sp.exp(-1*1j* f[i] *2*pi  )-A[1]*sp.exp(-2*1j *f[i]*2*pi  ))**2

    return a

frequency=np.linspace(0,0.5,long)
T=[0]*720
for i in range(0,720-long):
   temp=aclose[i:i+long]
   A,P,k=arburg(X=temp,order=2)
   result=s(frequency)
   #result=np.int64(result)
   tmp=max( enumerate(result),key=lambda x:x[1])
   T[i]=(1/max([tmp[1]]))


print(len(T))
tmp=[]
for i in range(0,len(T)-10):
    tmp.append(np.mean(T[i:i+5]))


#result=s(frequency*2*pi)

plt.subplot(2,1,1)
plt.grid(True)
plt.plot(aclose)
plt.subplot(2,1,2)

plt.plot( [0]*(long+5)+tmp)
plt.grid(True)
plt.show()
