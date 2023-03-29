input_list = input("Enter elements separated by space: ").split(' ')
search_element = input("Enter the element, which count is needed ")
element_counter = 0
for elements in input_list:
    if elements == search_element:
        element_counter = element_counter + 1
print(f"Count of {search_element}: {element_counter}")


