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
#创建类：学生类，创建对象：张三，在类中定义方法输出：张三学习python
#方法1
class StudentsClass:#类
    def study_python(self,name):#类中函数，称为方法
        print(f"张三爱学习{name}!")
zs=StudentsClass()#创建对象，整个过程成为实例化
zs.study_python("python")
#方法2
'''self参数'''
class StudyClass(object):
    name="zhuzhu"
    age=26
    def gerenxinxi(self):
        print(self.name)
        print(self.age)
zz=StudyClass()
zz.gerenxinxi()
#方法3
'''self参数'''
class StudyClass(object):
    def gerenxinxi(self):
        print(self.name)
        print(self.age)
zz=StudyClass()
zz.name="zhuzhu"
zz.age=26
zz.gerenxinxi()

ww=StudyClass()
ww.name="ww"
ww.age=28
ww.gerenxinxi()