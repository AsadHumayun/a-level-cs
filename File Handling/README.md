# Some useful tips

## Methods

`<File>` represents a File instance, attained by executing something like `myvar = open(...)` or using a `with open(...) as ...` block.

`<File>.read(<chars>)` - reads the first number of `<chars>` characters from the text file [R]
`<File>.readline(<lnNumber>)` - reads the `lnNumber` line of the file, if no argument is provided then the first line will be returned [R]
`<File>.write(<String>)` - write a string to the file, action depends on the current mode that is selected; sometimes it will completely overwrite the filer and sometimes it will simoply append text to it. [N/A]
`<File>.close()` - close the file [N/A]

**For more functions and methods, visit the [Python Documentations](https://docs.python.org/3/library/functions.html#open).**

### Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'U'	universal newline mode (deprecated)


You use these when opening files, so something like `F = open("file", "mode<one of the characters listed above>")`

Also note; you do NOT need to close your file if it's in a Python with block, since when Python exists this block, the file is automatically closed for you. An example of a with block is displayed below. 

```py
# manual close 
with open("./filename.txt", "r") as f: 
    print(f.read())
    f.close()
```

will work just as well as...

```py 
with open("./filename.txt", "r") as f: 
    print(f.read())
```

It's still good practice to include the `<File>.close()` just so you get into the habit and so you don't mess up aand forget to in the exam.