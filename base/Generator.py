
#一边循环一边计算的机制，称为生成器generator
#创建generator的第一种方法：将列表生成式中的[]改成(),就创建了一个generator
g = (x*x for x in range(1,10))
for x in g:
    print(x)

#创建generator的第二种方法：如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#斐波那契数列1,1,2,3,5,8,13...  计算第N个数是多少，并打印截止到该数的数列

def fib(N):
    n, a, b = 0, 0, 1
    list=[]
    while(n < N):
        list.append(b)
        a, b = b, a+b
        n = n+1
    print(list)
    print(list[-1])

fib(8)

#将普通函数变为generator的函数
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib1(N):
    n, a, b = 0, 0, 1
    list=[]
    while(n < N):
        list.append(b)
        yield b
        a, b = b, a+b
        n = n+1
    print(list)
    print(list[-1])

g = fib1(10)
while True:
    try:
        x = next(g)
        print("g:",x)
    except StopIteration as e:
        print(e.value)
        break

##杨辉三角
def Yanghui(N):
    list1 = [1]
    list2 = [1,1]
    i = 1
    while(i<= N):
        if(i == 1):
            #print(list1)
            yield list1
            i = i+1
        elif(i == 2):
            #print(list2)
            yield list2
            i = i+1
        else:
            list1 = list2
            list2 = []
            list2.append(1)
            j = 2
            while(j < i):
                list2.append(list1[j-1]+list1[j-2])
                j = j+1
            list2.append(1)
            #print(list2)
            yield list2
            i = i+1
g = Yanghui(10)

while True:
    try:
        x = next(g)
        print("g:",x)
    except StopIteration as e:
        print(e.value)
        break


