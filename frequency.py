def list_to_dict_with_frequencies(numbers_list):
    frequency_dict = {}
    for number in numbers_list:
        frequency_dict[number] = frequency_dict.get(number, 0) + 1
    return frequency_dict

user_input_numbers = []
for i in range(10):
    user_input = int(input(f"Enter integer {i+1}: "))
    user_input_numbers.append(user_input)


result_dict = list_to_dict_with_frequencies(user_input_numbers)

print("Original List of Numbers:", user_input_numbers)
print("Dictionary with Frequencies:", result_dict)