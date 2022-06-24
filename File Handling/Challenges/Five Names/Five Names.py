'''
Write a program which asks the user for 5 names; 
each time the name will be saved to a text file.  The program should output the contents of the file
after the names have been entered.
'''

with open("./5Names.txt", "w") as f:
    names = []
    while len(names) < 5:
        name = str(input("Please enter your name: "))
        names.append(name)
    f.write("\n".join(names))