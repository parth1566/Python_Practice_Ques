rate = float(input("Enter Rate of return: "))
initial = int(input("Enter the initial investment: "))
cf1 = int(input("Enter the 1st year annual cash flow: "))
cf2 = int(input("Enter the 2nd year annual cash flow: "))
cf3 = int(input("Enter the 3rd year annual cash flow: "))

def npv(rate, initial, cf1, cf2, cf3) :
    cf1/(1 + rate) + cf2/(1 + rate)**2 + cf3/(1 + rate)**3 - initial
    return round(cf1/(1 + rate) + cf2/(1 + rate)**2 + cf3/(1 + rate)**3 - initial, 2)

print(npv(rate, initial, cf1, cf2, cf3))