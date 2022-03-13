# Bython
Python with braces, symbol logical operators (&&, ||, !), increment and decrement operators (--, ++ suffix only), else if (not elif), uncapitalized true, false and none and it doesn't care about indentation.

Bython doesn't break when using dictionaries, lambdas or when putting braces in their own lines.
However please do indent your code correctly unlike this:
```python
variable = {
1: "one",
    2: "two",
  3: "three"
}

""" THIS WONT BREAK && || ! else if { } \" """
def say(message) {
   if (message) {
      print(message)
    }
else if (!message) {
return none
   }
}

# THIS WONT BREAK && || ! else if { }
def main()
{
    print(variable[int(input("? "))])
    print("THIS WONT BREAK: && || else if { } \" ")
    addition = lambda x, y: x + y
      return 0
}

if (__name__ == "__main__" && (true && !true || !none))
{
    main()
}
```

Which will get turned into this (use the -k  to keep the file because otherwise it will run it and then delete it):
```python
variable = {
    1: "one",
    2: "two",
    3: "three"
}

""" THIS WONT BREAK && || ! else if { } \" """
def say(message):
    if (message):
        print(message)
    elif (not message):
        return None

# THIS WONT BREAK && || ! else if { }
def main():
    print(variable[int(input("? "))])
    print("THIS WONT BREAK: && || else if { } \" ")
    addition = lambda x, y: x + y
    return 0

if (__name__ == "__main__" and (True and not True or not None)):
    main()
```
# Unimplemented features
## One liners ##
I did manage to get one liners working but it was a **very** ugly solution, so much so that I just scrapped it.

# Installation
Download bython.py

# Usage
The first file specified will be the one run, other ones will just be created.
You can't control the names of the output files, they will be the same as the files but with .py.
If -k isn't passed the files will be deleted afterwards.

To just create the files without running them pass -k, pass a non-existent file as the first argument and then just pass the rest of the files afterwards.
```
python bython.py <files> (-k to keep the file)
python bython.py none <files> -k (to create files without running them)
```
Examples:
```
python bython.py main.by library.by -k
python bython.py main.by
python bython.py none main.by -k
```
