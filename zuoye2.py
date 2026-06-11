<<<<<<< HEAD
jiao_wu_xi_tong={}
jiao_wu_xi_tong['甜甜']="97"
jiao_wu_xi_tong['丫丫']="90"
jiao_wu_xi_tong['小米']="88"
jiao_wu_xi_tong['明明']="78" 
print(jiao_wu_xi_tong)
h=["新增","修改","删除","查询"]
while 1:
    i=input("请输入你要执行的操作：")#增删查改四个操作
    if i=="quit":
          break
    elif i==h[0]:
#新增
      while len(jiao_wu_xi_tong)<=10:#限制字典新增人数
            z=input("输入学生姓名：")
            if z=="quit":#如果不想新增了可以控制退出
                  break
            if z not in jiao_wu_xi_tong:
                b=int(input("输入学生成绩："))
                jiao_wu_xi_tong[z]=b
            else:
                print("该学生已存在，不用新增")
                continue
      print(jiao_wu_xi_tong)
#修改
    elif i==h[1]:
       while 1:  
          z=input("输入学生姓名：")
          if z=="quit":#如果不想修改了可以控制退出
                break
          if z in jiao_wu_xi_tong:
                    b=int(input('输入学生新的成绩：'))
                    jiao_wu_xi_tong[z]=b
          else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)
#删除
    elif i==h[2]:
       while 1:  
            z=input("输入学生姓名：")
            if z=="quit":#如果不想删除了可以控制退出
                break 
            if z in jiao_wu_xi_tong:
                     jiao_wu_xi_tong.pop(z)
            else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)
#查询
    elif i==h[3]:
       while 1:  
          z=input("输入学生姓名：")
          if z=="quit":#如果不想删除了可以控制退出
                break 
          if z in jiao_wu_xi_tong:
                     print(f"学生姓名为{z},学生成绩为{jiao_wu_xi_tong[z]}")
          else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)
    continue
                     
          
=======
jiao_wu_xi_tong={}
jiao_wu_xi_tong['甜甜']="97"
jiao_wu_xi_tong['丫丫']="90"
jiao_wu_xi_tong['小米']="88"
jiao_wu_xi_tong['明明']="78" 
print(jiao_wu_xi_tong)
h=["新增","修改","删除","查询"]
while 1:
    i=input("请输入你要执行的操作：")#增删查改四个操作
    if i=="quit":
          break
    elif i==h[0]:
#新增
      while len(jiao_wu_xi_tong)<=10:#限制字典新增人数
            z=input("输入学生姓名：")
            if z=="quit":#如果不想新增了可以控制退出
                  break
            if z not in jiao_wu_xi_tong:
                b=int(input("输入学生成绩："))
                jiao_wu_xi_tong[z]=b
            else:
                print("该学生已存在，不用新增")
                continue
      print(jiao_wu_xi_tong)
#修改
    elif i==h[1]:
       while 1:  
          z=input("输入学生姓名：")
          if z=="quit":#如果不想修改了可以控制退出
                break
          if z in jiao_wu_xi_tong:
                    b=int(input('输入学生新的成绩：'))
                    jiao_wu_xi_tong[z]=b
          else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)
#删除
    elif i==h[2]:
       while 1:  
            z=input("输入学生姓名：")
            if z=="quit":#如果不想删除了可以控制退出
                break 
            if z in jiao_wu_xi_tong:
                     jiao_wu_xi_tong.pop(z)
            else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)
#查询
    elif i==h[3]:
       while 1:  
          z=input("输入学生姓名：")
          if z=="quit":#如果不想删除了可以控制退出
                break 
          if z in jiao_wu_xi_tong:
                     print(f"学生姓名为{z},学生成绩为{jiao_wu_xi_tong[z]}")
          else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)
    continue
                     
          
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
