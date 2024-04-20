height = int(input("Enter height of rectangle: "))
width = int(input("Enter width of rectangle: "))
symbol = input("Enter symbol to build rectangle with: ")

for string in range(height):
    for column in range(width):
        print(symbol, end='')
    print('')