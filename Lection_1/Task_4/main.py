import math
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print("Equation example: ax^2+bx+c=0")
print("Enter the equation arguments:")
number_a = int(input("a = "))
number_b = int(input("b = "))
number_c = int(input("c = "))

discriminant = number_b * number_b - 4*number_a*number_c

if discriminant < 0:
    print("The equation has no roots")
if discriminant == 0:
    print(f"Result: x = {(-number_b+math.sqrt(discriminant))/(2*number_a)}")
if discriminant > 0:
    first_root = (-number_b+math.sqrt(discriminant))/(2*number_a)
    second_root = (-number_b-math.sqrt(discriminant))/(2*number_a)
    print(f"Result: x1 = {first_root}, x2 = {second_root}")





