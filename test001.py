import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# pd.set_option('display.max_columns', None)

'''
直营绩效20年6月，主管
'''
rawdata=pd.read_excel('payroll_test.xlsx',sheet_name='Sheet1')
#
#按照全勤，不换团队，最简单的情况进行计算
#
fields=['业务员编号',	'姓名',	'在职状态',	'城市',	'现团队',\
   '职位',	'入职时间',	'离职时间',	'出勤天数',	'事假天数',	'病假天数',	'原团队',\
   '变更时间',	'底薪',	'职级薪',	'当月4月有效户',	'当月5月有效户',	'次月B类',	'次月C类',	'次月D类',\
   '次月E类',	'次月F类',	'第三月D类',	'第三月E类',	'第三月F类',\
   '有效商户提奖合计',	'有效净增笔数',	'每笔提奖金额',	'有效净增笔数提奖合计',	'E类商户合计',	'E类每户提奖',\
   'F类商户合计',	'F类每户提奖',	'存量提奖合计',	'GPRS云喇叭/支付宝云喇叭（租）',\
   'WiFi云喇叭/码枪Q500（租）',	'招财宝（租）',	'T1（租）',	'GPRS云喇叭/支付宝云喇叭',	'WiFi云喇叭/码枪Q500',\
   '招财宝',	'T1',	'4gQM500',	'智掌柜',	'机具提奖合计',	'个人绩效合计',	'团队绩效合计',	'KPI值',\
   '应付绩效合计'	,'应扣款合计'	,'机具领用扣款'	,'其他补款'	,'应付薪资合计'	,'银行卡号'	,'手机号'	,'身份证号'	,\
   '开户行',	'省份'	,'地市','unknown']

rawdata=rawdata.iloc[2:]
rawdata=rawdata.reset_index(drop=True)
rawdata.columns=fields
rawdata.to_excel('tmp.xlsx',index=None)
print(rawdata.head())

necessaryField=['业务员编号','姓名','底薪','职级薪','当月4月有效户',	'当月5月有效户',	'次月B类',	'次月C类',	'次月D类',\
   '次月E类',	'次月F类',	'第三月D类',	'第三月E类',	'第三月F类',\
   '有效商户提奖合计',	'有效净增笔数',	'每笔提奖金额',	'有效净增笔数提奖合计',	'E类商户合计',	'E类每户提奖',\
   'F类商户合计',	'F类每户提奖',	'存量提奖合计',	'GPRS云喇叭/支付宝云喇叭（租）',\
   'WiFi云喇叭/码枪Q500（租）',	'招财宝（租）',	'T1（租）',	'GPRS云喇叭/支付宝云喇叭',	'WiFi云喇叭/码枪Q500',\
   '招财宝',	'T1',	'4gQM500',	'智掌柜','KPI值']
# print(rawdata.iloc[1])
testdata=rawdata[necessaryField]

print(testdata.head())
'''
testdata=rawdata[necessaryField]
testdata=testdata[:32]
testdata.iloc[:,11:14]=testdata.iloc[:,11:14].fillna(0)
# print(testdata[['第三月D类',	'第三月E类',	'第三月F类','有效商户提奖合计',	'有效净增笔数']])
# exit()
conmoney=rawdata['底薪'][0]+rawdata['职级薪'][0]
s1=(testdata['当月4月有效户'][0]+testdata['当月5月有效户'][0])*50
s2=(testdata['次月B类'][0]*20+testdata['次月C类'][0]*40+testdata['次月D类'][0]*80+testdata['次月E类'][0]*120+\
    testdata['次月F类'][0]*160+testdata['第三月D类'][0]*20+testdata['第三月E类'][0]*50+testdata['第三月F类'][0]*80)
'''