<<<<<<< HEAD
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
result=kebian4()


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
def kebian6():
    count+=1
    print(count)#5
kebian6()
print(count)#4
'''由于只在主程序里定义了count为全局变量
所以在函数里只要count值有更新都会把之前的值覆盖而显示出最新的值
=======
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
result=kebian4()


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
def kebian6():
    count+=1
    print(count)#5
kebian6()
print(count)#4
'''由于只在主程序里定义了count为全局变量
所以在函数里只要count值有更新都会把之前的值覆盖而显示出最新的值
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
但主程序里count值不变'''