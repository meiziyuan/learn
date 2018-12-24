##数据类型转换函数
#int()函数可以把其他数据类型转换为整数
a = int("124")
b = int(12.2)
c = float("12.15")
d = str(1.24)
e = bool(1)
f = bool("")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

#定义默认参数要牢记一点：默认参数必须指向不变对象！
def test(L=[]):
    L.append("END")
    return L

print(test())
print(test())

#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数

def test2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(test2(1,2,3,4,5,6,7,8,9,10))



#*lists表示把lists这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
lists = [1,2,3,4,5,6,7,8]
print(test2(*lists))