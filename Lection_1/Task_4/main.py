import math
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print("Equation example: ax^2+bx+c=0")
number_a = int(input("Please, enter the a argument: "))
number_b = int(input("Please, enter the b argument: "))
number_c = int(input("Please, enter the c argument: "))

discriminant = number_b * number_b - 4*number_a*number_c


def solution():
    if discriminant < 0:
        print("The equation has no roots")
    if discriminant == 0:
        print(f"Result: x = {((-number_b*number_b)+math.sqrt(discriminant))/(2*number_a)}")
    if discriminant > 0:
        first_root = (-(number_b*number_b)+math.sqrt(discriminant))/(2*number_a)
        second_root = (-(number_b*number_b)-math.sqrt(discriminant))/(2*number_a)
        print(f"Result: x1 = {first_root}, x2 = {second_root}")


if number_b == 0 | number_c == 0:
    print("Result: x=0")
elif number_b == 0:
    if number_c/number_a >= 0:
        x1 = math.sqrt(number_c/number_a)
        x2 = -math.sqrt(number_c/number_a)
        print(f"Result: x1 = {x1}, x2 = {x2}")
    else:
        print("The equation has no roots")
elif number_c == 0:
    print(f"Result: x1 = 0, x2 = {-number_b/number_a}")
else:
    solution()




