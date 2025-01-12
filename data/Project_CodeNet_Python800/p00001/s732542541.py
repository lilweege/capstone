s = []

for i in range(10):
  s.append(int(raw_input()))

s.sort()

for i in range(3):
  print s[9-i]