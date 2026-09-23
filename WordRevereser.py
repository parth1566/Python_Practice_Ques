sentence = input("Please eneter your word(s): ")

word = sentence.split()
reversed_word = word[::-1]
result = " ".join(reversed_word)

print(result)