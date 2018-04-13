from scipy.interpolate import interp1d
daily_returnXYD=(np.array(daily_returnXYD))
daily_returnSC=(np.array(daily_returnSC))
f=interp1d(daily_returnXYD,daily_returnSC)
xnew=np.linspace(min(daily_returnXYD),max(daily_returnXYD),num=100)
plt.plot(daily_returnXYD,daily_returnSC,'o',xnew,f(xnew),'-')
plt.show()
'''
插值是指已知某函数在若干离散点上的函数值或导数信息，
插值曲线要过数据点，拟合曲线整体效果更好
在scipy中使用cubic插值总是有问题，经查发现是有很多相同数据（日回报率相同导致，不适用预测）
改天自己写个插值函数，这样才算真正明白
'''
