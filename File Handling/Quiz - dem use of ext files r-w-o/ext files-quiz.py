"file ops in py"
#database, configuration values, static/global configurations, list of data such as students' marks etc.
#a file contains a number of RECORDS, and a record contains a number of FIELDS. Fields refer to the GROUPS and records refer to the PERIODS.

from typing import List
from operator import itemgetter as ItemGetter # i cant stand the all lowercase "itemgetter"

id = str(input("Please enter your name (will be used to save your score in): "))
scr = 0
ls = []
with open("./quizq.txt", "r") as f:
    for l in f.readlines():
        #l = line[i]
        l = l.split(":")
        l[1] = l[1].split(";")
        q = l[0]
        ans = str(input("[Q]: " + q))
        if (not ans in l[1]):
            print("INCORRECT ANSWER. The correct answer(s) was/were: " + "\n".join(l[1]) + "\nCurrent score: [" + str(scr) + "]")
        else:
            scr += 1
            print("CORRECT ANSWER. The correct answer(s) was/were: " + "\n".join(l[1]) + "\nCurrent score: [" + str(scr) + "]")

print("Your total score is: " + str(scr) + ". Yuh.")

print("If you would like to change any of the questions, asnwers or add more acceptable answers to a said question, then please refer to the config file (./quizq.txt) in which you can edit such settings.")

import time
ms0 = int(round(time.time() * 1000)) # time#time() prolly returns in s
with open("./scrs.txt", "w") as f: 
    f.write(str(str(id) + ";" + str(scr)))
ms1 = int(round(time.time() * 1000)) # time#time() prolly returns in s
df = ms1 - ms0
print("Successfully updated scrs.txt in " + str(df) + " ms.")