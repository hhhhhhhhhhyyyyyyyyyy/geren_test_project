i=0
s=0
while i<=9:
    i=i+1
    if i%2==0:#把偶数过滤掉
        continue
    s=s+i
    print(i)
    print(s)
    #不能把i=i+1放在这一行，因为continue会跳过当前while循环里的代码，即遇到偶数时不会执行i=i+1，陷入死循环
    #continue过滤掉本次循环然后进入下一次循环
#进行1+3+5+7+9这个运算
#1. continue：跳过「本轮剩下代码」，直接开启下一轮循环 
#2. break：直接彻底跳出整个while循环，循环永久结束

