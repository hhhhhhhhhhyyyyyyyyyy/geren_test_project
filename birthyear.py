print("请输入您的年龄：")
age1=input()         #input输入的数据默认是字符串，需要转化成整数类型
print(age1)
age=float(age1)  
#可转化成整数型数据int也可转化成浮点型数据float
print(age)
#若是整数型数据用print（）输出为26，浮点型数据输出为26.0
print("请输入今年的年份：")
year=int(input())     #也可以试着写year=int(input())
print(year)
birthyear=year-age   #现在的年份减去年龄等于出生年份
print("您的出生年份为：\n")#换行符为\n,而不是/n
print(birthyear)
