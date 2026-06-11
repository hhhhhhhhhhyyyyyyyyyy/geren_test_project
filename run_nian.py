print("请输入一个年份：")
year=int(input())
a=year%100
b=year%4
c=year%400
print(a,b,c)
if c==0:
    print("闰年")
elif a==0 and not c==0:
    print("平年")
elif not a==0 and b==0:
    print("闰年")
else:
    print("平年")