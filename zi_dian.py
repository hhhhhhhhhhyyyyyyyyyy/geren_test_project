<<<<<<< HEAD
#[ip,usename,password,fuwu1,fuwu2,cpu型号,cpu主频,内存型号,内存主频,硬盘]
#{}，dict()，key:value
#对于key的要求：
#1、不能重复，不然两个一摸一样的key，后面的会覆盖前面的；
#2、必须是不可变的数据类型，在python当中被称为可hash
#查询方式1
dict={"ip":"198.165.65.7","cpu型号":"17-12700K","CPU主频":"4.9GHZ"}#通过key可以取到value
print(dict["ip"])#如果key不存在会报错
#查询方式2
print(dict.get("ip1","不存在"))#如果key不存在不会报错，会返回不存在
#循环查询
#for key in dict:
for i in dict:
    print(i,dict[i])
print(dict.values())
#for v in dict.values():
for v in dict.values():
    print(v)
#for i,v in dict.item()
for i,v in dict.items():
    print(i,v)


#新增字典数据
#dict[key]=value
dict["userame"]="dire"
dict["passwords"]="253424"
print(dict["userame"])
print(dict)

#修改字典数据(只能修改value，key修改不了)
dict["passwords"]="123456"
print(dict)

#删除字典数据，根据key来删除
dict.pop("userame")
print(dict)

#字典嵌套
dict={"name":"yanyan",
      "age":26,
      "height":160,
      "hushand":{"name":"zhizhi",
                 "age":28,
                 "height":180,
                 "ex_wife":{"age":30,
                            "height":165,
                            "name":"lili"}}}
print(dict["hushand"]["ex_wife"]["name"])

#字典嵌套数据修改
dict["hushand"]["ex_wife"]["age"]=40
print(dict)

#字典嵌套列表
dict={"name":"yanyan",
      "age":26,
      "height":160,
      "children":[{"name":"holy","age":14,"hobby":['王者荣耀','和平精英','三角洲']},
                  {"name":"bule","age":18,"hobby":['王者荣耀','打瓦']},
                  {"name":"boby","age":11,"hobby":['看书']}]}
print(dict["children"][1]["hobby"][1])#输出的是孩子2的爱好,hobby[1]:打瓦
#想看到每个孩子的名字和年龄
for i in dict["children"]:#i表示children中的每一项，也就是每一个孩子的信息
    g=i["name"]
    h=i["age"]
    print(g,h)

=======
#[ip,usename,password,fuwu1,fuwu2,cpu型号,cpu主频,内存型号,内存主频,硬盘]
#{}，dict()，key:value
#对于key的要求：
#1、不能重复，不然两个一摸一样的key，后面的会覆盖前面的；
#2、必须是不可变的数据类型，在python当中被称为可hash
#查询方式1
dict={"ip":"198.165.65.7","cpu型号":"17-12700K","CPU主频":"4.9GHZ"}#通过key可以取到value
print(dict["ip"])#如果key不存在会报错
#查询方式2
print(dict.get("ip1","不存在"))#如果key不存在不会报错，会返回不存在
#循环查询
#for key in dict:
for i in dict:
    print(i,dict[i])
print(dict.values())
#for v in dict.values():
for v in dict.values():
    print(v)
#for i,v in dict.item()
for i,v in dict.items():
    print(i,v)


#新增字典数据
#dict[key]=value
dict["userame"]="dire"
dict["passwords"]="253424"
print(dict["userame"])
print(dict)

#修改字典数据(只能修改value，key修改不了)
dict["passwords"]="123456"
print(dict)

#删除字典数据，根据key来删除
dict.pop("userame")
print(dict)

#字典嵌套
dict={"name":"yanyan",
      "age":26,
      "height":160,
      "hushand":{"name":"zhizhi",
                 "age":28,
                 "height":180,
                 "ex_wife":{"age":30,
                            "height":165,
                            "name":"lili"}}}
print(dict["hushand"]["ex_wife"]["name"])

#字典嵌套数据修改
dict["hushand"]["ex_wife"]["age"]=40
print(dict)

#字典嵌套列表
dict={"name":"yanyan",
      "age":26,
      "height":160,
      "children":[{"name":"holy","age":14,"hobby":['王者荣耀','和平精英','三角洲']},
                  {"name":"bule","age":18,"hobby":['王者荣耀','打瓦']},
                  {"name":"boby","age":11,"hobby":['看书']}]}
print(dict["children"][1]["hobby"][1])#输出的是孩子2的爱好,hobby[1]:打瓦
#想看到每个孩子的名字和年龄
for i in dict["children"]:#i表示children中的每一项，也就是每一个孩子的信息
    g=i["name"]
    h=i["age"]
    print(g,h)

>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
