a = 65534   # FF FE
b = 65535   # FF FF
c = 65536
d = 2998302

with open("binary2", 'wb') as bin_file:
    # to_bytes take 2 required arguments
    # 1. number of bytes - or how many bytes will the number take
    # 2. orientation - big endian or little endian
    # big endian - most significant byte first
    # little endian - least significant byte first
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'big'))
    bin_file.write(d.to_bytes(4, 'little'))

with open("binary2", 'rb') as bin_file_2:
    # We can read like this
    e = bin_file_2.read(2)
    int_e = int.from_bytes(e, 'big')
    print(int_e)

    # or we can also read like this
    f = int.from_bytes(bin_file_2.read(2), 'big')
    print(f)

    g = int.from_bytes(bin_file_2.read(4), 'big')
    print(g)

    h = int.from_bytes(bin_file_2.read(4), 'big')
    print(h)

    i = int.from_bytes(bin_file_2.read(4), 'little')
    print(i)
