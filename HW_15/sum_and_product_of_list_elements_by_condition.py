lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6

filtered_list = [num for num in lst if MIN <= num <= MAX]

if filtered_list:
    sum_ = sum(filtered_list)
    product = 1
    for num in filtered_list:
        product *= num
else:
    sum_ = None
    product = None

print("sum_ =", sum_, ", product =", product)