Height = [0]*10

for i in range (10):
    Height[i] = int(input())
Height.sort()
Height.reverse()
for j in range(3):
    print(Height[j])
