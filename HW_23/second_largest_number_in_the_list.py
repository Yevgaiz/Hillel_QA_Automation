def second_largest_number(nums):
    max_num = second_max_num = float('-inf')
    max_count = 0

    for num in nums:
        if num > max_num:
            second_max_num = max_num
            max_num = num
            max_count = 1
        elif num == max_num:
            max_count += 1
        elif num > second_max_num:
            second_max_num = num

    return second_max_num if second_max_num != float('-inf') and max_count != len(nums) else None


print(second_largest_number([22]))
print(second_largest_number([1, -10]))
print(second_largest_number([1, 3, 3, 2]))
print(second_largest_number([1, 3, 2, 4, 16, 25, 10, 5, 16.1]))