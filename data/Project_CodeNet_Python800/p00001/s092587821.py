import sys 
height_li = []
for i in range(10):
    height_li.append(int(input()))
for i in range(3):
    print(sorted(height_li,reverse=True)[i])