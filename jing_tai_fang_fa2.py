class people():
    __age=30

    def __init__(self,name):
        self.name=name
        print(self.name)

    @classmethod
    def show_age(cls):#带参数是类方法
        print(cls.__age)
    
    @staticmethod
    def show_age2():#不带参数是静态方法
        print(people.__age)#静态方法实现私有变量在类外打印

x=input("请输入人名：")
v=people(x)
v.show_age()
v.show_age2()
people.show_age()
people.show_age2()
'''
类似类方法
1、需要用到装饰器@staticmethod
2、静态方法无需传递参数
3、只能访问类的属性和方法，对象属性方法无法访问
4、类创建静态方法就实现了
'''

'''
类方法与静态方法相同点：
1、都需要装饰器
2、都可通过类名调用访问但不能访问对象
3、可在创建对象前使用，因为不依赖于对象

不同：
1、装饰器不同
2、类方法有参数，静态方法无参数

普通方法与  类方法和静态方法不同
1、普通方法要依赖于对象，需要参数self
2、没有装饰器
3、创建对象后才能调用普通方法，否则无法调用

'''