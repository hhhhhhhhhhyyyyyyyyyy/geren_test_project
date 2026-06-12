'''
递归函数：函数直接或间接调用函数本身称为递归函数，必须有出口
1、可遍历一个文件夹下面所有文件
2、快速排序等高级算法离不开递归
'''
#三以内数字累加和 3+2+1
def sums(numbers):
     if numbers==1:
          return 1
     return numbers+sums(numbers-1)         
b=sums(3)
print(b)