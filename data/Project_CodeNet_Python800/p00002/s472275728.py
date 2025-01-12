line = []
try:
    while True:
        a,b = input().split(" ")
        d = int(a) + int(b)
        list = [c for c in str(d)]
        line.append(len(list))
except EOFError:
    for e in range(0,len(line)):
        print(line[e])
