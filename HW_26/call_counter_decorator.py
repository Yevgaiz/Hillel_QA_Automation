import os


# def call_counter(path):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if not os.path.exists(path):
#                 with open(path, 'w') as f:
#                     f.write("Function 'add' was called 0 times")

#             with open(path, 'r') as f:
#                 count = int(f.read().split()[4])
#
#             with open(path, 'w') as f:
#                 count += 1
#                 f.write(f"Function '{func.__name__}' was called {count} times\n")
#
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator


def call_counter(path):
    def decorator(func):
        def wrapper(*args, **kwargs):

            if os.path.exists(path):
                with open(path, 'r') as f:
                    lines = f.readlines()
                    counts = {}
                    for line in lines:
                        func_name, count_str = line.strip().split(" was called ")
                        counts[func_name[10:-1]] = int(count_str[:-6])
            else:
                counts = {}

            counts[func.__name__] = counts.get(func.__name__, 0) + 1

            with open(path, 'w') as f:
                for func_name, count in counts.items():
                    f.write(f"Function '{func_name}' was called {count} times.\n")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@call_counter('data.txt')
def add(a, b):
    return a + b


@call_counter('data.txt')
def divide(a, b):
    return a / b


print(divide(12, 2))
print(add(4, 6))
print(add(3, 5))
