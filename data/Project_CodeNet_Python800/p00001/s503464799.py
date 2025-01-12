mountains = []

for _ in range(10):
    mountains.append(int(input()))

mountains.sort(reverse=True)

for height in mountains[:3]:
    print(height)

