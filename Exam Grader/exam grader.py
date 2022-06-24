import sys

scr = int(input("Please enter student's score, out of 100: ")) # 100 is the cap

if scr > 100:
    print("Sorry but the maximum number of marks is 100.")
    sys.exit()

grds = []

# I was doing
# with f as open("./grds.txt"):
# slightly incorrect lol
with open("./grds.txt") as f:
    l = f.readline()
    l = l.split(";")
    for el in l: # el refers to element, not l, lol
        grds.append(el.split(":"))
    f.close()

for g in grds:
    if eval(g[0].split(":")[0].replace("x", str(scr))) == True:
        print(f"Your grade for score ({scr}) is {g[1]}")
        sys.exit()
    else: 
        continue