'''把函数作为参数传入，这样的函数称为高阶函数'''
#abs函数：用来完成对数字求绝对值计算
print(abs(-19))
#round函数:完成对数字四舍五入的运算
print(round(2.5))
'''这两个函数是学习高阶函数的前置条件'''
#先将两个数字进行绝对值操作之后完成求和计算
#方法1
def sumd(a,b):
    return abs(a)+abs(b)
result=sumd(-1,-4)
print(result)

f1=lambda a,b:abs(a)+abs(b)
print(f1(-2,-5))

#方法2
def sum2(a,b,f):
#高阶函数，将abs的操作融入sum2函数中，当然，f可以代入其他函数
    return f(a)+f(b)
result2=sum2(-2,-  4,abs)
print(result2)