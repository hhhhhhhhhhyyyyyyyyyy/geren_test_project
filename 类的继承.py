# class father():
#     __name2='mother'
#     name='father'
#     def eating(self):
#         print("father's eating diet")
#         return self.__name2
    
#     def drink(self):
#         print('father drink')

# class son(father):
#     def eating2(self):
#         print("son's diet")
    
#     def drink(self):
#         super().drink()#father drink  防重写方法1
#         super(son,self).drink()#father drink  防重写方法1
        
        

# d=son()
# x=d.eating()
# print(x)
# print(d.name)#父类里所有的属性方法都可以调用
# father().drink()#father drink 防重写方法3
# d.eating2()
# d.drink()



'''深度优先机制：当对象调用方法时，
查找顺序先从自身类找，
如果自身类没找到，
则去取父类找，父类没有再去父类的父类找，直到object类（顶层基类）
若还无，则报错

当子类和父类拥有的方法名字一样时，
子类对象调用该方法优先执行自身的方法，
那么实际上就是子类的方法覆盖父类的方法，也称为重写,
比如父类和子类里都有drink这个方法，如果我想在子类里调用父类的drink方法
则可以用super()'''


'''以下为多继承'''
class grandfather():
    def play22(self):
        print('grandfather喜欢玩球')

class father1(grandfather):
    def play(self):
        print('father1喜欢玩球')



class father2(grandfather):
    def play(self):
        print('father2喜欢玩球')
    def play22(self):
        print('grandfather22喜欢玩球')

class son(father1,father2):#遵循左边优先原则，谁在左边优先调用谁
    def play11():
        pass


s=son()
s.play()#father1喜欢玩球
s.play22()
#grandfather22喜欢玩球  
# 优先遍历father，先遵循左边优先原则遍历father1和father2
#father1和father2都没有就去grandfather里找