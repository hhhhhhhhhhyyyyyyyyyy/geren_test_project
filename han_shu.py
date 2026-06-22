 
"""
1、函数的概念：对某段代码进行封装，在需要这段代码的时候直接调用即可
2、函数的定义：只是声明，没有调用就没有具体执行
def 函数名():
     函数体（想要封装的代码）
3、函数的调用
函数名()                
"""
# #固定长度的参数
# def sums(num1,num2=5):

#     print("num1",num1)
#     print("num2",num2)
#     sums11=num1+num2
#     print(sums11)
# sums(1,2)#默认num1=1，num2=2
# sums(num1=5)#没有传num2等于几时，默认使用函数定义的形参num2=5
# sums(num1=3,num2=7)
# #只要进行调用，主程序传过去的参数值优先级大于函数形参的固定值，因此优先使用num2=7

# #可变长度的参数
# def kebian(*a):#*a表示在数据接收时会自动转换成元组数据类型
#     print(a)
# kebian("我爱我家")#('我爱我家',)元组在只有一个元素时结尾必须有逗号
# kebian("我爱我家",'wo')#答案自动变成元组类型

# def kebian3(e,f,g):
#     print(e,f,g)
# t=(1,2,3)#元组数据
# kebian(*t)#进行解包，将元组数据变成普通的三个变量传递到函数当中，*t相当于e，f，g=1，2，3
# """如果要解包的话，函数变量和输入变量的值要一一对应，不可缺少或过多"""


# def kebian2(**b):#**b表示在数据接收时会自动转换成字典数据类型
#     print(b)
# #不可以写kebian2(1,2,3)，因为函数会辨别不了你这个是字典当中的key还是value
# kebian2(b=1,c=2,d=3)#答案自动变成字典类型

# '''当两个函数想要互相使用到内部变量时，可以应用到函数的返回值
#    1、使用renturn关键字返回内容
#    2、将内容返回到函数调用处
#    3、函数体中没有return语句时，函数运行结束，默认返回值None，也被称为隐含返回值
#    4、在函数看到第一个return时就关闭了，所以不可以在一个函数里使用多个return'''


# def kebian4():
#     h=1
#     i=2
#     return h+i,h*i
# result=kebian4()#result变量是元组类型
# #或者可以取两个变量m,n同时接收返回的两个数字
# #a,b=kebian4()，这叫元组的拆包
# #dict={"name":"hyy","age":18}
# #a,b=dict()字典的拆包


# def kebian5(j,k):
#     print(j+k)
# kebian5(*result)

# '''定义全局变量的两种方法
# 1、在主程序里直接定义
# 2、在函数里使用global'''

# count=4
# def kebian6():
#     global count
#     count+=1
#     print(count)#5
# kebian6()
# print(count)#5 
# '''由于之前使用global定义了count为全局变量
# 所以不管在函数里还是主程序只要count值有更新都会把之前的值覆盖
# 而显示出最新的值'''
# '''比较一下两个程序的结果'''
# count=4
# def kebian7():
#     count=4#即便是在主程序定义了全局变量count，但是在子函数里的count会默认不是全局变量而需要重新定义
#     count+=1
#     print(count)#5
# kebian7()
# print(count)#4
# '''由于只在主程序里定义了count为全局变量
# 所以在函数里只要count值有更新都会把之前的值覆盖而显示出最新的值'''


# '''内置函数'''
# #1、zip函数
# #用于将可迭代的对象作为参数将对象中对应的元素打包成一个个元组
# #然后返回这些元组组成的列表
# ll=[23,45,66]
# li=[23,12,21]
# b=zip(ll,li)
# print(b)#返回的是zip object迭代器本身
# print(list(b))#要把它转换为元组或者列表类型

# #2、map函数
# #map(func,list)将传入的函数变量func作用到list每个变量当中，并将结果组成新的迭代器返回
# #将ld当中的整数变成浮点型数据
# ld=[1,2,3,4]
# c=map(float,ld)
# print(c)#返回的是map object迭代器本身
# print(list(c))#要把它转换为列表类型，这个函数本身返回的是新列表
# #将lf当中的数据变成数据的平方返回 
# lf=[1,2,3,4,5]
# def funct1(x):
#     return x**2
# d=map(funct1,lf)
# print(d)
# print(list(d))

# #3、filter函数
# #用于过滤序列中不符合条件的元素，返回由符合条件元素组成的新列表
# #filter（function or None,iterable）>>>返回的也是filter object
# #iterable是自动生成的一组序列，例如range（）函数生成序列，然后投入子函数function过滤掉不符合条件的
# #生成新的符合条件的新列表
# def ou_shu(i):
#     if i%2==0:
#         return i
# v=filter(ou_shu,range(1,11))
# print(list(v))#返回1-10的偶数序列列表

