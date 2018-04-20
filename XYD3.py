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
