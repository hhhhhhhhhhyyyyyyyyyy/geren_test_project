'''
有且只有列表，字典，集合有推导式，作用是简化代码
'''
#列表推导式又叫列表生成式
list1=[i for i in range(10)]
print(list1)
'''1、生成偶数列表'''
list2=[i for i in range(0,10,2)]
print(list2)

list3=[i for i in range(10) if i%2==0]
print(list3)

'''2、生成元组规律列表'''
list4=[(i,j) for i in range(1,3) for j in range(2,4)]
print(list4)#[(1, 2), (1, 3), (2, 2), (2, 3)] 

#集合推导式
set1={1,3,2,4,33,2,1,3}
set2={i**2 for i in set1}#求集合set1里元素的平方再放到set2集合里 i**2表示i的平方
print(set2)#{1, 1089, 4, 9, 16}具有去重功能


#字典推导式
'''将两个列表类型的变量组合成一个字典'''
list5=["姓名","年龄","身高"]
list6=["何妍妍",26,158]
ge_ren_xin_xi={}
for i in range(len(list5)):
    k=list5[i]
    v=list6[i]
    ge_ren_xin_xi[k]=v
print(ge_ren_xin_xi)

ge_ren_xin_xi={list5[i]:list6[i] for i in range(len(list5))}
print(ge_ren_xin_xi)
#如果两个列表数据个数相同，len(任选一个列表填写)；
#如果两个列表数据个数不一样，len(选择个数少的列表填入)

'''字典推导式可用于快速筛选目标数据'''
xi_tong_shu_ju={"sd":206,"ed":24,"cd":67,"hd":599,"ad":799}
xi_tong_shu_ju2={k:v for k,v in xi_tong_shu_ju.items() if v>200}
print(xi_tong_shu_ju2)
#选择的目标数据大于200
