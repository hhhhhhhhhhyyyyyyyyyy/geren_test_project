<<<<<<< HEAD
'''
逐行读取原文件内容；
修改要调整的内容；
把内容写到新文件当中；
整个过程完毕之后，硬盘上会有两个文件；
删除原来的文件，把新文件的名字改成原来的文件的名字
with open("文件名","模式",encoding="utf-8")as 变量名：
   对文件的读写操作
能够正常自动关掉文件，不用写f.close()
'''
import os
with open("hellobig.py",mode="w",encoding="utf-8")as f1:
     f1.write("不能不爱我\n")
     f1.write("也不要恨我\n")
     f1.write("你爱不爱我\n")
     f1.write("你会爱我的对吗\n")
with open("hellobig.py",mode="r",encoding="utf-8")as f1,\
open("hellobig2.py",mode="w",encoding="utf-8")as f2: 
     for line in f1:
         print(line)#按行读，一行一行被循环，逐行获取数据
         if line.startswith("不"):#识别出第一个字是“不”的
              line="要"+line[1:]#将不替换成要
         f2.write(line)#将line的所有东西都放到f2里
os.remove("hellobig.py")
=======
'''
逐行读取原文件内容；
修改要调整的内容；
把内容写到新文件当中；
整个过程完毕之后，硬盘上会有两个文件；
删除原来的文件，把新文件的名字改成原来的文件的名字
with open("文件名","模式",encoding="utf-8")as 变量名：
   对文件的读写操作
能够正常自动关掉文件，不用写f.close()
'''
import os
with open("hellobig.py",mode="w",encoding="utf-8")as f1:
     f1.write("不能不爱我\n")
     f1.write("也不要恨我\n")
     f1.write("你爱不爱我\n")
     f1.write("你会爱我的对吗\n")
with open("hellobig.py",mode="r",encoding="utf-8")as f1,\
open("hellobig2.py",mode="w",encoding="utf-8")as f2: 
     for line in f1:
         print(line)#按行读，一行一行被循环，逐行获取数据
         if line.startswith("不"):#识别出第一个字是“不”的
              line="要"+line[1:]#将不替换成要
         f2.write(line)#将line的所有东西都放到f2里
os.remove("hellobig.py")
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
os.rename("hellobig2.py","hellobig.py")