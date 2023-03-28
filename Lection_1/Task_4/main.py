import math
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print("Equation example: ax^2+bx+c=0")
number_a = int(input("Please, enter the a argument: "))
number_b = int(input("Please, enter the b argument: "))
number_c = int(input("Please, enter the c argument: "))

discriminant = number_b * number_b - 4*number_a*number_c

if discriminant < 0:
    print("The equation has no roots")
if discriminant == 0:
    print(f"Result: x = {(-number_b+math.sqrt(discriminant))/(2*number_a)}")
if discriminant > 0:
    first_root = (-number_b+math.sqrt(discriminant))/(2*number_a)
    second_root = (-number_b-math.sqrt(discriminant))/(2*number_a)
    print(f"Result: x1 = {first_root}, x2 = {second_root}")





