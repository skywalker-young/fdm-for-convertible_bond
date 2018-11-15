    def saveSyncData(self, strategy):
        """保存同步数据（无效）"""
        # 建立数据库连接
        client = pymongo.MongoClient('localhost', 27017)
        collection = client['VnTrader_Position_Details'][strategy.name]
        # print(collection)
        # print('插入数据：%s' % strategy.name)
        var = strategy.varList
        d = {}
        for i in var:
           d[i] = strategy.__getattribute__(i)

        collection.insert_one(d)
        
        
        连接数据库部分代码
