min_width = int(input('Enter minimal width: '))
max_width = int(input('Enter maximal width: '))

if min_width > max_width:
    print("Warning: Minimum width is greater than maximum width.")
    exit()

if (max_width - min_width) % 2 != 0:
    print('Difference between maximum and minimum widths is not a multiple of 2')
    exit()

spaces = (max_width - min_width) // 2
print(" " * spaces + "*" * min_width)

for i in range(min_width + 1, max_width - 1, 2):
    spaces = (max_width - i) // 2
    print(" " * spaces + "*", end="")
    if i > min_width:
        inner_spaces = i - 1
        print(" " * inner_spaces + "*", end="")
    print()


for i in range(max_width - 1, min_width - 1, -2):
    spaces = (max_width - i) // 2
    print(" " * spaces + "*", end="")
    if i > min_width:
        inner_spaces = i - 1
        print(" " * inner_spaces + "*", end="")
    print()

spaces = (max_width - min_width) // 2
print(" " * spaces + "*" * min_width)

