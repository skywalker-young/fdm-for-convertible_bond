window=15
move=1
macd=[]
for i in range(len(daily_returnXYD)-window+1):
 tmp=sum(daily_returnXYD[i:i+window])/window
 macd.append(tmp)

macdForSc=[]
for i in range(len(daily_returnSC)-window+1):
 tmp=sum(daily_returnSC[i:i+window])/window
 macdForSc.append(tmp)

plt.plot(macd,macdForSc)
plt.show()
############################

这部分是研究波动率关系
########################
for i in range(move):
   tmp= (daily_returnXYD[i*window:(i+1)*window])
   tmp=sp.sqrt(sp.var(tmp))
   macdForXYD.append(tmp)
for i in range(move):
     tmp = (daily_returnSC[i*window:(i + 1)*window])
     tmp = sp.sqrt(sp.var(tmp))
     macdForSC.append(tmp)

plt.scatter(macdForXYD,macdForSC)
f=interp1d(macdForXYD,macdForSC)
xnew=np.linspace(min(macdForXYD),max(macdForXYD),num=500)
plt.plot(macdForXYD,macdForSC,'o',xnew,f(xnew),'-')
plt.xlabel("15days volatility of XYD")
plt.ylabel("15days volatility of SC")
plt.show()
