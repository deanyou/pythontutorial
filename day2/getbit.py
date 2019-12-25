#!/usr/bin/python3

# 取第n位
def getbit(n):
    a = 0xf7
    b = a >> n
    c = b & 0x01
    print('{} {:02x} {:02x} {:02x}'.format(n, a, b, c))

for i in range(8):
    getbit(i)

#
# 0 f7 f7 01
# 1 f7 7b 01
# 2 f7 3d 01
# 3 f7 1e 00
# 4 f7 0f 01
# 5 f7 07 01
# 6 f7 03 01
# 7 f7 01 01
