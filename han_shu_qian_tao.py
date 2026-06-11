'''函数嵌套'''
def print_line():
    print("-"*20)

def print_lines(number1):
    i=1
    while i<=number1:
        print_line()
        i+=1


def pr(number2):
    for i in range(number2):
        print_line()
        print_lines(2)
pr(2)

