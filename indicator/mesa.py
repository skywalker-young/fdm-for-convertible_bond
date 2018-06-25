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

long=len(aclose)
#plt.subplot(2,1,1)
#plt.plot(aclose)
aclose=sp.log(aclose)*10
A,P,k=arburg(X=aclose,order=2)
print(A)
print(P)
print(k)
pi=sp.pi
frequency=np.linspace(0,1,long)

def s(f):
    a = [0] * long
    for i in range (long):
          a[i]=(sp.sqrt(P))/abs(1-A[0]*sp.exp(-1j*2*pi*f[i])-A[1]*sp.exp(-1j*2*pi*f[i]*2))**2

    return a

result=s(frequency *2*pi)

N=len(aclose)# N一定要偶数
n=N/2
A0=sp.mean(aclose)
print(A0) #2602.18
plt.subplot(2,1,1)
plt.plot(aclose)
plt.subplot(2,1,2)
plt.plot(frequency ,result)
plt.show()

