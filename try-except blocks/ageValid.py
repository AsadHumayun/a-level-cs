agev = False
age = 0

try:
    age = int(input("Please enter your age: "))
except TypeError:
    print("Please enter your date of birth as an integer: ")
    age = int(input("Please enter your age: "))

print(age)