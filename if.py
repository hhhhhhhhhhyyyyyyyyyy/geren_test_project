<<<<<<< HEAD
#if语句三种基本格式

print("请输入您的年纪：")
age=int(input())

#1、只有if

if age<18:
   print("未成年")
else:
   pass
#2、if.....else.....

if age<18:
   print("未成年")
else:
   print("成年人")

#3、if....elif....

if age<18:
   print("未成年")
elif age<30:
   print("青年")
elif age<50:
   print("壮年")
elif age<100:
   print("老年")
else: 
   print("已到百岁，长寿之人")

#4、if嵌套

if age>18:
    if age>30:
       print("是否到达结婚条件？")
       a=input()
       if a=="是":
          print("可以领取结婚证")
       else:
          print("不可以领取结婚证")
    else: 
       print("不可以领取结婚证")
else:
    print("不可以领取结婚证")

#5、and使用，or使用，not使用
=======
#if语句三种基本格式

print("请输入您的年纪：")
age=int(input())

#1、只有if

if age<18:
   print("未成年")
else:
   pass
#2、if.....else.....

if age<18:
   print("未成年")
else:
   print("成年人")

#3、if....elif....

if age<18:
   print("未成年")
elif age<30:
   print("青年")
elif age<50:
   print("壮年")
elif age<100:
   print("老年")
else: 
   print("已到百岁，长寿之人")

#4、if嵌套

if age>18:
    if age>30:
       print("是否到达结婚条件？")
       a=input()
       if a=="是":
          print("可以领取结婚证")
       else:
          print("不可以领取结婚证")
    else: 
       print("不可以领取结婚证")
else:
    print("不可以领取结婚证")

#5、and使用，or使用，not使用
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
