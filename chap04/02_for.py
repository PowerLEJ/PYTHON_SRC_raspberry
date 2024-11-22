list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for i in list_of_list:
    for j in i:
        print(j)

print("="*50)

a = [1,2,3,4]
a.append(5)
a.extend([6,7])
b = [a, a]
print(b)
b = [*a, *a]
print(b)