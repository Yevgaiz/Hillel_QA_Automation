from typing import Callable
# import inspect


def custom_map(function: Callable, *iterables):
    # sig = inspect.signature(function)

    min_length = min(len(lst) for lst in iterables)

    trimmed_iterables = [lst[:min_length] for lst in iterables]
    # print(trimmed_iterables)
    # print(*trimmed_iterables)
    # result = [function(*args) for args in zip(*trimmed_iterables)]
    # print(list(sig.parameters))
    # print(trimmed_iterables)
    if function == sum:
        result = [function(args) for args in zip(*trimmed_iterables)]
        # print(list(sig.parameters))
        # print('if')
    else:
        result = [function(*args) for args in zip(*trimmed_iterables)]
        # print('else')
        # print(list(sig.parameters))

    return result


print(custom_map(sum, [1, 1, 2, 3], [3, 0, 5], [1, 2, 3, 2]))
print(custom_map(len, [[11, 2], (2, 4), [1, 3, 5, 7]]))
print(list(custom_map(lambda x, y: x + y, [1, 2, 3], [3, 5, 0])))
