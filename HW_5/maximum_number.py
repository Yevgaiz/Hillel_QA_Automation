num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

max_num = num1

if num2 > max_num:
    max_num = num2

if num3 > max_num:
    max_num = num3

print("The maximum number is:", max_num)