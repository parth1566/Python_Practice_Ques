marks = int(input("Enter your marks: "))

def grades(marks) :
    if marks < 0 or marks > 100:
        return "Invalid"
    elif marks >= 90:
        return "A"
    elif marks >= 75 and marks <= 89:
        return "B"
    elif marks >= 60 and marks <= 74:
        return "C"
    elif marks >= 40 and marks <= 59:
        return "D"
    else:
        return "Fail"

print(grades(marks))