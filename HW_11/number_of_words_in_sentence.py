sentences = input(str("Enter the sentences: ")).strip()
print(len(sentences))
words_number = []
current_count = 0

for i in range(len(sentences)):
    if sentences[i] == " ":
        current_count += 1
    elif sentences[i] == "." or sentences[i] == "...":
        if i != len(sentences) - 1:
            current_count += 1
            words_number.append(current_count)
            current_count = 0

if current_count > 0:
    words_number.append(current_count)

if len(words_number) == 0 and len(sentences) != 0:
    words_number = [1]

print(words_number)

