data = "Hello\\\\World"
print(data)
if '\\' in data:
    pos = data.find('\\')
    print(pos)
    data = data[0:pos] + data[pos+1:]
print(data)
