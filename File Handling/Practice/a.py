with open("./a.txt", "a") as f:
    f.write("hi??")
    f.write("hii2?")
    # this just adds the param in the function to the current content of the file
    # the txt file already contained "ogc;" and in the end its contents read "ogc;hi??hii2?" -- it was NOT overwritten
    # love this method ngl