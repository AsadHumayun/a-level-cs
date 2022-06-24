students = int(input("Enter number of students :"))
books = int(input("Enter number of books :"))

lfo = students % books
bf = (books - lfo) / students

print(f"Number of books per student: {bf}\nNumber of books left over: {lfo}")