mountains = []
for x in range(10):
    mountains.append(int(raw_input()))
mountains.sort()
print(mountains[-1])
print(mountains[-2])
print(mountains[-3])