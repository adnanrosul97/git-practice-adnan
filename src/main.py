from datetime import datetime
from utils import add, subtract

print("Name: Adnan Rosul")
print("Today's Date:", datetime.today().strftime("%Y-%m-%d"))

print("\nBasic Calculator")

a = 10
b = 5

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))