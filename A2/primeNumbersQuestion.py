# author: asadhumayun

import os, sys

def isPrime(number: int) -> bool:
    prime = True
    
    for i in range(number):
        if i == 0 or i == 1 or i == number:
            continue

        if float(number / i).is_integer():
            prime = False

    return prime

def displayNumberStats(number: int) -> None:
    if number <= 1:
        print('Number must be > 1')
    else:
        if isPrime(number):
            print('is prime')
        else:
            print('is not prime')

    return None


while True:
    inpt = input('Enter a number. If you would like to exit the program, just press enter.')
    if inpt:
        displayNumberStats(int(inpt))
    else:
        sys.exit(0)
