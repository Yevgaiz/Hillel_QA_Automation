def linearize_list(lst):
    linearized = []
    for item in lst:
        if isinstance(item, list):
            linearized.extend(linearize_list(item))
        else:
            linearized.append(item)
    return linearized


nested_list = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
linearize = linearize_list(nested_list)
print(linearize)
