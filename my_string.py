#写字符的几种形式
s1="字符串hengigu"
s2='zifuchuan'
s3="""shgugkgugk"""
s4='''shgjgdjkgdkqgdk'''
#字符串索引
print(s1[0])#索引从左往右0开始计算 字
print(s1[6])#g
print(s1[-1])#索引从右向左计算从-1开始  u
#字符串切片
print(s2[2:4])#fu  这个表示，从0开始数，取s2的第二个元素，然后往后取4-2=2个元素
print(s2[:6])#zifuch 相当于s2[0:6]
print(s2[6:])#uan
print(s2[-6:-1])#uchua
#[h1,h2]里h2这个数字位置所在字符都取不到，即便是负号也是从前往后取
#[start:stop:step]
print(s3[::3])
#表示从头到尾每3个选一个，将s3里包含的字符串分组，每三个分为一组，取每一组的第一个字符
#比如shgugkgugk，分为shg ugk gug k这几组，取每组的第一个字符，则是sugk这几个字符
print(s3[-1:-8:-3])
#表示从尾到头 每3个选一个，将s3里包含的字符串分组，每三个分为一组，取每一组的第一个字符
#比如shgugkgugk，从尾到头分为kgu gkg u这几组(因为是从[-1:-8]这几个字符里分组)，取每组的第一个字符，则是kgu这几个字符
#只要step是负数，就得从右往左数
print(s3[::-2])
#这个语法一般用来判断是不是回文
h1="shgdjsgggsjdghs"
h=h1[::-1]
if h1==h:
    print("h1是回文")
else:
    print("h1不是回文")
    