#百分号
#按照百分号一一对应
res = "my name is %s my age is %s" %('egon',"18")
print(res)

#str.format
res = "my name is {0}, my age is {1}".format('hayden', 18)
print(res)

#用format打破位置的限制
res = "my name is {name}, my age is {age}".format(age=18, name='egon')
#一一对应
print(res)
#如果要输出{name}怎么办
res = 'name {{{x}} age {y}}'.format(x='dd', y=18)
print(res)
#两个{}代表一个



#f
x = input('your name')
y = input('your age:')
res = f'my name is {x} my age is {y}'
print(res)
#速度上有差异，%最慢，format快，推荐使用format

