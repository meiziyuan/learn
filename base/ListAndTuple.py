###学习python中的tuple和list
##查看内置函数的方法

matelist = ['123', '456', 789]
##用len()函数可以获得list元素的个数
print("list长度：", len(matelist))
##最后一个元素的索引是len(classmates) - 1;;;;要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(matelist[-1])
##list是一个可变的有序表，可直接在最后面添加元素
matelist.append("abc")
###也可以将元素插在指定位置，比如插在倒数第二个元素的前面
matelist.insert(-2,"bnm")
print(matelist)
###在第三个元素前面插入
matelist.insert(2, "sdf")
print(matelist)
###要删除末尾元素
matelist.pop()
print(matelist)
##删除指定位置的元素
matelist.pop(2)
print(matelist)


##tuple一旦初始化就不能修改,因此它没有append、insert、pop等方法，只能获取查看，不能修改，不能赋值为另外的元素

##tuple所谓的不变，指的是tuple所有的元素，指向永远不变


