#1 算数运算符
print(10+3)
print(10/3) #除不尽，结果带小数
print(10//3)#只保留整数部分
print(10 % 3)#取模 取余数

#比较运算符 > < >= <= == = !=
print(10>3)#结果是真或假

#赋值运算符
#增量赋值
age = 18
age = age +1
age += 1
print(age)

#链式取值
z=y=x=10
print(x, y, z)
print(id(x), id(y), id(z))
print(id(x),id(y), id(z))

#交叉赋值
m = 10
n = 20
temp = m
m = n
n = temp#交换两个值
#简便方法
m, n = n, m #原理相同，python简编的交叉赋值。

#解压赋值
#把五个月的工资取出来分别赋值给不同的变量名
#以下就是解压赋值，即从列表中解放出来
salaries = [111, 222, 333, 444, 555]
#mon0, mon1, mon2, mon3 = salaries#必须一一对应少一个多一个都不行
#还可以怎么做？
#mon1=salaries[0]
#mon2=salaries[1]
#mon3=salaries[3]
#只想取前三个值怎么办l
x,y,z,*aaa=salaries[111,222,333,444,555] #*aaa接收到剩余的没有对应关系的值存成列表并赋值
print(x, y, z)

print("please input your name:")


#逻辑运算符
#区别not and or
