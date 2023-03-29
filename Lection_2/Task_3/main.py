result_list = []
for i in range(3):
    input_list = input("Enter the elements separated by space: ").split(" ")
    for elements in input_list:
        if input_list.count(elements) > 1:
            result_list.append(elements)
print(f"Duplicates: {set(result_list)}")


