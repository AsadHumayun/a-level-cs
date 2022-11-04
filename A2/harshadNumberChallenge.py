#author: asadhumayun

'''
    Checks wether or not a float instance is an integer

    Returns:
        bool: True if the float instance is an integer, False otherwise
'''
def checkInteger(n: float) -> bool:
    _n = int(str(n).split('.')[1])

    if _n == 0:
        return True
    else:
        return False

'''
    Checks wether or not a number is a harshad number

    Returns:
        bool: True if the number is a harshad number, False otherwise
'''
def isHarshad(number: int) -> int or bool:
    digits = list(map(lambda x: int(x), list(str(number))))
    sum_ = sum(digits)
    res = float(number) / float(sum_)
    if checkInteger(res):
        return int(res)
    else:
        return False

# User's nth harshard number
target = int(input('enter ur nth number pls: '))

calcs = 0
harshards = []

for i in range(100000):
    calcs += 1
    if i == 0:
        continue
    if type(isHarshad(i)) is not bool:
        print(i, isHarshad(i), type(isHarshad(i)))
        harshards.append(i)
    else:
        pass

print(f'''
    {target}th harshard number is {harshards[target - 1]}

    Calculations: {calcs*3}
''')
