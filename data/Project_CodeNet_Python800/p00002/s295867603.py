try:
    s=[]
    while True:
        t = input()
        s.append(t)
except EOFError:
    for i in range(len(s)):
        print(len(str(int(s[i].split(' ')[0])+int(s[i].split(' ')[1]))))