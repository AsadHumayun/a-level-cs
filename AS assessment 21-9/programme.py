import sys

username = str(input("Pleas enter your username: "))
while len(username.split("@")) != 2:
	print("You have entered an invalid email address, please try again.")
	username = str(input("Please enter your username (must be formatted as a valid email address): "))

password = str(input("Please enter your password: "))
t = 3
cps = "Tues0921!"
while t != -1:
	if t <= 0:
		print("Sorry, you have [0] attempts remaining.")
		sys.exit() # ensures programme dies after person has lost all 3 attempts
	if password == cps:
		print("Correct password!")
		break; # break out of loop
		t = -1 # ensures loop doesn’t run again by invalidating condition
	else:
		t = t - 1
		password = str(input("Please enter your password; you have [" + str(t) + "] attempts remaining after this attempt!"))

numberIn = int(input("Enter a positive whole number: "))
if numberIn <= 0:
	print("You did not enter a positive whole number!")
	sys.exit()

numberOut = 0
count = 0

while numberIn > 0:
	count += 1 
	partValue = numberIn % 2
	numberIn //= 2
	print(f"numberIn={numberIn}\npartValue={partValue} on iteration #{count} (just above for loop)")
	for i in range(0, count-1):
		partValue = partValue * 10 
	numberOut = numberOut + partValue
	print(f"count={count}\nnumberOut={numberOut}\nnumberIn={numberIn}\n")
print("The result is: " + str(numberOut))