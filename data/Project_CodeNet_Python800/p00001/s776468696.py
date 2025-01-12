# coding: utf-8

mountains = []
for i in range(10):
    mountains.append(int(input()))
    
outputCount = 3    
for height in list(reversed(sorted(mountains))):
    print(height)
    outputCount -= 1
    if outputCount == 0:
        break