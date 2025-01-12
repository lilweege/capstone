mountains = []
for x in range(10):
  mountains.append(int(raw_input()))

mountains.sort()
mountains.reverse()
print mountains[0]
print mountains[1]
print mountains[2]