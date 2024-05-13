import os


def call_counter(path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not os.path.exists(path):
                with open(path, 'w') as f:
                    f.write("Function 'add' was called 0 times")

            with open(path, 'r') as f:
                count = int(f.read().split()[4])

            with open(path, 'w') as f:
                count += 1
                f.write(f"Function '{func.__name__}' was called {count} times\n")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@call_counter('data.txt')
def add(a, b):
    return a + b


print(add(4, 6))
print(add(3, 5))
