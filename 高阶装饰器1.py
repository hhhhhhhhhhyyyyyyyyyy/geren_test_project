def wrapper1(fn):
    def inner(*args,**kwargs):
        print('欢迎登录1')
        kk=fn(*args,**kwargs)
        print('祝你玩得愉快1')
        return kk
    return inner

def wrapper2(fn):
    def inner(*args,**kwargs):
        print('欢迎登录2')
        kk=fn(*args,**kwargs)
        print('祝你玩得愉快2')
        return kk
    return inner

def wrapper3(fn):
    def inner(*args,**kwargs):
        print('欢迎登录3')
        kk=fn(*args,**kwargs)
        print('祝你玩得愉快3')
        return kk
    return inner



@wrapper3
@wrapper2
@wrapper1
def game(): #先运行经过wrapper1装饰结果，在运行经过wrapper2装饰的结果，在运行经过wrapper3装饰的结果
    print("欢迎来到我的世界")

game()
#结果如下：
# 欢迎登录3
# 欢迎登录2
# 欢迎登录1
# 欢迎来到我的世界
# 祝你玩得愉快1
# 祝你玩得愉快2
# 祝你玩得愉快3