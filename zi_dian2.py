<<<<<<< HEAD
#统计字典中每个字符出现的次数,并把结果放在字典中
cishu={}
s="shdwhdjjdbjhwkdgjhbdsjagdebdjegfwhjefwejkfh"
for i in s:
    print(i)
for i in s:
    result=cishu.get(i,0)#如果字符没出现就让result=0
    result+=1
    cishu[i]=result
print(cishu)

## 做统计
# 车牌区域划分，现给出以下车牌。根据车牌的信息，分析出各省的车牌持有量。
cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
locations={'沪': '上海', '京': '北京', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南'}
resu={}
c=[]
for a in cars:
    i=locations[a[0]]#找到简称相对应的省份名
    c.append(i)#把省份名放进列表c
print(c)
for x in c:
      b=resu.get(x,0)#把省份名从列表c取出来
      b+=1
      resu[x]=b
print(resu) 
# 结果:
# {"上海":1, "北京":1, "黑龙江":3, "山东":2}
    

=======
#统计字典中每个字符出现的次数,并把结果放在字典中
cishu={}
s="shdwhdjjdbjhwkdgjhbdsjagdebdjegfwhjefwejkfh"
for i in s:
    print(i)
for i in s:
    result=cishu.get(i,0)#如果字符没出现就让result=0
    result+=1
    cishu[i]=result
print(cishu)

## 做统计
# 车牌区域划分，现给出以下车牌。根据车牌的信息，分析出各省的车牌持有量。
cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
locations={'沪': '上海', '京': '北京', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南'}
resu={}
c=[]
for a in cars:
    i=locations[a[0]]#找到简称相对应的省份名
    c.append(i)#把省份名放进列表c
print(c)
for x in c:
      b=resu.get(x,0)#把省份名从列表c取出来
      b+=1
      resu[x]=b
print(resu) 
# 结果:
# {"上海":1, "北京":1, "黑龙江":3, "山东":2}
    

>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
