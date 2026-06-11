

###
#求1-3+5-7+9-11+....+99等于多少
i=1
s=0
while i<=50:
    if i%2==0:
        s=s-2*i+1
    else:
        s=s+2*i-1
    i=i+1
print(s)
#第二种方法，引入符号变量
i=1
s=0
fu=1
while i<=99:
    if i%2==1:     #只要奇数
        s=s+i*fu
        fu=-fu  #+1，-3，+5，-7，把符号看作数字的一部分进行加和运算
#注意鉴别和下面运算的区别，这步和s在同一列说明这一步嵌套在if语句里而不是是嵌套在while循环语句里，说明每次当i赋新奇数值fu都要变号
    i=i+1
print(s)#在while循环外，所以只出一个结果

#求1+3+5+7+9+11+....+99等于多少，用引入符号变量法
i=1
s=0
fu=1
while i<=99:
    if i%2==1:     #只要奇数
        s=s+i*fu
    fu=-fu  
#注意鉴别和上面运算的区别，这步和if在同一列说明这一步并非嵌套在if语句里而是嵌套在循环语句里，说明每次给i赋新值不论是奇数还是偶数fu都要变号
    i=i+1
print(s)
#用break打断while循环
while True: #作为关键字True第一个字母T要大写
    content=input("请输入一些字符，遇到退出则退出：") #input也是可以像print一样打印出引号内的内容
    if content=="退出":
        break#break是退出当前while循环
        
    print("我想说的话是：%s" %content)#在当前while循环内
