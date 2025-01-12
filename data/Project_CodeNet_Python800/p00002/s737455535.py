l = []
while True:
    try:
        s = raw_input()
    except:
        break
    l.append(len(str(sum(map(int, s.split())))))
for i in l:
    print i