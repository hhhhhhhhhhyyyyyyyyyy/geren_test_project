<<<<<<< HEAD
#range用法
print(list(range(5)))
print(list(range(1,10,2)))
print(list(range(10,1,-2)))
#for循环基础框架
for i in range(10):#控制循环次数
    print("拍篮球")
#使用for循环将奇数和偶数分开
numbers=[21,236,44,26,77,92,75,66]
oushu=[]
jishu=[]
for i in numbers:
    if i%2==0:
        oushu.append(i)
#返回值就是oushu这个列表本身，所以不用再定义一个变量盛放b=oushu.append(i)是错的
    else:
        jishu.append(i)
print(oushu)
=======
#range用法
print(list(range(5)))
print(list(range(1,10,2)))
print(list(range(10,1,-2)))
#for循环基础框架
for i in range(10):#控制循环次数
    print("拍篮球")
#使用for循环将奇数和偶数分开
numbers=[21,236,44,26,77,92,75,66]
oushu=[]
jishu=[]
for i in numbers:
    if i%2==0:
        oushu.append(i)
#返回值就是oushu这个列表本身，所以不用再定义一个变量盛放b=oushu.append(i)是错的
    else:
        jishu.append(i)
print(oushu)
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
print(jishu)