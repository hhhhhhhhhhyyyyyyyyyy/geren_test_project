<<<<<<< HEAD
def shuru():
    a=int(input("请输入第1个数："))
    b=int(input("请输入第2个数："))
    c=int(input("请输入第3个数："))
    d=int(input("请输入第4个数："))
    h=[a,b,c,d]
    return h


def bi_jiao(a,b,c,d):
    t=[a,b,c,d]
    h=max(t)
    x=min(t)
    s=(h,x)
    return s
n=bi_jiao(*[1,2,3,4]) 
print(n) 

def bi_jiao2():
    t=shuru()
    h=max(t)
    x=min(t)
    s=(h,x)
    return s
m=bi_jiao2()
=======
def shuru():
    a=int(input("请输入第1个数："))
    b=int(input("请输入第2个数："))
    c=int(input("请输入第3个数："))
    d=int(input("请输入第4个数："))
    h=[a,b,c,d]
    return h


def bi_jiao(a,b,c,d):
    t=[a,b,c,d]
    h=max(t)
    x=min(t)
    s=(h,x)
    return s
n=bi_jiao(*[1,2,3,4]) 
print(n) 

def bi_jiao2():
    t=shuru()
    h=max(t)
    x=min(t)
    s=(h,x)
    return s
m=bi_jiao2()
>>>>>>> d0e2d9f23fb56140c0070b06bc0a6c3ea019b599
print(m)