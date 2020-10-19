import copy

list1 = [1, 2, 3]
list3 = copy.deepcopy(list1)
print(id(list1))
print(id(list3))