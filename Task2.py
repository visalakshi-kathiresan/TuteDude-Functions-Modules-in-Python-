import math
number = float(input("Enter a number: "))

if number >= 0:
    square_root = math.sqrt(number)
    print("Square root:", square_root)
else:
    print("square root is not defined for negative numbers.")

if number > 0:
    natural_log = math.log(number)
    print("Logarithm:", natural_log)
else:
    print("logarithm is only defined for positive numbers.")

sine = math.sin(number)
print("Sine:", sine)
