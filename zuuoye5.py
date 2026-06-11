cheng_ji={"小虎":{"数学":99,"语文":66,"英语":98},
          "小杨":{"数学":79,"语文":64,"英语":100},
          "月月":{"数学":99,"语文":90,"英语":100}}
def chaxun(name1):
    #字典推导式里所有的变量都是暂时的，出了字典表达式就会消失
    #所以这里不适合用字典推导式，还是乖乖用循环
    for k,v in cheng_ji.items():
        if k==name1:
           print(v)#cheng_ji1.values()不可以写这个
           return v
       
def aves():
    h=chaxun(z)
    sum1=0
    for m in h.values():
       sum1=m+sum1
    q=sum1/3
    return q
    
while 1:
    z=input("请输入要查询学生的名字：")
    if z not in cheng_ji:
        if z!="quit":
            print("输入姓名有误，请重新输入")
            continue
        else:
            break
    else:
        x=aves()
        print(x)
    continue
    



