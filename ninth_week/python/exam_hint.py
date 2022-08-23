message = input("\nEnter a string you want to swarp words: ")
print(message.split())
separate_words = message.split()

print("Separate words:")
for word in separate_words:
    print(word)

print("Modify each words")
print(len(separate_words))
for index in range(len(separate_words)):
    separate_words[index] = "G" + separate_words[index]
    print(separate_words[index])

print(separate_words)
print(" ".join(separate_words))
