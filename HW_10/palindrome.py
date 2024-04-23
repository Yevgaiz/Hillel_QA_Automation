string = str(input('Enter string: ')).strip().lower()

string_rev = string[::-1]


if string == string_rev:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

string_rev1 = ""
for i in range(len(string) - 1, -1, -1):
    string_rev1 += string[i]

if string == string_rev1:
    print("It's still a palindrome")
else:
    print("It's still not a palindrome")


