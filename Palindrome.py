string = input("Enter text here: ").lower()
rev_string = string[:: -1]
print(rev_string)

if string == rev_string:
    print(True)
else:
    print(False)
