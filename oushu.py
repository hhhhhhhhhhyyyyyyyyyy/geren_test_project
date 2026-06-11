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
print(jishu)