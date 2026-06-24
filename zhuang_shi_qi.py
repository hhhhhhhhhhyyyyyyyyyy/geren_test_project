#装饰器：在不改变原有函数的基础上给函数增添新功能
'''
装饰器通用模型：
def wrapper(fn):#fn为要增加功能的函数
    def inner(*args,**kwargs): #可以接受所有参数
        ret=fn(*args,**kwargs)  #运行你装饰的函数
        return ret  #返回结果
    return inner
        
'''

def wrapper(fn):#fn为要增加功能的函数
    def inner(*args,**kwargs): #可以接受所有参数 inner实际上就是一个代替fn的函数，所以fn什么参数会原封不动传给inner
        #植入你想在执行fn前想做的事情
        print("登陆")
        #植入你想在执行fn前想做的事情
        ret=fn(*args,**kwargs)#运行你装饰的函数fn
        return ret  #返回结果,如果fn有返回值就用这个返回结果，得到原函数fn结果
    return inner #替代原函数
#第一种
def add_i():
    print("我要写文章")

add_i=wrapper(add_i)#前一个add_i是经过wrapper返回的inner，后一个add_i是第19行的函数
add_i()
#第二种
@wrapper  #等于22行代码
def add_i():
    print("我要写文章")

add_i()