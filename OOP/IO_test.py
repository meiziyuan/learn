#IO编程IO在计算机中指Input/Output，也就是输入和输出。
# 由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口

#同步和异步的区别就在于是否等待IO执行的结果。如果干巴巴等着操作执行完，再进行其他事，就是同步。
#如果是在干完这件事，等待过程中，去做其他事，就是异步。
#使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。
# 想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。
# 如果是服务员跑过来找到你，这是回调模式；
# 如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。
import logging

try:
    f = open("../testfiles/test",'rb') ##以读文件的模式打开一个文件对象，使用内置的open()函数
    print(f.read())  ##调用read()方法可以一次性读取文件的全部内容，python把文件读取到内存中，是用一个str表示。
except IOError as e:
    logging.info(e)
finally:
    f.close()  #文件使用完了必须关闭，否则占用系统资源。

#上面是一个完整的文件操作异常检查，但是每次操作文件这样写，很繁琐。python引入with语句自动帮我们调用close()方法
with open("../testfiles/test",'r') as f1:
    print(f1.read())
    print(f1.read(3))
    print(f1.readline())
    print(f1.readlines())

with open("../testfiles/test",'w') as ww:
    ww.write("test2")

with open("../testfiles/test",'a') as ww:
    ww.write("test1")

#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
# 所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。


##StringIO:在内存中读写str，要把str写入StringIO，需要先创建一个StringIO，然后像文件一样写入
from io import StringIO
f = StringIO()
f.write("hello")
print(f.getvalue())  #getvalue()方法用于写入后的str

f1 = StringIO('你好')
print(f1.read())

#StringIO操作的是str,如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO
bb = BytesIO()
bb.write("中文".encode('utf-8'))   #写入的不是str，而是经过UTF-8编码的bytes。
print(bb.getvalue())
print(bb.getvalue().decode('utf-8'))

#或者如下：
bw = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(bw.read().decode('utf-8'))


##文件目录操作
import os
print(os.name)   ##如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#print(os.uname())  ##在window上不提供

##在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)

#要获取某个环境变量的值，可以调用os.environ.get('key')
print(os.environ.get('ANDROID_HOME'))
print(os.environ.get('PATH'))

#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
#查看当前目录的绝对路径
print(os.path.abspath("."))



##我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
import pickle
d = dict(name= 'yuan',age = 20)
pickle.dumps(d)
f = open("../testfiles/test",'wb')
pickle.dump(d,f)
f.close()

import json
json_str = '{"name":"yuan" , "age":25 }'
print(json.loads(json_str))  ##将str转换为dict类型
print(type(json.loads(json_str)))

print(json.dumps(d))
print(type(json.dumps(d))) ##将dict转换为一个str类型