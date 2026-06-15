"""如果一个函数有一个返回值，并且只有一句代码，可以使用lambda简化"""
'''
lambda也叫匿名函数
lambda语法：lambda 参数列表：表达式或者返回值
lambda表达式的参数可有可无，函数的参数在lambda表达式中完全适用
lanbda表达式能接收任何数量的参数但只能返回一个表达式的值
'''
# #函数
# def f1():
#     return 200

# print(f1)#打印lambda内存地址
# print(f1())#返回值200，调用函数

# #lambda 匿名函数
# f2=lambda:100
# print(f2)#打印lambda内存地址
# print(f2())#返回值100 调用函数

# #函数
# def adds(a,b):
#     return a+b

# result=adds(1,3)
# print(result)

# #lambda
# f3=lambda a,b :a+b
# print(f3(1,3))

# '''lambda参数形式'''
# #无参数 
# f4=lambda : 100
# print(f4())

# #一个参数
# f5=lambda a:a
# print(f5('hello!'))

# #默认参数
# f6=lambda a,b,c=100: a+b+c
# print(f6(100,50))
# print(f6(100,50,200))

# #可变参数*args
# f7=lambda *args:args
# print(f7(20,18,27))

# #可变参数**kwargs
# f8=lambda **kwargs:kwargs
# print(f8(name='hyy',age=27))

'''lambda的应用'''
#带判断的lambda
f9=lambda a,b:a if a>b else b
print(f9(10,80))
#列表数据按字典key的值排序
gerenxinxi=[{"name":"hyy","age":28},
            {'name':'zwy','age':27},
            {'name':'qyy','age':26}]
#按照字典的name值进行升序排序
gerenxinxi.sort(key=lambda x:x["name"])
print(gerenxinxi)
#按照字典的name值进行降序排序
gerenxinxi.sort(key=lambda x:x["name"],reverse=True)
print(gerenxinxi)
#按照字典的age值进行升序排序
gerenxinxi.sort(key=lambda x:x["age"])
print(gerenxinxi)
#按照字典的age值进行降序排序
gerenxinxi.sort(key=lambda x:x["age"],reverse=True)
print(gerenxinxi)