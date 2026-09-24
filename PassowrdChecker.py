def is_strong_password(password):
    has_digit = False
    has_upper = False
    has_special = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
        if char in "!@#$%":
            has_special = True

    return len(password) >= 8 and has_digit and has_upper and has_special

print(is_strong_password("parth123"))
print(is_strong_password("PARTH123"))
print(is_strong_password("Parth@123"))
print(is_strong_password("P@1"))