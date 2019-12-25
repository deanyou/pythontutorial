#!/usr/bin/python3

# 移位
a = 0x55
b = a >> 3
c = a << 3 # 注意：按32bit在移位
print('{:02x} {:02x} {:02x}'.format(a, b, c))