# #4、reduce函数
# #reduce(func，lst)，其中func必须有两个参数，每次func计算的结果继续和序列的下一个元素做累计计算
# #计算列表序列中各个数字的累加和
# import functools
# lis1=[1,2,3,4]
# def sum1(a,b):
#     return a+b
# x=functools.reduce(sum1,lis1)
# #reduce在functools模块中，想要使用reduce必须调用functools模块

# #5、sorted函数  
# # sorted(可迭代对象，key=func ，reverse)  key可以省略
# #执行过程把list当中所有可迭代对象一个一个传递给key作为参数，根据key的结果进行排序
# #reverse默认进行升序排序，如果reverse=True就是进行降序排序 
# lis5=['shuhwdlhw','何妍妍','账务会计','无限流怪谈']
# #根据字数多少排序
# result1=sorted(lis5,key=lambda x:len(x))#升序排序
# result2=sorted(lis5,key=lambda x:len(x),reverse=True)#降序排序
# print(result1)
# print(result2)

# #callable(xxx)判断xxx是否可以被调用
# def func():
#     print('1')
# print(callable(func))#True
# func()
# def fun1(fn):
#     if callable(fn):#判断是否可以被调用
#         fn()
#     else:
#         print("您输入的内容不可被调用")
# fun1(func)



# # #import copy
# # #import os
# # mm=input('>>>')
# # __import__(mm)#动态加载字符串模块名


# #eval函数
# #将输入字符串当作代码执行
# s='2+4*3'
# r=eval(s)#有返回值
# print(r)#14

# #exec函数
# #将输入字符串当作代码执行
# s='b=2+4*3'
# exec(s)#无返回值
# print(b)#14


# #compile函数
# #加载一串字符串代码，后面方便通过exec和eval去执行
# #compile


# #bin函数
# a=7
# print(bin(a))#0b111  十进制化为二进制
# b=0b101
# print(b)#5  二进制化为十进制

# #oct函数
# c=9
# print(oct(c))#转化成八进制 0o11

# #hex函数
# d=18
# print(hex(d))#转化成16进制 0x12

# #power函数
# print(pow(2,6))#2的6次方 等同于print(2**6)

# #sum函数
# print(sum([11,4,3]))#参数必须是可迭代对象 18
# print(max([11,4,3]))#参数必须是可迭代对象 11
# print(min([11,4,3]))#参数必须是可迭代对象 3
# print(min(11,4,3))


# #字典
# h=dict()#空字典
# d=dict([("zha","ben"),("死鬼","dd")])#{'zha':'ben','死鬼':'dd'}
# print(d)
# c={}
# print(c)

# #frozenset函数,不可增删改
# g=frozenset((11,22,6,11,22))#frozenset({11,22,6})具有去重效果
# print(g)

# #enumerate函数
# lis9=['hyy',25,'why']
# for i,item in enumerate(lis9,10):#10，'hyy'，11，25,12,'why'
#     print(i)#从10开始算起
#     print(item)


# #all,any函数
# lis8=[0,'nih',True]
# print(any(lis8)) #相当于or 结果是True
# print(all(lis8))#相当于是and 结果是 Flase

# # reversed函数
# lis9=['hyy',25,'why']
# r=reversed(lis9)
# print(list(r))
# #和filter，map，zip一样都是返回迭代器如果只写print(r)只会显示列表迭代器不会显示列表内容


#切片slice
s='今天我的心情很好'
s1=s[0:6:2]
print(s1)
s2=slice(0,6,2)
s3=s[s2]
print(s3)

print(ord('中'))#中字在字符中是几号 20013
print(chr(20013))#20013在字符串中对应什么字符 中  

'''迭代器'''
# #统一一些数据的循环方式，不同数据类型有不同的循环方式
# #但是通过给定__iter__（获取迭代器）可以统一循环标准(元组，列表，字典，字符串，set集合斗士可迭代对象)
# #bool，int，float类型不能获取迭代器 
# #迭代器也是for循环原理  
# s="sdwdgwhdq"
# print(s.__iter__())#获取字符串迭代器
# t=[12,32,22]
# print(t.__iter__())#获取列表迭代器
# it=iter(t)#或者写it=t.__iter__()
# it2=iter(s)#或者写it2=s.__iter__()
# print(it.__next__())#获取t列表下第0个数据
# print(it.__next__())#获取t列表下第1个数据
# print(it.__next__())#获取t列表下第2个数据
# print(it.__next__())#获取t列表下第3个数据，但是取不到会报错
# #迭代器特点一：只能向前取值，不能往后取值
# #迭代器特点二：一次性的，走完了还走就报错
# print(it2.__next__())#获取s字符串下第0个数据 相当于print(next(it2))
# print(it2.__next__())#获取s字符串下第1个数据
# print(it2.__next__())#获取s字符串下第2个数据