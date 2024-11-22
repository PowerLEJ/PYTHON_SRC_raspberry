ary = [2, 3, 4, 5]

while True:
    a = input("정수를 입력해주세요: ")

    if a.isdigit():
        a = int(a)

        for i in ary: # for i in range(2, 6):
            if a % i == 0:
                print(f"{a}는 {i}로 나누어 떨어지는 숫자입니다.")
            else:
                print(f"{a}는 {i}로 나누어 떨어지는 숫자가 아닙니다.")

    elif a == "q" or a == "Q":
        break

exit()

import datetime

now = datetime.datetime.now()

print(type(now))

print(f"{now.year}년")

exit()

while True:

    a = input("a값을 입력 > ")

    if a.isdigit():

        a = int(a)

        if a > 10:
            print("a는 10보다 큽니다.")
        else:
            print("a는 10보다 작거나 같습니다.")

        break