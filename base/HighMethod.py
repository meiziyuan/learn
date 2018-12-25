#函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
f = abs
print(f(-1))
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

#map()  and reduce()
#map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#通过list()函数让它把整个序列都计算出来并返回一个list。
def f(x):
    return x*x
iter = map(f,[1,2,3,4,5,6])
print(list(iter))

list1 =[1,2,3,4,5]
print(list(map(str,list1)))  #将list1中的每个元素转为字符串，生成一个Interator，通过list()生成一个list列表



##reduce:reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x,y):
    return x+y

reduce(add,[1,3,5,7,9])

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
def normalize(name):
    return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#和map()类似，filter()也接收一个函数和一个序列。【对序列中的元素按照某个方法进行过滤】
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#把一个序列中的空字符串丢掉
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A',' ','MK',None])))
#filter()的作用是从一个序列中筛出符合条件的元素。
# 由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。


##sorted()函数可以对list进行排序
sorted([36, 5, -12, 9, -21])  ##[-21, -12, 5, 9, 36]
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
sorted([36, 5, -12, 9, -21],key=abs) #[5, 9, -12, -21, 36]

#默认情况下，对字符串排序，是按照asicc的大小比较的
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)) #['about', 'bob', 'Credit', 'Zoo']
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))  #['Zoo', 'Credit', 'bob', 'about']

#用sorted()对上述列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name) ##对L中的每一个元素使用by_name方法，然后将作用之后的元素进行排序
print(L2)
