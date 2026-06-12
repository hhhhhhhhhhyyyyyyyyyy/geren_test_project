#定义功能界面函数
def info_print():
    print("请选择功能：")
    print("1、新增学员")
    print("2、删除学员")
    print("3、修改学员")
    print("4、查询学员")
    print("5、显示所有学员")
    print("6、退出系统")
    print("-"*20)

#显示功能界面
info_print()
#等待存储所有学员信息
info=[]
#用户输入功能序号




"""添加学员模块函数"""
def add_info():
    global info
#接受用户输入学员信息并保存，学员基本信息有姓名，id，电话
    user_name=input("请输入学员姓名：")
    user_id=input("请输入学员id：")
    user_tel=input("请输入学员电话：")
#判断是否添加学员，如果学员信息已存在，则报错提示；
    for i in info:
         if user_name==i["name"]:
              print("该学员已存在")
              return 
#如果学员已存在，return就结束函数返回主程序，如果这里用break下面的代码不在for循环里依旧会被执行，会产生列表添加重复元素
#如果学员信息不存在，则准备空字典，将用户输入的数据追加到空字典，再列表追加字典数据   
#对应if条件成立的句子调用该函数
         """else:
            user_dict={}
            user_dict["name"]=user_name  #字典索引都需要加双引号
            user_dict["id"]=user_id
            user_dict["tel"]=user_tel
            info.append(user_dict)不可以这样写，因为这样写意味着经过几次循环就加几个同样的字典信息到列表"""
    user_dict={}
    user_dict["name"]=user_name  #字典索引都需要加双引号
    user_dict["id"]=user_id
    user_dict["tel"]=user_tel
    info.append(user_dict)


'''删除学员模块函数'''
def del_info(): 
         global info    
#按用户输入的学员姓名进行删除
#用户输入目标学员姓名
         user_name=input("请输入学员姓名：")
#检查这个学员是否存在
#存在则该列表删除这个数据
#不存在则显示“该用户不存在”
#对应if条件成立的句子调用该函数
         for i in info:
           if user_name==i["name"]:
                info.remove(i)
                break
         else:
             print("该用户不存在")
"""重点：
关键在于 Python 的for-else语法规则：
 
- else代码块，只有在整个for循环完整跑完、且从未被break打断时，才会执行 1 次。

- 循环里只要触发了break ， else就会直接跳过，永远不执行。"""
#这里细品一下为什么用break而不是return，因为只是想跳出循环而不是想跳出整个函数
#至于else代码块只会执行一次，意味着该代码中的“该用户不存在”只会打印一次          
           
""" 
if user_name!=i["name"]:
    print("该用户不存在")
else:
    info.remove(i)
如果这样写的话会有很多次输出用户不存在，而我们只需要系统输出一次用户不存在即可"""
               
                

'''修改学员信息模块函数'''
#用户输入目标学员姓名，检查这个学员是否存在
#如果存在则修改学员信息，不存在则报错
#对应if条件成立的句子调用该函数
def modify_info():
     user_name=input("请输入学员姓名：")
     global info
     for i in info:
          if user_name==i["name"]:
               x=input("请选择你要修改的项目：（tel，id）")
               y=int(input("请输入数字:"))
               i[x]=y
               break
     else:
          print("该学员不存在")


'''查询学员信息模块函数'''
#用户输入目标学员姓名，检查这个学员是否存在
#如果存在则显示学员信息，不存在则报错
#对应if条件成立的句子调用该函数
def search_info():
     user_name=input("请输入学员姓名：")
     global info
     for i in info:
          if user_name==i["name"]:
               a=i["name"]
               b=i["id"]
               c=i["tel"]
               print("查找到的学员信息如下：")
               print(f"该学员姓名为{a}，id为{b}，电话为{c}")
               break
     else:
          print("该学员不存在")


'''显示所有学员信息模块函数'''
#打印所有学员信息
def print_all():
     print('学号\t姓名\t电话')
     for i in info:
          a=i["name"]
          b=i["id"]
          c=i["tel"]
          print(f"{a}\t{b}\t{c}")

#按照用户输入的不同序号，执行不同的功能。
#如果用户输入1，执行添加；如果用户输入2，执行删除
while 1:
     x=int(input("请输入功能序号："))
     if x==1:
          print("新增")
          add_info()
          print(info)
     elif x==2:
          print("删除")
          del_info()
          print(info)
     elif x==3:
          print("修改")
          modify_info()
          print(info)
     elif x==4:
          print("查询")
          search_info()
          print(info)
     elif x==5:
          print("显示所有学员")
          print_all()
          print(info)
     elif x==6:
          print("退出系统")
          break
     else:
          print("输入有误，请重新输入：")
     continue