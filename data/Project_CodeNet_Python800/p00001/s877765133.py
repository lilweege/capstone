mountains = []
[mountains.append(int(input())) for i in range(10)]
mountains = sorted(mountains)[::-1]
for j in range(3):
    print(mountains[j])