#GARCH-NoVaS模型文献：“Financial time series and volatility prediction using NoVaS transformations”，作者：DN Politis，DD Thomakos，2006， 
#下载地址：http://www.math.ucsd.edu/~politis/PAPER/politisthomakosBOOK.pdf
#EGARCH(1,1)模型文献：Conditional Heteroskedasticity in Asset Returns: A New Approach，作者：Daniel B. Nelson，《Econometrica》 , 1991 ，
#下载地址：http://web.pdx.edu/~crkl/ec572/readings/Nelson91.pdf
#GJR-GARCH(1,1,1)模型文献：On the Relation between the Expected Value and the Volatility of the Nominal Excess Return on Stocks，作者：Lawrence R. Glosten ， Ravi Jagannathan ， David E. Runkle，《The Journal of Finance》 
#, 1993 , 下载地址：https://core.ac.uk/download/pdf/6717634.pdf


import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import kurtosis
from arch import arch_model

start = '20130501'
end = '20180606'
index300_data = DataAPI.MktIdxdGet(ticker='000300', beginDate=start, endDate=end, field="tradeDate,closeIndex")
index300_data=index300_data.set_index('tradeDate')
index300_data.head()


index300_data.index = index300_data.index.astype('datetime64[ns]')#索引变格式
index300_returns = index300_data.pct_change()[1:]
index300_returns = (index300_returns - np.mean(index300_returns))/np.std(index300_returns) # 标准化均值为0方差为1
index300_returns.tail()

#GARCH(1,1)模型
garch_11 = arch_model(index300_returns, vol='Garch', p=1, o=0, q=1, dist='Normal')
res = garch_11.fit()
res.summary()

C, A, B = res.params[1:] # 保存 GARCH 系数
def arch_p(C, A, B, returns, p):
    """基于GARCH(1,1)模型模拟的系数，返回  ARCH(p) 模型中的 sigma^2 """

    squared_returns = returns**2
    lagged_squared_returns = squared_returns.iloc[-p:] #
    lagged_squared_returns = lagged_squared_returns[::-1] # 顺序颠倒

    a = C/(1-B)
    a_i = [A*B**(i-1) for i in range(1,p+1)]

    ans = a + np.dot(a_i,lagged_squared_returns)
    return ans
  
 def garch_forecast(C, A, B, returns, dist='Normal'):
    """GARCH模型 L1 预测 
    参数:
    C -  GARCH 模型的常数项
    A -  GARCH 模型的 Y_n^2 系数
    B - GARCH 模型的 sigma_n^2 系数
    """
    
    n = len(returns)
    p = int(n/2)
    
    #GARCH 模型的 sigma_n^2 系数
    arch_p_term = arch_p(C, A, B, returns, p)
    
    #计算残差项平方的  median 
    if dist.lower()=='normal':
        Zn2 = 0.45
    elif dist.lower()=='t':
        Zn2 = 0.53
    else:
        print("无效分布输入, 只能选 'normal' 或 't' ")
        return None
    
    forecast = arch_p_term * Zn2
    return forecast
  garch_forecast(C,A,B,index300_returns[:'2018-06-08'])
  
