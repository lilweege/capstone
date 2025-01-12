try:
    s = []
    while True:
        t = input()
        s.append(t)
except EOFError:
    for i in range(len(s)):
        a = int(s[i].split(' ')[0])
        b = int(s[i].split(' ')[1])
        print(len(str(a + b)))