try:
    data = []
    while True:
        data.append(raw_input())

except EOFError:
    pass

for i in data:
    x, y = i.split()
    a, b = int(x), int(y)
    for j in range(1, 8): 
        if (a + b) / (10 ** j) < 1:
            print j
            break