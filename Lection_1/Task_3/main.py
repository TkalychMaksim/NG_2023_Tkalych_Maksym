print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
number_a = float(input("Please, enter the first number: "))
number_b = float(input("Please, enter the second number: "))
print("Operations list:\n plus(+) \n minus(-) \n multiply(*) \n squaring(^)")
operation = input("Choose operation from list: ")
match operation:
    case "plus" | "+":
        print(f"Result: {number_a + number_b}")
    case "minus" | "-":
        print(f"Result: {number_a - number_b}")
    case "multiply" | "*":
        print(f"Result: {number_a * number_b}")
    case "divide" | "/":
        print(f"Result: {number_a / number_b}")
    case "squaring" | "^":
        print(f"Result: {number_a}^2 = {number_a * number_a} \n {number_b}^2 = {number_b * number_b}")
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

