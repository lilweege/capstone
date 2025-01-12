# coding: utf-8
# Here your code !

mount = [int(input()) for i in range(10)]
a = max(mount)
mount.remove(a)
b = max(mount)
mount.remove(b)
print(a)
print(b)
print(max(mount))