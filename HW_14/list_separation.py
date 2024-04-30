input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

divisible_by_3_not_5 = [num for num in input_list if num % 3 == 0 and num % 5 != 0]
divisible_by_5_not_3 = [num for num in input_list if num % 5 == 0 and num % 3 != 0]
divisible_by_3_and_5 = [num for num in input_list if num % 3 == 0 and num % 5 == 0]

print(divisible_by_3_not_5)
print(divisible_by_5_not_3)
print(divisible_by_3_and_5)