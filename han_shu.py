 
"""
1、函数的概念：对某段代码进行封装，在需要这段代码的时候直接调用即可
2、函数的定义：只是声明，没有调用就没有具体执行
def 函数名():
     函数体（想要封装的代码）
3、函数的调用
函数名()                
"""
#固定长度的参数
def sums(num1,num2=5):

    print("num1",num1)
    print("num2",num2)
    sums11=num1+num2
    print(sums11)
sums(1,2)#默认num1=1，num2=2
sums(num1=5)#没有传num2等于几时，默认使用函数定义的形参num2=5
sums(num1=3,num2=7)
#只要进行调用，主程序传过去的参数值优先级大于函数形参的固定值，因此优先使用num2=7

#可变长度的参数
def kebian(*a):#*a表示在数据接收时会自动转换成元组数据类型
    print(a)
kebian("我爱我家")#('我爱我家',)元组在只有一个元素时结尾必须有逗号
kebian("我爱我家",'wo')#答案自动变成元组类型

def kebian3(e,f,g):
    print(e,f,g)
t=(1,2,3)#元组数据
kebian(*t)#进行解包，将元组数据变成普通的三个变量传递到函数当中，*t相当于e，f，g=1，2，3
"""如果要解包的话，函数变量和输入变量的值要一一对应，不可缺少或过多"""


def kebian2(**b):#**b表示在数据接收时会自动转换成字典数据类型
    print(b)
#不可以写kebian2(1,2,3)，因为函数会辨别不了你这个是字典当中的key还是value
kebian2(b=1,c=2,d=3)#答案自动变成字典类型

'''当两个函数想要互相使用到内部变量时，可以应用到函数的返回值
   1、使用renturn关键字返回内容
   2、将内容返回到函数调用处
   3、函数体中没有return语句时，函数运行结束，默认返回值None，也被称为隐含返回值
   4、在函数看到第一个return时就关闭了，所以不可以在一个函数里使用多个return'''


def kebian4():
    h=1
    i=2
    return h+i,h*i
result=kebian4()#result变量是元组类型
#或者可以取两个变量m,n同时接收返回的两个数字
#a,b=kebian4()，这叫元组的拆包
#dict={"name":"hyy","age":18}
#a,b=dict()字典的拆包


def kebian5(j,k):
    print(j+k)
kebian5(*result)

'''定义全局变量的两种方法
1、在主程序里直接定义
2、在函数里使用global'''

count=4
def kebian6():
    global count
    count+=1
    print(count)#5
kebian6()
print(count)#5 
'''由于之前使用global定义了count为全局变量
所以不管在函数里还是主程序只要count值有更新都会把之前的值覆盖
而显示出最新的值'''
'''比较一下两个程序的结果'''
count=4
def kebian7():
    count=4#即便是在主程序定义了全局变量count，但是在子函数里的count会默认不是全局变量而需要重新定义
    count+=1
    print(count)#5
kebian7()
print(count)#4
'''由于只在主程序里定义了count为全局变量
所以在函数里只要count值有更新都会把之前的值覆盖而显示出最新的值'''


'''内置函数'''
#1、zip函数
#用于将可迭代的对象作为参数将对象中对应的元素打包成一个个元组
#然后返回这些元组组成的列表
ll=[23,45,66]
li=[23,12,21]
b=zip(ll,li)
print(b)#返回的是zip object迭代器本身
print(list(b))#要把它转换为元组或者列表类型

#2、map函数
#将一个列表中的每个元素都转换成某种数据类型
ld=[1,2,3,4]
c=map(float,ld)
print(c)#返回的是map object迭代器本身
print(list(c))#要把它转换为列表类型，这个函数本身返回的是新列表

#3、filter函数
#用于过滤序列中不符合条件的元素，返回由符合条件元素组成的新列表
#filter（function or None,iterable）>>>返回的也是filter object
#iterable是自动生成的一组序列，例如range（）函数生成序列，然后投入子函数function过滤掉不符合条件的
#生成新的符合条件的新列表
def ou_shu(i):
    if i%2==0:
        return i
v=filter(ou_shu,range(1,11))
print(list(v))#返回1-10的偶数序列列表



'''迭代器'''
#统一一些数据的循环方式，不同数据类型有不同的循环方式
#但是通过给定__iter__（获取迭代器）可以统一循环标准(元组，列表，字典，字符串，set集合斗士可迭代对象)
#bool，int，float类型不能获取迭代器 
#迭代器也是for循环原理  
s="sdwdgwhdq"
print(s.__iter__())#获取字符串迭代器
t=[12,32,22]
print(t.__iter__())#获取列表迭代器
it=iter(t)#或者写it=t.__iter__()
it2=iter(s)#或者写it2=s.__iter__()
print(it.__next__())#获取t列表下第0个数据
print(it.__next__())#获取t列表下第1个数据
print(it.__next__())#获取t列表下第2个数据
print(it.__next__())#获取t列表下第3个数据，但是取不到会报错
#迭代器特点一：只能向前取值，不能往后取值
#迭代器特点二：一次性的，走完了还走就报错
print(it2.__next__())#获取s字符串下第0个数据
print(it2.__next__())#获取s字符串下第1个数据
print(it2.__next__())#获取s字符串下第2个数据