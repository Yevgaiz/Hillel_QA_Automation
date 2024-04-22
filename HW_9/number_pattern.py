num = int(input('Enter n: '))

for i in range(1, num + 1):
    for x in range(num - i):
        print("  ", end="")
    for y in range(1, i + 1):
        print(y, end=" ")
    for z in range(i - 1, 0, -1):
        print(z, end=" ")
    print("")