fd = open("basic.txt", "w")

with fd as fff:
    fff.write("Hello Python Programming...!")
    # print("Hello Python Programming...!", file=fd)

fd.close


with open("basic.txt", "r") as fff:
    contents = fff.read()

print(contents)