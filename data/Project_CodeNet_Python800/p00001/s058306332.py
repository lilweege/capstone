max = [0,0,0]
for a in range(10):
    s = int(input())
    if max[0] < s:
        max[2] = max[1]
        max[1] = max[0]
        max[0] = s
    elif max[1] < s:
        max[2] = max[1]
        max[1] = s
    elif max[2] < s:
        max[2] = s
for a in max:
    print(a)
