lst = [3.5, 11, 1.23, 3, -1, -100]
result = []

for i in range(len(lst) - 1):
    result.append(lst[i])
    result.append((lst[i] + lst[i+1]) / 2)

result.append(lst[-1])
print("Result:", result)