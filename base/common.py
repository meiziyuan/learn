import os
###dir方法,dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
# 如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
a = 123
def test():
    print("345")
print(dir())

##dir([object])   object -- 对象、变量、类型。返回模块的属性列表。
dir()  ##获得当前模块的属性列表
print(dir([]))  ##查看列表的方法
print(dir(str)) ##查看字符串的方法


##如何获取当前路径
#当前路径用“.”表示，在用os.path.abspath()将其转换为绝对路径
print(os.path.abspath("."))

##如何获取当前模块的文件名，可以用过特殊变量获取__file__
print(__file__)

###如何获取命令行参数
#argv的第一个元素永远是命令行执行的.py文件名。
import sys
print(sys.argv)

##如何获取python命令的可执行文件路径
print(sys.executable)
