#面向对象：将数据和函数绑定在一起，进行封装，减少代码重复
#面向过程：根据业务逻辑从上到下写代码
#类：抽象概念，仅仅是模板，用来描述具有相同属性和方法的对象的集合
#对象：具体事物的存在，在现实世界当中是可以看得见摸得着的
'''将对象归类，让具有某些特征的具体事物划分到一个集合当中'''
'''
类的三部分：
1、类的名称：类名
2、类的属性：一组数据
3、类的方法：允许对类进行的操作
4、python使用class关键字来定义类
5、基本结构：
class 类名:
      pass
'''
'''创建对象：可根据已经定义的类去创建出一个个对象
格式:对象名-类名'''
# #创建类：学生类，创建对象：张三，在类中定义方法输出：张三学习python
# #方法1
# class StudentsClass:#类
#     def study_python(self,name):#类中函数，称为方法
#         print(f"张三爱学习{name}!")
# zs=StudentsClass()#创建对象，整个过程成为实例化
# zs.study_python("python")
# #方法2
# '''self参数'''
# class StudyClass(object):
#     name="zhuzhu"#类属性
#     age=26
#     def gerenxinxi(self):#不断发生改变，谁调用就变成谁
#         print(self.name)
#         print(self.age)
# zz=StudyClass()
# zz.gerenxinxi()
# #方法3'''对象中的参数可以传到类中函数'''
# '''self参数'''
# class StudyClass(object):
#     def gerenxinxi(self):
#         print(self.name)#每个调用方法的对象都得有name和age
#         print(self.age)
# zz=StudyClass()
# zz.name="zhuzhu"#对象属性 
# zz.age=26
# zz.gerenxinxi()

# ww=StudyClass()
# ww.name="ww"
# ww.age=28
# ww.gerenxinxi()

#类
# class phone():
#     xinghao='pingguo'
#     faxingyear=2020

# #给类创建对象
# iPhone=phone()
# print(iPhone.xinghao)
# #对象里实际没有这个属性，但是类里有这个属性，所以直接拿类里的使用
# #添加对象属性
# iPhone.faxingdate='5月6日'
# #添加对象属性
# iPhone.xinghao='sanxing'
# #之所以称为添加属性是因为对象里没有这个属性
# #但是print也能打印出是因为拿类里的属性给类中对象用
# #一旦对象里添加该属性就在对象属性中取
# print(iPhone.xinghao)
# print(iPhone.faxingyear)
# print(iPhone.faxingdate)
# #修改类属性
# phone.xinghao='huawei'
# print(iPhone.xinghao)#sanxing*****修改类属性不影响类中对象属性
# print(phone.xinghao)

class StudyClass(object):
      '''如果不保证每个调用方法的对象都有方法中的变量，如name和age，得采用魔术方法__名字__（初始化）'''
      def __init__(self):#在创建对象时就自动进入到这个方法，无需代码调用
            '''相比于类属性的变量只在类中，init真实将变量定义到每个对象中'''
            print('-'*20)
            self.angel=98#为self空间动态添加angel变量
      def gerenxinxi(self):#在类中称为方法，在主程序称为函数
            print(self.name)#每个调用方法的对象都得有name和age
            print(self.age)
            print(self.angel)
zz=StudyClass()
#1、找类；
#2、向类申请一模一样的空间；
#3、找是否有init，如果有执行init然后给zz分配内存以及地址，传地址给self；
#4、如果没有init就直接开辟内存地址给zz
zz.name="zhuzhu"#对象属性 
zz.age=26
zz.gerenxinxi()

ww=StudyClass()
ww.name="ww"
ww.age=28
ww.gerenxinxi()
