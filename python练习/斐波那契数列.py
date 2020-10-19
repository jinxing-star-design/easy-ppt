##斐波那契数列
a = 0
b = 1
while True:
    c = a +b
    if c > 100:
        break
    print(c)
    a = b
    b = c
print()
##打印一百以内素数的个数
print(2)

count = 1
for i in range(3, 100, 2):
    for j in range(3, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:

        count += 1
print(count)


