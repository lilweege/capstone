a = [input() for i in range(10)]
print max(a)
b = max(a)
a.remove(b)
print max(a)
b = max(a)
a.remove(b)
print max(a)