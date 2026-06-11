<<<<<<< HEAD
'''公共操作：
1、+：表示合并，适用于字符串，列表，元组
2、*：表示复制，适用于字符串，列表，元组
3、in：元素是否存在，适用于字符串，列表，元组，字典
4、not in：元素是否不存在，适用于字符串，列表，元组，字典
'''
b="sgdgkj"
c="wgsyguqgs"

d=[11,22,"wosh"]
print(22 in d)#True

e=[32,(22,54)]
print(22 in e)#False

f=[{23:34,56:78}]
print(23 in f)#False
print(34 in f)#False

g=(23,34,"sggdjw")
print('s' in g)#False
print('s ' in g)#False

h=(23,23,(23,12))
print(12 in h)#False

i=({23:24,12:67},)
print(23 in i)#False
print(24 in i)#False

j={"wo":"ni","qu":"lai"}
print('w' in j)##False
print('wo' in j)#True
'''字典里的key和value可以被判断是否在内'''
print('wo' in j.keys())#True
print('wo' in j.values())#False

#*
print(b*2)
print(d*2,e*2,f*2)
print(g*2,h*2,i*2)

#in 和 not in
"""常用于if判断"""
print('a' in b)
print('a' not in b)
"""
由此可见，in或者not in 只能判断字符串里某个字符；
字典，元组，列表里整个元素，
如果字符串，字典，列表，元组里嵌套字典，
列表，元组，字符串将被嵌套的整体看作一个元素，
不能感知到被嵌套的整体里还有哪些嵌套的部分元素
"""

'''
1、len()计算容器中元素个数
2、del()删除：格式  del 目标或者del（目标）
3、max()返回容器中元素最大值
4、min()返回容器中元素最小值
5、range(start,end,step)生成从start到end的数字 步长为step，一般用在for循环当中
6、enumerate(可遍历对象，start=)用于将一个可遍历的数据对象组合（列表，元组，字符串）作为一个索引序列，同时标出数据和数据下标，一般用在for循环当中
'''
print(max(b))
print(min(c))#根据字母表顺序决定大小

k=[12,28,90,23,10,26]
print(max(k))
print(min(k))

v=range(0,10,1)
print(v)#答案为range(0, 10)
for i in range(0,10,1):
    print(i)
'''不写步长默认步长为1，不写start默认为0，range(10)
即可单独省略步长，也可步长和起始值一起省略，但一般没有只省略起始值的'''



l=[12,35,22,56]
for i in enumerate(l):
      print(i)
'''enumerate(可遍历对象，start=)，start用来设置遍历数据下标的起始值，默认为0，start可省略
(0, 12)
(1, 35)
(2, 22)
(3, 56)
可见返回值是元素下角标和元素本身的值
并且返回类型是元组
'''
m=[12,35,22,56,88]
for i in enumerate(m,start=1):
      print(i)

'''
tuple()元组类型
set()集合类型（无序，不支持下标，且具有去重功能）
list()列表类型
这三种类型可两两相互转换
=======
'''公共操作：
1、+：表示合并，适用于字符串，列表，元组
2、*：表示复制，适用于字符串，列表，元组
3、in：元素是否存在，适用于字符串，列表，元组，字典
4、not in：元素是否不存在，适用于字符串，列表，元组，字典
'''
b="sgdgkj"
c="wgsyguqgs"

d=[11,22,"wosh"]
print(22 in d)#True

e=[32,(22,54)]
print(22 in e)#False

f=[{23:34,56:78}]
print(23 in f)#False
print(34 in f)#False

g=(23,34,"sggdjw")
print('s' in g)#False
print('s ' in g)#False

h=(23,23,(23,12))
print(12 in h)#False

i=({23:24,12:67},)
print(23 in i)#False
print(24 in i)#False

j={"wo":"ni","qu":"lai"}
print('w' in j)##False
print('wo' in j)#True
'''字典里的key和value可以被判断是否在内'''
print('wo' in j.keys())#True
print('wo' in j.values())#False

#*
print(b*2)
print(d*2,e*2,f*2)
print(g*2,h*2,i*2)

#in 和 not in
"""常用于if判断"""
print('a' in b)
print('a' not in b)
"""
由此可见，in或者not in 只能判断字符串里某个字符；
字典，元组，列表里整个元素，
如果字符串，字典，列表，元组里嵌套字典，
列表，元组，字符串将被嵌套的整体看作一个元素，
不能感知到被嵌套的整体里还有哪些嵌套的部分元素
"""

'''
1、len()计算容器中元素个数
2、del()删除：格式  del 目标或者del（目标）
3、max()返回容器中元素最大值
4、min()返回容器中元素最小值
5、range(start,end,step)生成从start到end的数字 步长为step，一般用在for循环当中
6、enumerate(可遍历对象，start=)用于将一个可遍历的数据对象组合（列表，元组，字符串）作为一个索引序列，同时标出数据和数据下标，一般用在for循环当中
'''
print(max(b))
print(min(c))#根据字母表顺序决定大小

k=[12,28,90,23,10,26]
print(max(k))
print(min(k))

v=range(0,10,1)
print(v)#答案为range(0, 10)
for i in range(0,10,1):
    print(i)
'''不写步长默认步长为1，不写start默认为0，range(10)
即可单独省略步长，也可步长和起始值一起省略，但一般没有只省略起始值的'''



l=[12,35,22,56]
for i in enumerate(l):
      print(i)
'''enumerate(可遍历对象，start=)，start用来设置遍历数据下标的起始值，默认为0，start可省略
(0, 12)
(1, 35)
(2, 22)
(3, 56)
可见返回值是元素下角标和元素本身的值
并且返回类型是元组
'''
m=[12,35,22,56,88]
for i in enumerate(m,start=1):
      print(i)

'''
tuple()元组类型
set()集合类型（无序，不支持下标，且具有去重功能）
list()列表类型
这三种类型可两两相互转换
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
'''