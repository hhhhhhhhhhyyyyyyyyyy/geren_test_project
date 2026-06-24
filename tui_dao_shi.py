

# '''
# 有且只有列表，字典，集合有推导式，作用是简化代码
# '''
# #列表推导式又叫列表生成式
# list1=[i for i in range(10)]
# print(list1)

# '''1、生成偶数列表'''
# list2=[i for i in range(0,10,2)]
# print(list2)

# list3=[i for i in range(10) if i%2==0]
# print(list3)

# '''2、生成列表'''
# lis7=[f"乡村爱情{i}" for i in range(1,13)]
# print(lis7)
# #['乡村爱情1', '乡村爱情2', '乡村爱情3', '乡村爱情4', 
# # '乡村爱情5', '乡村爱情6', '乡村爱情7', '乡村爱情8', '乡村爱情9', 
# # '乡村爱情10', '乡村爱情11', '乡村爱情12']

# '''3、在列表推导式中筛选数据并修改'''
# lis8=['张无忌','张三丰','李明玉','王二狗','谢逊']#要求将张姓修改为李姓
# lis9=[i.replace('张','李') for i in lis8 if i.startswith('张')]
# print(lis9)#['李无忌', '李三丰']


# lis0=[]
# for i in lis8:
#     if i[0]=="张":
#         i='李'+i[1:]
#         lis0.append(i)
#     else:
#         lis0.append(i)
# print(lis0)
# '''4、生成元组规律列表'''
# list4=[(i,j) for i in range(1,3) for j in range(2,4)]
# print(list4)#[(1, 2), (1, 3), (2, 2), (2, 3)] 

# #集合推导式
# set1={1,3,2,4,33,2,1,3}
# set2={i**2 for i in set1}#求集合set1里元素的平方再放到set2集合里 i**2表示i的平方
# print(set2)#{1, 1089, 4, 9, 16}具有去重功能


# #字典推导式
# '''将两个列表类型的变量组合成一个字典'''
# list5=["姓名","年龄","身高"]
# list6=["何妍妍",26,158]
# ge_ren_xin_xi={}
# for i in range(len(list5)):
#     k=list5[i]
#     v=list6[i]
#     ge_ren_xin_xi[k]=v
# print(ge_ren_xin_xi)

# ge_ren_xin_xi={list5[i]:list6[i] for i in range(len(list5))}
# print(ge_ren_xin_xi)
# #如果两个列表数据个数相同，len(任选一个列表填写)；
# #如果两个列表数据个数不一样，len(选择个数少的列表填入)

# '''字典推导式可用于快速筛选目标数据'''
# xi_tong_shu_ju={"sd":206,"ed":24,"cd":67,"hd":599,"ad":799}
# xi_tong_shu_ju2={k:v for k,v in xi_tong_shu_ju.items() if v>200}
# print(xi_tong_shu_ju2)
# #选择的目标数据大于200


# '''
# 1、列表推导式：[结果 for循环 if条件]
# 2、字典推导式：{key:value for循环 if条件}
# 3、集合推导式：{key  for循环 if条件}
# 无元组推导式
# 生成器表达式：(结果 for循环 if条件)
# '''
# lis11=(f"乡村爱情{i}" for i in range(1,13))#生成器
# for item in lis11:
#      print(item)

def func():
    print(111)
    yield 222


g=func()#创建一个空生成器
'''不会执行函数内部print(111)'''
g1=(i for i in g)#生成器推导式，依赖g
g2=(i for i in g1)#生成器推导式，依赖g1
'''生成器推导式同样具有惰性，
此时不会读取g里的数据，
只是记录：g1要从g里拿数据，g2要从g1里拿数据
'''

print(list(g))#强制遍历生成器g
'''其过程：
1、进入func()函数，执行print(111),打印111
2、碰到yield，将222返回给list(g)
3、函数执行完毕，生成器彻底耗尽，永久清空，再也拿不出任何值
4、list收集到[222],打印结果[222]'''
print(list(g1))#强制遍历生成器g1
'''因为g1数据源是g，但g已经被遍历空了，g1循环取值什么都取不到，最终形成空列表

'''
print(list(g2))
'''因为g2数据源是g1，但g1本来就是空列表，g2循环取值什么都取不到，最终形成空列表

'''
# 111
# [222]
# []
# []