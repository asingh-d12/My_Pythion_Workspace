a_str = "Python is awesome!!"
# the syntax is something like this
# This is most basic one
print("1. Most Basic -> <string>[start:end:step] --> end char is not included, and by default if step is not specified it is considered 1"
      "This Basically means how much you step, instead of 1 step which is by default")
print(a_str[3:5:1])
print("This is an example of 2 step, as when with 1 step, the output was \"{}\"".format(a_str[0:8]))
print("With step = 2, the output is = \"{}\"".format(a_str[0:8:2]))
print(a_str[1:9:3])
print(a_str[10:17:2])

print()
print('*' * 50)
print("2. No Start Value Provided -> <string>[:end] and with a specified step")
print(a_str[:5:1])
print(a_str[:8:2])
print(a_str[:9:3])
print("Basically means start from 'start' or 0")

print()
print('*' * 50)

another_str = "9;223,372+036:854.775,807"
print("We are starting with this String, and our objective is to remove all different separators and make them same")
print(another_str)
print("We want all the , from the above string so, skip can be 4 and start can be 1")
separators = another_str[1::4]
print(another_str[1::4])

print()
print('*' * 50)

print("This is an experiment using both slicing and other things like join and comprehension(will come in future)")
print("1. First, let's print all the characters in this another_str using this list comprehension...")
print([a_char for a_char in another_str])

print("2. Now let's try adding if-else in this list comprehension, i.e. if char not present in separator then return as it is, else return ' '(this is in case of changing several different separators to ' ')")
print([a_char if a_char not in separators else " " for a_char in another_str])

print("3. Let's join and create a final string, join can be done on ''")
print(''.join([a_char if a_char not in separators else " " for a_char in another_str]))
