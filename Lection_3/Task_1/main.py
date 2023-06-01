def calculation(operation, first_num, second_num):
    match operation:
        case "+":
            return first_num + second_num
        case "-":
            return first_num - second_num
        case "*":
            return first_num * second_num
        case "/":
            return first_num / second_num
        case "^":
            return first_num ** second_num


def main():
    print("Enter 2 numbers")
    first_num = float(input("First number: "))
    second_num = float(input("Second number: "))
    operation = input(
        "Choose the operation from list:\n [1] Plus\n [2] Minus\n [3] Multiply\n [4] Divide\n [5] Degree\n ")
    match operation:
        case "1" | "Plus":
            print(calculation("+", first_num, second_num))
        case "2" | "Minus":
            print(calculation("-", first_num, second_num))
        case "3" | "Multiply":
            print(calculation("*", first_num, second_num))
        case "4" | "Divide":
            print(calculation("/", first_num, second_num))
        case "5" | "Degree":
            print(calculation("^", first_num, second_num))


main()