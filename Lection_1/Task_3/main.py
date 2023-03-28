print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
number_a = float(input("Please, enter the first number: "))
number_b = float(input("Please, enter the second number: "))
print("Operations list:\n plus(+) \n minus(-) \n multiply(*) \n squaring(^)")
operation = input("Choose operation from list: ")

match operation:
    case "plus" | "+":
        result = number_a + number_b
    case "minus" | "-":
        result = number_a - number_b
    case "multiply" | "*":
        result = number_a * number_b
    case "divide" | "/":
        result = number_a / number_b
    case "squaring" | "^":
        result = number_a * number_a, number_b * number_b

print(f"Result: {result}")
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

