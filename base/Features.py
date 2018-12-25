
##切片：取指定索引范围的操作，比如取前三个元素  list1[n:m]表示取索引n到m-1的元素
#由于list支持倒数操作，切片也可倒数,比如取最后两个元素
list1 = [1, 2, 3, 4, 5]
print(list1[0:3])  ##取第一个到第三个元素
print(list1[-3:])  ##取倒数第3个到最后一个元素
print(list1[-1])   ##取最后一个元素

##list[n:m:k]  表示从索引n到m-1的元素中，每k个取一次
#先初始换一个序列0-99
list2 = list(range(100))
aa = list2[0:20:2]
print(aa)

bb = aa[:]   ##aa[:]将aa复制一份list，赋值与bb
print(bb)


##迭代for ... in ...
#python的for 循环不仅可以用在list、tuple上，还可以用在任何可迭代对象上
#默认情况下，for作用于dict上，迭代的是key,如果想要作用于value上，则需要for aa in d.values().
#如果是同时迭代key，value,则可以用 for key,value in d.items()

dicta = {"A": 1, "B": 2, "C": 3}
for key,value in dicta.items():
    print(key, ":", value)

for key in dicta:
    print(key)

for value in dicta.values():
    print(value)

##如何判断一个对象是不是可迭代的呢？使用collections模块IterIterable类型判断
from collections import Iterable
if (isinstance('abc',Iterable)):
    print(True)

##如果要实现对list实现类似Java那样下标的循环，python内置的enumrate函数可以把一个list变成索引-元素对
#这样就可以在for循环中同时迭代索引与元素本身了
for i,value in enumerate(['A', 'B', 'C']):
    print(i,value)


##列表生成式
list_1 = list(range(1,10)) ##生成一个从1-9的数字序列
print("list_1:", list_1)

##写生成列表式时，要把生成的元素放在前面，后面跟for循环，就可以把列表创建出来
list_2 = [x*x for x in range(1,10)]  ##生成一个1-9每个数的平方组成的列表
print("list_2:", list_2)

import os
print([d for d in os.listdir(".")])  #列出当前目录下所有的文件和目录名

#把一个list中的字符串都变成小写
L = ['Hello', 'World', 'Python']
print([s.lower() for s in L])