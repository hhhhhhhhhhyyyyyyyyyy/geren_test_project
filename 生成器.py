'''
1、函数中如果包含了yield，通过yield来返回数据的话，这个函数就是生成器函数
def func():
    yield 1111
特点 函数名()  此时不是在运行函数，而是在创建生成器
2、极其省内存，生成器和迭代器一样，仅记录步骤和代码
对于很长的数列，取一个值执行一次代码，不会都执行出来
可以使用for循环提取需要的东西
'''

def func():
    print("我爱你")
    yield  234
    print('谁爱我？')
    yield 345

mm=func()#创建一个生成器
r=mm.__next__()#生成器开始执行，结果是：我爱你，直到遇到最近的一个yield为止，生成器的本质是迭代器
print(r)#结果是：我爱你 234
r2=mm.__next__()#结果是：我爱你  234  谁爱我？
print(r2)#结果是：我爱你  234  谁爱我？  345



def func1():
    for i in range(999):
        yield i

xx=func1()
print(xx.__next__())#0 不会将0-998都打印出来，而是写一个next打印一个数字
print(xx.__next__())#1
print(xx.__next__())#2
print(xx.__next__())#3

for i in range(50):
    print(xx.__next__())#4-53  因为0-3上面已经取了

for item in xx:
    if item<=100:
        print(item)#54-100 因为0-53上面已经取了

'''生成器表达式和推导式我放在一起了'''
