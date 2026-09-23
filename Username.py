first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = (input("Enter your birth year: "))

userName = first_name.lower() + "_" + last_name[:1].lower() + birth_year[2:]

print(userName)