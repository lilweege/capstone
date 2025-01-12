a = []
while True:
    try:
        a.append(list(map(int, input().split())))
    except EOFError:
        break

for i in a:
    print(len(str(i[0] + i[1])))

