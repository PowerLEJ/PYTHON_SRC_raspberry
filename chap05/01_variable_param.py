# def print_n_times(n, *values):
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values: # values를 리스트처럼 활용
            print(value)
        print()

# print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

print("="*50)

def cal(a, b):
    return a+b, a-b

add, sub = cal(10, 20)
print(add, sub)

add = cal(10, 20)[0]
sub = cal(10, 20)[1]
print(add, sub)

print("test", "hello", sep="\t", end="\t")
print("Hello")