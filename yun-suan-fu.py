#算数运算  +  -   *   %(取余数)  //(除完之后取商的整数部分)    /(除法，不管能不能整除，结果永远是float型数，6/2=3.0)
#比较运算  <  >   <=  >=   ==     !=(不等于)     is(判断是否是同一个对象)    not is（判断是否不是同一个对象）
#a='另一只猫'
#b="另一只猫"
#a is b   #判断两只猫是否是同一只
#a==b     #判断两只猫是否花色，颜色等一致，类似双胞胎
#is一般用来判断是否为空
a=None
print(a is None)
#赋值运算  a=a+1也可写作a+=1
#逻辑运算   and   or   not  组合怎么计算？   (a  and   b)  and  (c  or  d)
#运算优先级  （） >  not  >   and   >   or
# 0可以表示假，非0可以表示真，所以，0 and 2 因为0为假，所以and不会去判断后面，直接输出0，即有一个假就是假
print(2 and 4)#两个都真输出后面的4
print(33 or 28) #判断第一个为真，or不会看后面，直接输出33，即有一个真都是真
print(2 and 0)#第一个真判断第二个，第二个为假，输出后面的0
print(0 or  88)#判断第一个为假，or要去判断第二个，发现第二个为真，输出88
#成员运算 判断一个字符串里有没有某个字符 in   not in
s="sggugkggkgjv我爱中国"
print("中国"in s)
print("gg"not in s)

#bool类型
print(bool(0))#flase
print(bool(4))#true
print(bool("字符串"))#true
print(bool(" "))#有空格 true
print(bool(""))#false
print(bool())#false
print(bool([1,2,3]))#true
print(bool([""]))#true
print(bool([]))#false
print(bool(None))#false
#0,""空字符串,{}空字典，()空元组,[]空列表,b''空字节,set()空集合，None   都表示空

