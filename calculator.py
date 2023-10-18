#Prompt for user input

a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

#Perform Operations

print("Sum: {} + {} = {}".format(a, b, a+b))
print("Difference: {} - {} = {}".format(a,b, a-b))
print("Multiplication: {} * {} = {}".format(a,b, a*b))
print("Division: {} / {} = {}".format(a,b, a/b))
print("Power: {} ** {} = {}".format(a,b, a**b))
print("Division with remainder: {} / {} = {} Remainder: {}".format(a,b, a//b, a%b))