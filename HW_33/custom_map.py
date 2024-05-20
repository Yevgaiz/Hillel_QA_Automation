from typing import Callable

def custom_map(function: Callable, *iterables):
    min_length = min(len(lst) for lst in iterables)

    trimmed_iterables = [lst[:min_length] for lst in iterables]

    if function == sum:
        result = [function(args) for args in zip(*trimmed_iterables)]
    else:
        result = [function(*args) for args in zip(*trimmed_iterables)]

    return result


print(custom_map(sum, [1, 1, 2, 3], [3, 0, 5], [1, 2, 3, 2]))
print(custom_map(len, [[11, 2], (2, 4), [1, 3, 5, 7]]))
print(list(custom_map(lambda x, y: x + y, [1, 2, 3], [3, 5, 0])))
