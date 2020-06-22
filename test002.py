import pandas as pd
import datetime
pd.set_option('display.float_format',lambda x : '%.2f' % x)
# rawdata=pd.read_excel('ForBdkpi.xlsx',sheet_name='Sheet1')
# # print(len(rawdata))
#
# # print(rawdata.iloc[1])
#
# rawdata.iloc[:,27:31]=rawdata.iloc[:,27:31].fillna(0)
# print(rawdata.head())

# basci=pd.read_excel('basic.xlsx')
# '''处理人员信息'''
# rawdata1=pd.read_excel('ForBdkpi.xlsx',sheet_name='人员信息')
# rawdata1=rawdata1.drop(index=[0])
# rawdata1=rawdata1.iloc[:,[1,2,3,4,6,7,12,13,20]]
# rawdata1['是否本月离职']=rawdata1['是否本月离职'].fillna(0)
#
# tmp1=pd.merge(basci,rawdata1,how='left',on=['业务员编号','姓名'])
#
# tmp1.to_excel('tmp1.xlsx',index=None)
# print('finish')

'''处理考勤记录'''
rawdata2=pd.read_excel('ForBdkpi.xlsx',sheet_name='考勤记录')
rawdata2=rawdata2.drop(index=[0])
rawdata2 = rawdata2.iloc[:, [0,2,4,5,6,16,17]]
rawdata2[['事假(天)','病假(天)']]=rawdata2[['事假(天)','病假(天)']].fillna(0)#( 为英文输入法下的字符
# # print(rawdata2.tail())
# rawdata2.to_excel('tmp考勤记录.xlsx',index=None)
# print('finish')

'''处理人员信息变更'''
rawdata3=pd.read_excel('ForBdkpi.xlsx',sheet_name='team-change')

rawdata3=rawdata3.iloc[:,[4,7,8,9]]
rawdata3=rawdata3.rename(columns={'业务员姓名':'姓名'})
# # print(rawdata3.head())
#
tmp1=pd.read_excel('tmp1.xlsx')

#
tmp2=pd.merge(tmp1,rawdata3,how='left',on=['业务员编号','姓名'])

testsummary=pd.merge(tmp2,rawdata2,how='left',on=['业务员编号','姓名','入职时间','离职时间'])
testsummary.to_excel('TestSummary.xlsx',index=None)
# '''人员信息和人员变更信息合并后，再添加考勤记录'''

# #BDkpi表以考勤记录为标准制作

# summary2.to_excel('TestSummary.xlsx',index=None)
##bdkpi的前几列 ！！！