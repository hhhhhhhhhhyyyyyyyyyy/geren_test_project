<<<<<<< HEAD
jiao_wu_xi_tong={}
jiao_wu_xi_tong['甜甜']="97"
jiao_wu_xi_tong['丫丫']="90"
jiao_wu_xi_tong['小米']="88"
jiao_wu_xi_tong['明明']="78" 
print(jiao_wu_xi_tong)
c=["新增","删除","修改","查询","quit"]


def shu_ru_xing_ming():
          i=input("输入学生姓名：")
          return i

def shu_ru_cheng_ji():
       global b
       b=int(input("输入学生成绩："))
       return b                      

def xin_zeng():
    while len(jiao_wu_xi_tong)<=10:#限制字典新增人数
            z=shu_ru_xing_ming()
            if z=="quit":#如果不想新增了可以控制退出
                  break
            if z not in jiao_wu_xi_tong:
                shu_ru_cheng_ji()
                jiao_wu_xi_tong[z]=b
            else:
                print("该学生已存在，不用新增")
                continue
    print(jiao_wu_xi_tong)

def xiu_gai():
    while 1:  
          z=shu_ru_xing_ming()
          if z=="quit":#如果不想修改了可以控制退出
                break
          if z in jiao_wu_xi_tong:
                    shu_ru_cheng_ji()
                    jiao_wu_xi_tong[z]=b
          else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
    print(jiao_wu_xi_tong)

def shan_chu():
       while 1:  
            z=shu_ru_xing_ming()
            if z=="quit":#如果不想删除了可以控制退出
                break 
            if z in jiao_wu_xi_tong:
                     jiao_wu_xi_tong.pop(z)
            else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)

def cha_xun():
       while 1:  
          z=shu_ru_xing_ming()
          if z=="quit":#如果不想删除了可以控制退出
                break 
          if z in jiao_wu_xi_tong:
                     print(f"学生姓名为{z},学生成绩为{jiao_wu_xi_tong[z]}")
          else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)

while 1:
 h=input("请输入你想进行的操作：")#新增，删除，修改，查询
 if h==c[0]:
      xin_zeng()
 elif h==c[2]:
      xiu_gai()
 elif h==c[1]:
      shan_chu()
 elif h==c[3]:
       cha_xun()
 elif h==c[4]:
       break
 else:
       continue
       
=======
jiao_wu_xi_tong={}
jiao_wu_xi_tong['甜甜']="97"
jiao_wu_xi_tong['丫丫']="90"
jiao_wu_xi_tong['小米']="88"
jiao_wu_xi_tong['明明']="78" 
print(jiao_wu_xi_tong)
c=["新增","删除","修改","查询","quit"]


def shu_ru_xing_ming():
          i=input("输入学生姓名：")
          return i

def shu_ru_cheng_ji():
       global b
       b=int(input("输入学生成绩："))
       return b                      

def xin_zeng():
    while len(jiao_wu_xi_tong)<=10:#限制字典新增人数
            z=shu_ru_xing_ming()
            if z=="quit":#如果不想新增了可以控制退出
                  break
            if z not in jiao_wu_xi_tong:
                shu_ru_cheng_ji()
                jiao_wu_xi_tong[z]=b
            else:
                print("该学生已存在，不用新增")
                continue
    print(jiao_wu_xi_tong)

def xiu_gai():
    while 1:  
          z=shu_ru_xing_ming()
          if z=="quit":#如果不想修改了可以控制退出
                break
          if z in jiao_wu_xi_tong:
                    shu_ru_cheng_ji()
                    jiao_wu_xi_tong[z]=b
          else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
    print(jiao_wu_xi_tong)

def shan_chu():
       while 1:  
            z=shu_ru_xing_ming()
            if z=="quit":#如果不想删除了可以控制退出
                break 
            if z in jiao_wu_xi_tong:
                     jiao_wu_xi_tong.pop(z)
            else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)

def cha_xun():
       while 1:  
          z=shu_ru_xing_ming()
          if z=="quit":#如果不想删除了可以控制退出
                break 
          if z in jiao_wu_xi_tong:
                     print(f"学生姓名为{z},学生成绩为{jiao_wu_xi_tong[z]}")
          else:
                    print("输入未匹配上学生姓名，请重新输入")
                    continue
       print(jiao_wu_xi_tong)

while 1:
 h=input("请输入你想进行的操作：")#新增，删除，修改，查询
 if h==c[0]:
      xin_zeng()
 elif h==c[2]:
      xiu_gai()
 elif h==c[1]:
      shan_chu()
 elif h==c[3]:
       cha_xun()
 elif h==c[4]:
       break
 else:
       continue
       
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
      