#!/usr/bin/python3

# slice

# 1.
a = 'hello world'
b = a[0]
c = a[10]
print(b, c) # h d

# 2.
b = a[-1]
c = a[-2]
d = a[-3]
print(b, c, d) # d l r

# 3.
b = a[0:3]
c = a[1:3]
print(b, c) # hel el

# 4.
b = a[:2]
c = a[1:]
d = a[:]
print(b) # he
print(c) # ello world 
print(d) # hello world

# 5.
b = a[::2]
c = a[::-1]
print(b) # hlowrd
print(c) # dlrow olleh



