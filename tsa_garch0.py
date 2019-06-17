import datetime
import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib as mpl
#%matplotlib inline
mpl.rc('figure', figsize=(14, 7))
from arch import arch_model
import datetime as dt

#取出深300指数、创业板指、国债指数、企业债指数、恒生指数、标普500指数、原油指数、黄金指数数据，并进行合并
start = '20130501'
end = '20180531'
indices = ['000300', '399006', '000012','000013','HSI','SPX']
df = DataAPI.MktIdxdGet(ticker=indices, beginDate=start, endDate=end, field="tradeDate,ticker,closeIndex")
df = df.pivot(index="tradeDate", columns="ticker", values="closeIndex")
df.head()

#计算各指数收益率数据
df1=df.pct_change()
df_returns=df1.dropna()
df_returns.head()

#计算沪深300指数GARCH模型
returns = 100.0 *df_returns['000300']
am2 = arch_model(returns)
res2 = am2.fit()
res2.summary()

res2.conditional_volatility.plot()

#读取香港恒指波幅指数

vhsi=pd.read_excel('VHSI.xlsx','file') 
vhsi=vhsi.set_index('date')
start = '20130501'
end = '20180531'
vhsi=vhsi[vhsi.index<end ]
vhsi=vhsi[start<vhsi.index]

vhsi=vhsi

returns = (returns.rolling(window=7,center=False).std())
returns = returns + (pd.rolling_mean(returns, window=30, center=False)) * (12 ** 0.5)

vseries = vhsi
vseries = vseries / (12 ** 0.5)
fig = vseries.plot()

vhsi.index.name = 'tradeDate'
vhsi = vhsi.set_index(pd.DatetimeIndex(vhsi.index).strftime("%Y-%m-%d"))
### Calculate Standard Errors ###
vhsi['realized volatility'] = returns
vhsi['GARCH'] = res3.conditional_volatility

vhsi=vhsi.dropna()

vhsi.drop(vhsi.columns[:3], axis=1,inplace=True)
vhsi.head()
