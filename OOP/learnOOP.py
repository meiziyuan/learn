

#由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

class Student(object):
    mateclass = 0   #类属性
#特殊方法“__init__”前后分别有两个下划线！！！
    def __init__(self,name,score,sex="女"):
        self.name = name
        self.score = score
        self.__sex=sex
        Student.mateclass = Student.mateclass+1   ##每创建一个实例，边+1
    def get_score(self):
        return self.score
    def get_sex(self):
        return self.__sex
    pass

bart = Student('alice',35,"男")
print(bart.get_sex())
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身.
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数.
# 但self不需要传，Python解释器自己会把实例变量传进去

#在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
# 除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
#类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

#方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
#通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

##判断class的类型，优先考虑isinstance()函数

s = Student('mei',98,'女')

if(isinstance(s,Student)):
    print("Yes")
##如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir(Student))

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
#下面两种方法是等价的
print("str".__len__())
print(len("str"))
s.mateclass = s.mateclass+1
s1 = Student('aaa',23)
print(s.mateclass)
print(s1.mateclass)