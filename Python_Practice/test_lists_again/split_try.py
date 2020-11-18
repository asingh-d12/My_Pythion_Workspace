numbers = "9, 223: 125   1254, 487,21,  ,458,1202::78;45"
separators = [x for x in numbers if not x.isnumeric()]
print(separators)

values = ''.join([x if x not in separators else ' ' for x in numbers]).split()
print(values)
