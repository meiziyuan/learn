
##数据类型
#转义字符\  也可以在字符串前面加上r
print("I\'m ok")
print(r"I'm ok")

##IDE一行输入不完换行输入 直接在最后enter键即可
print("sss"
      "aaa"
      "bbb")

##输出文本中多行换行,采用格式'''   '''   在命令行中，>>>代替...。...是提示符的,不是代码一部分
print('''sss
aaa
bbb''')

print(r'''I'm ok \n hello''')

##布尔值可以用and or not
print(True or False)

##变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型。如果赋值时候类型不匹配，就会报错
##在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，给变量赋值就是把数据和变量关联起来。

##在计算机内存中，采用unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为utf-8编码
##用记事本编辑的时候，从文件读取的utf-8字符被转换为unicode字符到内存中，编辑完成后，保存的时候，再把unicode转换为utf-8保存到文件。
##浏览网页的时候，服务器会把动态生成的unicode内容转换为utf-8再传输给浏览器。
# 所以你看到很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页正是用的UTF-8编码。
##在python3中，字符串是以unicode编码，就是说python字符串支持多语言
print("你好，hello")
##ord()将字符转为对应的unicode编码（获取字符的整数表示），chr()把编码转换为对应的字符
print(ord("A"))
print(chr(66))

##python的字符串是str,在内存中，一个字符对应若干个字节，如果要在网络上传输，或者保存在磁盘上，就需要把str变为以字节为单位的bytes
##python中对bytes类型的数据用带b的前缀的单引号或双引号表示
a = 'ABC'
b = b'ABC'
##以unicode编码的字符串str可以通过encode()方法编码为指定的bytes，比如
print('ABC'.encode('ascii'))
print('ABC'.encode('utf-8'))
#print('中文'.encode('ascii'))

##在bytes中，无法显示为ASCII字符的字节，用\x##显示。
print('中'.encode('utf-8'))

##反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
b'\xe4\xb8\xad'.decode('utf-8',errors='ignore')
#计算str包含多少个字符，即字符长度，用len()；如果换成bytes，就计算字节数
print(len('ABC中文'))
print(len('中文'.encode('utf-8')))

lista = []


tuple=(1, 2, 3)

###test git

