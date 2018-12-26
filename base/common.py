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

##获取当前目录下的文件及目录名
print(os.listdir("."))


##如何获取当前模块的文件名，可以用过特殊变量获取__file__
print(__file__)

###如何获取命令行参数
#argv的第一个元素永远是命令行执行的.py文件名。
import sys
print(sys.argv)

##如何获取python命令的可执行文件路径
print(sys.executable)

##获取键盘输入input()
#input()返回的是str,int()可以将str将纯数字的字符串转换为整数
str = input("请输入：")
aa = int(str)
print(aa > 0)

##range()可以生成一个整数序列，再通过list函数转换为list
#range(5)生成的序列是从0开始小于5的整数：range(1,5)生成的序列是从1开始小于5的整数
print(list(range(5)))   #[0,1,2,3,4]
print(list(range(1,5)))  #[1,2,3,4]

##type()返回对应的class类型
print(type(12))

