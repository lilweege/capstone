mountains = []

for i in range(10):
    m = int(input())
    mountains.append(m)

mountains.sort(reverse=True)

for i in range(3):
    print(mountains[i])
