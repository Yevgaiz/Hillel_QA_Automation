sentences = input(str("Enter the sentences: ")).strip()

words_number = []
current_count = 0

for i in range(len(sentences)):
    if sentences[i] == " " or i == 1:
        current_count += 1
    elif sentences[i] == "." or sentences[i] == "...":
        if i != len(sentences) - 1:
            # current_count += 1
            words_number.append(current_count)
            current_count = 0

if current_count > 0:
    words_number.append(current_count)

# if len(words_number) == 0 and len(sentences) != 0:
#     words_number = [1]


# Variant №2
print(words_number)

sentence_list = sentences.split(".")
sentence_list.pop()

sentence_words = []

for sentence in sentence_list:
    words = sentence.split()
    sentence_words.append(len(words))

print(sentence_words)
