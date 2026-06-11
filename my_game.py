<<<<<<< HEAD
import random
num1=random.randint(1,100)
print(num1)
x=0
while x<3: 
     i=int(input('请输入你想要输入的数字：'))
     if num1<i:
          print("输入数字过大")
     elif num1>i:
          print("输入数字过小")
     elif num1==i:
          print("恭喜你，猜对了")
          break
     x+=1
if x==3 and i!=num1 :
     print(f"正确答案为{num1}")
=======
import random
num1=random.randint(1,100)
print(num1)
x=0
while x<3: 
     i=int(input('请输入你想要输入的数字：'))
     if num1<i:
          print("输入数字过大")
     elif num1>i:
          print("输入数字过小")
     elif num1==i:
          print("恭喜你，猜对了")
          break
     x+=1
if x==3 and i!=num1 :
     print(f"正确答案为{num1}")
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
