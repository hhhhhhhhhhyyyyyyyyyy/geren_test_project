with open("hellonihao.py",mode="a",encoding="utf-8")as f1:
    f1.write("我讨厌你\n")
    f1.write("我还是喜欢你\n")
with open("hellonihao.py",mode="r",encoding="utf-8")as f2:
    content=f2.read()
print(content)
with open("hellonihao.py",mode="w",encoding="utf-8")as f3:
    list=["shdhih","wweuye","qajkdhk"]
    for item in list:
        f3.write(item)
        f3.write("\n")

