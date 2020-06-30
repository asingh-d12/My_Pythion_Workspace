\n - new line
\t - tab(usually 4 characters worth in python)
\' or \" - to escape these characters in case a double qoute is in a double quote string, or a single quote is in single quote character

or simply use """, with triple quote no need to escape single or double quote

```
print("He's saying, \"He needs some time\"\nNo Time is to be given\tunderstood")
print('*' * 100)
print('He\'s saying, "He needs some time"\nNo Time is to be given\tunderstood')
print('*' * 100)
# or simple
print("""He's saying, He needs some time
No Time is to be given\tunderstood""")
print('*' * 100)
# Use \ at the end of the line in case of """ in order to make sure everything is in same line
print("""He's saying, He needs some time \
No Time is to be given\tunderstood""")
```

![[Pasted image.png]]

**Escaping backslash character**
So, if i want to print something like a file path in windows.
If we do something like this:
```
print('c:\Users\amrit\test.txt')
```

Here the issue is this, there are several escape characters like \U, \a and \t which are being recognised as such even though we don't want this to happen.

*How to resolve this?*
2 methods:
>1. Escape backslash character themselves
>2. Raw Strings

Let's see how this works:
```
# Escaping Backslash character
print('c:\\Users\\amrit\\test.txt')
# Raw String
print(r'c:\Users\amrit\test.txt')
```

![[Pasted image 1.png]]