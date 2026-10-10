
from datetime import datetime
from utils import add, subtract, multiply

print("Name: Adnan Rosul")
print("Today's Date:", datetime.today().strftime("%Y-%m-%d"))

print("\nBasic Calculator")

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))

except ValueError:
    print("Error: Please enter valid numbers.")

except TypeError as e:
    print("Error:", e)
