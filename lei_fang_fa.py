class mimi():
    name='球球'
    def __init__(self,name):
        self.price=900
        print(f"我的猫猫叫{name}")
    def maomao2(self):
        self.age=18
        print(f'我的猫猫买来花了{self.price},它今年已经{self.age}了')
    def maomao3(self):
        self.maomao2()#同级调用需要加上self

    @classmethod#类方法
    def maomao(cls):#参数为class
        print(f'我的猫猫另一个名字叫{cls.name}')

d=mimi('汤圆')
d.maomao3()
d.maomao()

'''
类方法特点：
1、定义需要依赖装饰器@classmethod
2、类方法中参数不是一个对象，而是类
3、类方法只能使用类属性
4、类方法不能调用普通方法，比如maomao(class)不能调用maomao2()

类方法作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些功能，这些功能可以放进类方法
'''

        
