import random


def let_random_string(length: int) -> str:
    result = ""
    for _ in range(length):
        char_type = random.choice(['digit', 'lower', 'upper'])
        if char_type == 'digit':
            result += chr(random.randint(48,57))
        elif char_type == 'lower':
            result += chr(random.randint(97, 122))
        else:
            result += chr(random.randint(65, 90))
    return result


print(let_random_string(100))
