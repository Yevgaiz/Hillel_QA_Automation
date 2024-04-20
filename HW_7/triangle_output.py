size = int(input("Enter size of triangle: "))

for i in range(1, size + 1):
    for x in range(size - i):
        print(" ", end="")

    for y in range(i):
        print("*", end="")
    print('')