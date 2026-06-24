
j=True
def wrapper(fn):
    def inner(*args,**kwargs):
      while j:#while碰到break或者return自动退出循环
        print("请先登陆")
        x=input('请输入用户名：\n')
        y=input('请输入密码：\n')
        if x=='admin' and y=='040069':
            print('登陆成功')
            kk=fn(*args,**kwargs)
            return kk
        else:
            print("登陆失败，请重新登陆")
    return inner

@wrapper
def play():
    print('欢迎来到游戏世界！')
    return "我要玩辅助"

zz=play()
print(zz)