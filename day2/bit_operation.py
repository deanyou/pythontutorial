#!/usr/bin/python3

# 按位与、按位或
a = 0x55
b = a & 0x50
c = a | 0x5F
print('{:x} {:x} {:x}'.format(a, b, c)) # 55 50 5f

