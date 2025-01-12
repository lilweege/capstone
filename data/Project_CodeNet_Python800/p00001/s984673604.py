mountains = []
for i in range(10):
    mountains.append(int(input()))
for m in sorted(mountains)[-1:-4:-1]:
    print(m)