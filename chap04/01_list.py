list_a = [0, 1, 2, 3, 4, 5]

del list_a[1]
print(list_a)

list_a.pop(2)
print(list_a)

del list_a[1:3]
print(list_a)

list_a.remove(5)
print(list_a)

list_a.clear()
print(list_a)

exit()


print(type(list_a))
print(list_a)

list_a.append(4)
print(list_a)

list_a += [5]
print(list_a)

list_a.insert(0, 10)
print(list_a)