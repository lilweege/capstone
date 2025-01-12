High = []
for i in range(10):
    High.append(int(input()))
for i in range(3):
    print(max(High))
    High.remove(max(High))