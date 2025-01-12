line = [0]*10
for i in range(0, 10):
    line[i] = int(input())
line.sort(reverse=True, key=int)
for i in range(0, 3):
    print(line[i])