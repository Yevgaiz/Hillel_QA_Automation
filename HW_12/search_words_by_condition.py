string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."

words = string.split()

for word in words:
    if word.lower().count('o') == 2:
        print(word.title(), end=' ')