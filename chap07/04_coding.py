from urllib import request

target = request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

file = open("output.png", "wb") # wb : 바이너리 형식
file.write(output)
file.close()



ch = b'A' # b'로 감싸져 있으므로 바이너리 데이터임
print(type(ch)) # <class 'bytes'>

ch = 'A'
print(type(ch)) # <class 'str'>