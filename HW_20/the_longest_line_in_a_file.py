longest_line_length = 0
longest_line_content = ""

with open("My_file.txt", "r") as file:
    for line in file:
        line_length = 0
        for char in line:
            if char != '\n':
                line_length += 1
        if line_length >= longest_line_length:
            longest_line_length = line_length
            longest_line_content = line

print(" Longest line in the file:\n", longest_line_content.rstrip())
