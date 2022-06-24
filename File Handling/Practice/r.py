with open("r.txt", "r") as f:
    content = f.read() # returns a string, eg "content of first line\ncontents of second line"
    # You can convert this into a list, by splitting with the \n character; this splits the txt file up, so each element in the array is the value of a line
    content = content.split("\n")
    # [ "line1", "line2", "line3", "line4" ... ]

    # Now you can do whatever you want on them, eg sorting them to collate a leaderboard or display them.