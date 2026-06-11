'''函数计算'''

def shu_ru():
    a=int(input("请输入第一个数:"))
    b=int(input("请输入第二个数:"))
    c=int(input("请输入第三个数:"))
    t=(a,b,c)
    print(t)
    return t


"""求和函数"""

def sum1(a,b,c):
    d=a+b+c
    return d   # return后面可以跟表达式


h=shu_ru()
e=sum1(*h)
print(f"这三个数的和为{e}")

'''求平均数'''
def ave1():
    x=shu_ru()
    g=sum1(*x)
    i=g/3
    return i
print(f"这三个数的平均数为{ave1()}")

