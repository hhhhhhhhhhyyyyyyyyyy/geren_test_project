numbers=[1,2,3,4,5,6,7,8,9]
for i in numbers:
    for h in numbers:
        if i<=h:
            j=i*h
            print(f"{i}*{h}={j}",end="\t")#每个式子和前一个式子都相差一个空格
    print() #相当于print(end="\n")换行