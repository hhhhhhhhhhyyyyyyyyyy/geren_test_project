#文件操作
#open(文件路径，mode="你要干啥（读，写等）"，encoding="文件的编码格式")  打开文件
"""
1、文件路径分为相对路径和绝对路径
绝对路径：磁盘根目录开始查找，E:\Code\wen_jian.py(C,D,E,F,G盘都叫根目录)
相对路径：在python当中，以当前运行的py文件所在的文件夹作为基准，
           a、如果被搜索文件和当前运行的py文件在同一个文件夹内可以直接用./xx/xxxx.txt
xx/xxxx.txt
           b、如果不在当前文件夹内，可以使用../返回上一层文件夹进行查找


2、mode：r:代表read，只读,open的时候文件必须存在，不能写，最好的读取方式
         w：write，只写，W模式下，如果文件不存在，帮你创建新文件，不能创建新文件夹hgb/hellonihao.py
如果文件存在，会清空文件,w模式只能写不能读
         a：append，追加写,不能读，在文件末尾追加内容
         b：bytes，处理的是字节，字节的读或写，不单独用，一般和上面三种模式配合使用

3、encoding： 不论是读取还是写入文本都需要encode和decode操作，open会自动帮你完成这个过程，
但是得表明是指定的具体编码格式，utf-8或者gbk
"""
f=open("hellonihao.py",mode="w",encoding="utf-8")
f.write("谁？\n")
f.write("你是？\n")
f.write("你问我是谁？\n")
f.write("我还想问你是谁？\n")
import os
print(os.getcwd())#查找hellonihao的路径

f=open("hellonihao.py",mode="r",encoding="utf-8")
content=f.read()#可以一次性读取所有内容，但是内容偏大的话不太好
print(content)

for line in f:
    
    print(line)#按行读，一行一行被循环，逐行获取数据

#当文件不是文档而是图片时,模式带有b表示非文本文件
#比如图片，压缩包，excel，exe，MP3（音频），MP4（视频），不能写encoding参数
with open("piao_liang_zhao_pian.jpg",mode="rb")as f:
    contend=f.read()
print(content)
