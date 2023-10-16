#%
my_list = [1,2,3,4,5]
print(my_list)
x = my_list[1]
print(x)

#%
print(my_list[:3])
print(my_list[::2])
print(my_list[-2:])
print(my_list[::-1])

#%
my_list2 = [x*2 for x in my_list]
print(my_list2)

#%
list2 = []
list2.append(1)
list2.append(2)
list2.append(3)

print(list2)

#%
list2 = [1,2,3]
list2.pop()
print(list2)

list2.pop(0)
print(list2)

#%
help(type)
print(type(list))
help(list)
