<<<<<<< HEAD
#格式化输出
name="jj"
age=26
print(f"我叫{name},我今年{age}岁了")#f-string格式化输出
print(f"我叫{name},我今年{age+3}岁了")#大括号里可以进行运算
print("我叫%s,我今年%d岁了" %(name,age))#不可以写成print("我叫%s,我今年%d岁了")%(name,age)
#这样写也是不行的：print("我叫%s,我今年%d岁了" %name %age) 会报错说2个占位符（%s，%d）只有一个数据（%name）
print("我今年%d岁" %age)
=======
#格式化输出
name="jj"
age=26
print(f"我叫{name},我今年{age}岁了")#f-string格式化输出
print(f"我叫{name},我今年{age+3}岁了")#大括号里可以进行运算
print("我叫%s,我今年%d岁了" %(name,age))#不可以写成print("我叫%s,我今年%d岁了")%(name,age)
#这样写也是不行的：print("我叫%s,我今年%d岁了" %name %age) 会报错说2个占位符（%s，%d）只有一个数据（%name）
print("我今年%d岁" %age)
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
#格式化输出格式f"xxxxx{变量或者表达式}xxxxxxx"