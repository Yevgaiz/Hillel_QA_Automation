def lst2dict(lst):
    result = {}

    for i in range(0, len(lst) - 1, 2):
        result[lst[i]] = lst[i + 1]

    return result


print(lst2dict([0, 1, 2, 3, 4, 5, 6]))
print(lst2dict(['a', 'A', 'b', 'B', 'c']))