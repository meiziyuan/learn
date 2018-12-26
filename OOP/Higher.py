import logging
logging.basicConfig(level=logging.INFO)

##__slot__属性：限制当前类实例只能绑定的实例类型
class People(object):
    __slots__ = ('name','sex')  #用tuple定义允许绑定的属性名称
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    @property     ##把一个getter方法变成属性，只需要加上@property就可以了
    def name1(self):
        return self.name

    @name1.setter   ##@property本身又创建了另一个装饰器@name1.setter，负责把一个setter方法变成属性赋值
    def name1(self,value):
        self.name = value

    def __getattr__(self, item):
        print("处理没有找到属性的情况下")

    def __call__(self, *args, **kwargs):    ##直接对实例进行调用
        print("%s 被调用了"%self.name)

    pass

s = People('yuanmei','女')
s.name1 = 'mei'   ##调用setter方法，后面的赋值相当于传参
print(s.name1)
s()   ##直接对实例进行调用，调用的是__call__

def test():
    try:
        ss = People('alice','女')
        ss.age = 12
    except AttributeError as e:
        logging.exception(e)
        print(logging.info(e))
    finally:
        print("执行完毕")
test()

logging.info("test")
logging.warning("warning")