# Try/Except
### These are a lot like those try/catch statements in JavaScript, but slightly less precise, in my opinion, not like that matters anyway.

##### Python - Try/Except

Example -
```py
try:
    print(x)
except:
    print("An error occurred!")
```

The JavaScript equivalent - 

```js
try {
    conosle.log(x)
} catch (err) {
    console.error(err) // prints to stderr
}
```

This is the basic structure of a try/except block; note you can also specify the type of exception in certain cases to return a more tailored error message - instead of "Something went wrong!" to something like "NameError: 'x' is not defined"

```py
try:
    print(x)
except NameError:
    print("Variable 'x' is not defined")
except: # execute this part of the code if any other exception occurs
    print("Whoops! Something else seems to have gone wrong!")
else:
    # do this if no exception has occurred
    print("Code successfully executed; no errors detected")
```

### `Raise` Keyword

The `raise` keyword can be used to throw a custom exception - in JavaScript, you could simply use `throw ErrorType(Message<string>)`. Python works in a similar way. See below:

```py
x = "hello"

if not type(x) is int:
  raise TypeError("Variable 'x' must be of type int")
```

If you do not know the exact type of exception that may be occurred, you can simply use raise Exception() as demonstrated below:

```py
x = "hello"

if not type(x) is int:
  raise Exception("Variable 'x' must be of type int")
```


**I do recommend that you read the W3Schools tutorial on this** - it is very useful and explains everything you'd need to know to truly accept this topic (haha get it accept sounds like except). You can find their tutorial [here](https://www.w3schools.com/python/python_try_except.asp).
