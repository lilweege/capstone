mountains_high=[]
for i in range(10):
    mountains_high.append(int(input()))

mountains_high_copy=mountains_high.copy()
for i in range(9):
    for j in range(9):
        if mountains_high_copy[j]>mountains_high_copy[j+1]:
            num=mountains_high_copy[j]
            mountains_high_copy[j]=mountains_high_copy[j+1]
            mountains_high_copy[j+1]=num

for i in range(3):
    print(mountains_high_copy[9-i])