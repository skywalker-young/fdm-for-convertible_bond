# coding: utf-8
import numpy as np
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient, ASCENDING
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import mpl_finance as mpf
def dbConnect():

    # dbClient = MongoClient("localhost", 27017)
    try:
        dbClient = MongoClient("localhost", 27017)
        dbName = 'VnTrader_1Min_Db'
        collectionName = u'IF0000'
        #StartDate = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) -timedelta(10)
        StartDate=datetime(2017, 4, 1)
        EndDate=datetime(2017,5,30)
        d = {'datetime': {'$gte': StartDate,"$lt":EndDate}}
        # collection = dbClient.get_database('dbName').get_collection('collectionName')
        collection = dbClient[dbName][collectionName]
        #print collection, d
        cursor = collection.find(d).sort('datetime', ASCENDING)
        return list(cursor)
    except Exception:
        print u"终止！"

if __name__ == '__main__':
    db = dbConnect()
    close=[]
    high=[]
    low=[]
    open=[]

    for i in db:
         #print i
         close.append(i['close'])
         high.append(i['high'])
         low.append(i['low'])
         open.append(i['open'])


    close=close[:2000]
    #plt.plot(close)
    #plt.show()
    newHigh=[]
    newLow=[]
    newClose=[]
    newOpen=[]
    for  i in range( 2000-1):
        if (close[i]<close[i+1]):
            newHigh.append(max(high[i],high[i+1]))
            newLow.append(max(low[i],low[i+1]))
            newClose.append(max(close[i],close[i+1]))
            newOpen.append(max(open[i],open[i+1]))
        else:
            newHigh.append(min(high[i],high[i+1]))
            newLow.append(min(low[i],low[i+1]))
            newClose.append(min(close[i],close[i+1]))
            newOpen.append(min(open[i],open[i+1]))

    step=3
    count=1
    topHigh=[]
    topLow=[]
    topClose=[]
    topOpen=[]
    bottomOpen=[]
    bottomHigh=[]
    bottomLow=[]
    bottomClose=[]
    index=[]
    obH=[]
    obL=[]

    for i in range(1,1999-1):
        a=newHigh[i] == max(newHigh[i - 1], newHigh[i], newHigh[i + 1])
        b=newLow[i]==max(newLow[i-1],newLow[i],newLow[i+1])
        if (a and b):

            index.append(i)
            obH.append(i)

        c= newHigh[i]==min(newHigh[i - 1], newHigh[i], newHigh[i + 1])
        d= newLow[i] ==min(newLow[i-1],newLow[i],newLow[i+1])

        if (c and d):

            index.append(i)
            obL.append(i)

    #print(len(index))#1201

    test=[0]*1201
    for i in range (len(index)):
        test[i]=newClose[index[i]]

    for i in obH :

        topHigh.append([newHigh[i],i])
        topLow.append([newLow[i],i])
        topClose.append([newClose[i],i])
        topOpen.append([newOpen[i],i])

    for i in obL:
        bottomHigh.append([newHigh[i],i])
        bottomLow.append([newLow[i],i])
        bottomClose.append([newClose[i],i])
        bottomOpen.append([newOpen[i],i])



    topHigh.extend(bottomHigh)
    topLow.extend(bottomLow)
    topClose.extend(bottomClose)
    topOpen.extend(bottomOpen)

    HH=sorted(topHigh ,key=lambda x:x[1])
    LL=sorted(topLow,key=lambda x:x[1])
    CC=sorted(topClose,key=lambda x:x[1])
    OO=sorted(topOpen,key=lambda x:x[1])

    '''
    plt.subplot(2,1,1)
    plt.plot(close)
    plt.subplot(2,1,2)
    plt.plot(index,test)
    plt.show()
    '''

    #
    HH=[i[0]for i in HH]
    LL=[i[0]for i in LL]
    CC=[i[0]for i in CC]
    OO=[i[0]for i in OO]
    print(np.asarray(HH[400:500]))
    print(np.asarray(LL[400:500]))
    print(np.asarray(CC[400:500]))
    print(np.asarray(OO[400:500]))
    fig, ax = plt.subplots(figsize=(10, 10))
    mpf.candlestick2_ochl(ax,opens=OO,closes=CC,highs=HH,lows=LL ,width=1, colorup='g', colordown='r', )
    plt.show()
    #print(topHigh)

    #print([i[0] for i in a])






