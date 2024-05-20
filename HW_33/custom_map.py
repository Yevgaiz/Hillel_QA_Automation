from typing import Callable


def custom_map(function: Callable, *iterables):
    min_length = min(len(lst) for lst in iterables)

    trimmed_iterables = [lst[:min_length] for lst in iterables]

    result = [function(*args) for args in zip(*trimmed_iterables)]

    return result


print(custom_map(sum, [[1, 2, 3], [3, 5, 0, 5]]))
print(custom_map(lambda x, y: x + y, [1, 2, 3], [3, 5, 0]))
print(custom_map(len, [[], (2, 4), [1, 3, 5, 7]]))
