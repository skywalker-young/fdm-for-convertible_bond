'''
根据test002中得到的BDkpi中基础列，扩充至完整的bdkpi表
'''
import pandas as pd
import numpy as np
import datetime
# rawdata2=pd.read_excel('ForBdkpi.xlsx',sheet_name='商户交易信息汇总')
# print(rawdata2.head())
#
# rawdata2=rawdata2.iloc[:,[0,4,15,24,25,26,27,28]]
#
# rawdata2.to_excel('ForShopfinishedValue.xlsx',index=None)
#后三列在excel中把空白项替换为0 !!
# exit()
rawdata2=pd.read_excel('ForShopfinishedValue.xlsx',nrows=22614)

countifs1=rawdata2[:12082]

Subcountif1=countifs1.loc[(countifs1['审核状态']=='审核通过')&(countifs1['5月交易笔数汇总']>29)&\
                         (countifs1['开户重复进件']==0)&(countifs1['问题商户']==0)]

result1=Subcountif1.groupby(['编号']).size().reset_index(name='count_May')
# print(result1)

countifs2=rawdata2[12083:22613]

Subcountif2=countifs2.loc[(countifs2['审核状态']=='审核通过')&(countifs2['滚动']>29)&\
                          (countifs2['4月交易笔数汇总']<=29)&(countifs2['开户重复进件']==0)&(countifs2['问题商户']==0)]

result2=Subcountif2.groupby(['编号']).size().reset_index(name='count_April')
# print(result2)
'''how = outer , 全部保留，na归为0，再求和'''
mergeresult=pd.merge(result1,result2,how='outer',on='编号')
mergeresult['count_April']=mergeresult['count_April'].fillna(0)
mergeresult['count_May']=mergeresult['count_May'].fillna(0)
mergeresult['Ssum']=mergeresult['count_April']+mergeresult['count_May']
mergeresult=mergeresult.rename(columns={'编号':'业务员编号'})

basic=pd.read_excel('basic.xlsx')
finished=pd.merge(basic,mergeresult,how='left',on=['业务员编号'])
finished['Ssum']=finished['Ssum'].fillna(0)  ###计算完成值


targer_increasing_shop=30
current_month_attendance=19
rawdata=pd.read_excel('testsummary.xlsx')

shop_target_value=[]
rawdata['新增有效商户完成值']=finished['Ssum']
# rawdata['新增有效商户指标值']
for i in range(len(rawdata)):
    attend=rawdata['实际出勤天数'][i]

    sick=rawdata['事假(天)'][i]
    tmp=targer_increasing_shop*1.0/current_month_attendance*(attend+sick)
    tmp=round(tmp)
    shop_target_value.append(tmp)

rawdata['新增有效商户指标值']=shop_target_value

rawdata['新增有效商户完成率']=rawdata['新增有效商户完成值']/rawdata['新增有效商户指标值']

FinishShopPct=[]
for i in range(len(rawdata)):
    tmp=min(50,rawdata['新增有效商户完成率'][i]*50)
    tmp=round(tmp,2)
    FinishShopPct .append(tmp)

rawdata['新增有效商户完成分值']=FinishShopPct

rawdata.to_excel('tmpBDkpi.xlsx',index=None)
