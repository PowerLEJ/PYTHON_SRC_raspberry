PI = 3.141592

def number_input():
    output = input("숫자 입력 > ")
    return float(output)

def get_circumferene(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius

if __name__ == "__main__":
    print("test1")
    radius = number_input()
    print(get_circumferene(radius))
    print(get_circle_area(radius))