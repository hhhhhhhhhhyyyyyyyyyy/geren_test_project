class people():
    price=2000
    def __init__(self):
        self.name="肉丝"
        self.__age=29#私有变量
        print(self.__age)
        self.__siyou1()

      
    def __siyou1(self):#私有方法
        print('*'*20)

    def qusiyou(self):
        return self.__age

rose=people()
#rose.__siyou1()#会报错
print(people.price)#2000
print(rose.name)#肉丝
#print(rose.__age)#会报错，不能访问
'''
私有变量和私有方法只能在类里使用
'''      
#如果要去私有化，使其能在类外进行访问
#方法1：
print(rose._people__age)#带上类名
#方法2：
h=rose.qusiyou()#一般用return返回进行访问
print(h)