from sys import stdin
for line in stdin:
    a,b = line.split(" ")
    c = int(a)+int(b)
    print(len(str(c)))

