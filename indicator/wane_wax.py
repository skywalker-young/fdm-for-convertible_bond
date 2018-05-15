    for i,j in wave_crest:

        wave_crest_x.append(i)

        wave_crest_y.append(j)
    wave_base_x = [] #波谷x
    wave_base_y = [] #波谷y
    for i,j in wave_base:

        wave_base_x.append(i)

        wave_base_y.append(j)
    #将原始数据和波峰，波谷画到一张图上
    plt.figure(figsize=(20,10))
    plt.plot(arr)
    plt.plot(wave_base_x, wave_base_y, 'go')#红色的点
    plt.plot(wave_crest_x, wave_crest_y, 'ro')#蓝色的点
    plt.grid()
    plt.show()
wave_guess(dea[0:200])
'''
dea=dea[0:200]
dayspan=50
wave_wax_x = []  # 波峰x  记录索引，为天数
wave_wax_y = []  # 波峰y
wave_wane_x=[]   #波谷x
wave_wane_y=[]   #波谷y   记录索引为DEA值
for i in range (0,200,dayspan):

    tmp=dea[i:i+dayspan]
    wave_wax =max(enumerate(tmp),key=lambda x :x[1])
    wave_wane=min(enumerate(tmp),key=lambda x :x[1])

    wave_wax_x.append(wave_wax[0]+i)

    wave_wax_y.append(wave_wax[1])
    wave_wane_y.append(wave_wane[1] )
    wave_wane_x.append(wave_wane[0]+i)

print('wane x;wane y:',wave_wane_x,wave_wane_y)

#print(zip(wave_wax_y,wave_wane_y))
#plt.grid(True)


'''
#plt.plot([wave_wax_x,wave_wane_x],[wave_wax_y,wave_wane_y])
plt.scatter(wave_wax_x,wave_wax_y,color='r')
plt.scatter(wave_wane_x,wave_wane_y,color='b')
plt.plot(dea,color='black')
'''


newWaneY=[]
newWaneX=[]
#两个高坡间隔下确认一个min
for i in range(0,len(wave_wax_y),2):
    tmp=wave_wane_y[i:i+2]
    tmp=min(enumerate(tmp),key=lambda x :x[1])
    newWaneY.append(tmp[1])
    #newWaneX.append(wave_wane_y.index(newWaneY))


print(newWaneY)
for i in range(  2 ):
      a=wave_wane_y.index(newWaneY[i])
      newWaneX.append(wave_wane_x.pop(a-i))  ###记录索引，为天数

#a=wave_wane_y.index(newWaneY[1])
#print(a)
#newWaneX=(wave_wane_x.remove(wave_wane_x[a+1]))
#wave_wane_x.remove()

print('newWaneX',newWaneX)
print('newWaneY',newWaneY)
print('wax_x',wave_wax_x,wave_wax_y)

connectx=wave_wax_x+newWaneX
connectx=sorted(connectx)

aaa=[]
for i in range(2):
   aaa.append(connectx.index(newWaneX[i]))

for i in range(2):
  connecty=wave_wax_y.insert(aaa[i],newWaneY[i])

ax=plt.subplot(2,1,1)

ax.plot(aclose,label='closePrice',color='b')
plt.grid(True)
plt.subplots_adjust(top=None,bottom=None)
ax2=plt.subplot(2,1,2)
################
for i in range(5):
    plt.plot([connectx[i] ,connectx[i+1]],[wave_wax_y[i],wave_wax_y[ i+1]])
######################
plt.plot(dea,label='DEA',color='crimson')
plt.xlabel('weekdays')
#plt.subplots_adjust(   wspace=None, hspace=0)
plt.grid(True)
 
plt.legend()
plt.show()

