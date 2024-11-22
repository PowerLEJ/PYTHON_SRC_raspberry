from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

print(output)

exit()


import os

os.system("ls -al")

exit()

import sys

sum = 0
for i in sys.argv:
    try:
        sum += int(i)
    except:
        pass

print(sum)
exit()

import math as m

print(m.sin(1))
print(m.cos(1))
print(m.tan(1))
print(m.floor(2.5))
print(m.ceil(2.5))

print("="*50)

from math import sin, cos, tan, floor, ceil

print(sin(1))
print(cos(1))
print(tan(1))
print(floor(2.5))
print(ceil(2.5))