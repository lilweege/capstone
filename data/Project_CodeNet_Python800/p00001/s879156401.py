import fileinput

mountains = []
for cnt in range(10):
#    for line in fileinput.input():
    a = input()
    mountains.append(int(a))
mountains.sort()
print(mountains[9])
print(mountains[8])
print(mountains[7])