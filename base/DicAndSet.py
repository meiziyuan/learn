
##python内置了字典，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
#dic = {"key":value}
dic1 = {"yuan": 25, "zhang": 26, "wang": 23, "li": 24}
#为什么dict查找速度这么快？ 给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。
#如果key不存在，就会报错；
# 1.判断key是否存在，in
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
if("wang" in dic1):
    print("key存在")

print(dic1.get("yang",-1))

#删除一个key，用pop(key)方法，对应的value也会从dic中删除
dic1.pop("zhang")
print(dic1)
#与list比较，dic的查找和插入速度极快，不会随着key的增加而变慢；占用大量内存，内存浪费多
#list相反，查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少
#dic是用空间换时间的一种方法。
#dic中的key是不可变对象

#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
# 这个通过key计算位置的算法称为哈希算法（Hash）。

#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
# 而list是可变的，就不能作为key：


#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
#对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

s1 = set([1,2,3,4])
print(s1)
s2 = set((1,2,3))
print(s2)
#s3 = set((1,[2,3]))  #会报错，因为tuple中的list是可变的，不符合set中的对key不可变对象的要求

