express_company="海哥速运" #快递名称
base_weight=1  #首重重量
base_fee=12    #首重费用
extra_weight_price=6.1 #续重每公斤价格
print("请输入包裹总重量：")
total_weight=float(input()) #包裹总重量
total_fee=base_fee+(total_weight-base_weight)*extra_weight_price
#总费用等于首重费用加上续重部分总费用
print(f"快递公司名称为{express_company},总费用为：{total_fee}")
print("快递总费用为：%.2f" %total_fee)
#其实还是应该注意到用input（）函数输入什么都默认是字符串
#后期要做运算需要定义是整数型还是浮点型：total_weight=float(input())
#但是直接用数值赋值变量就不用担心这点，不用进行定义可直接运算