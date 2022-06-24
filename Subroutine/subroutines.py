# simple function, outputs numeric input
def smplfnc(lol: int):
    print(str(lol))

smplfnc(99) # --> "99" in sys.stdout

import sys, string as String
table = str.maketrans("", "", String.ascii_lowercase) #<source: stackoverflow>

# @returns [bool, errMessage]
# @param psw <str> password to be checked
def verify(psw: str):
    if type(psw) != str:
        psw = str(psw)
    else:
        if (len(psw) < 6 or len(psw) > 8) or (psw.translate(None, String.ascii_lowercase)):
            return [False, "Password must be between 6 and 8 chars, and have at least 2 capital letters.", verify]
        else:
            rntr = str(input("Please re-enter your password: "))
            if rntr != psw:
                return [False, "The password entered did not match the first password entry. The process has been restarted.", verify];
            else:
                return [True, "Password change successful.", sys.exit]

ps = str(input("Please enter a password [must be between 6 and 8 chars otherwise bad things will happen]: "))

d = verify(ps)
if d[0] == True:
    print(d[1])
    d[2]()

while d[0] != True: 
    print(d[1])
    ps0 = str(input("Please enter a password [must be between 6 and 8 chars otherwise bad things will happen]: "))
    verify(ps0)