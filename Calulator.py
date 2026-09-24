a = int(input("Enter first num: "))
b = int(input("Enter second num: "))
op = input("Enter operator: ")

def calculator(a, b, op):
    if op == "+":
        return(a + b)
    elif op == "-":
        return(a - b)
    elif op == "*":
        return(a * b)
    elif op == "/":
        return(a / b)
    elif op == "%":
        return(a % b)
    elif op == "**":
        return(a ** b)
    elif op == "/":
        if b == 0:
                return "Cannot divide by zero"
        return a / b
    else:
        return("Invalid Operator")

print(calculator(a, b, op))