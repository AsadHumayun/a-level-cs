from typing import List
from numpy import random

def gen(arr, maxLen):
    # generate random numbers
    while len(arr) != maxLen:
        n = random.randint(50)
        while n in arr: # ensure it's not already in the array
            n = random.randint(50)
        arr.append(n) # add to array
    return sorted(arr, reverse=False)

numbers = gen([], 6)
print("\n".join(map(lambda x: str(x), numbers)))

uin = input("Input your six numbers, separated by SPACES: ").split(" ")
matches = 0
print("You enetered: ", ",".join(uin))
srchd = []
for n in uin:
    if not n.isdigit(): continue # <- that fixed it lol, it was splitting the str instance incorrectly.
    n = int(n)
    if n in numbers and (n not in srchd):
        matches = matches + 1
        print("Match found:", str(n))
    srchd.append(n) # prevents dup matches

print(f"Number of matched numbers: {matches}")