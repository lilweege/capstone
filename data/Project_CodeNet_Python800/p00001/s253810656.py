hill = []
while True:
    try:
        hill.append(int(input()))
    except:
        break
for i in range(1, len(hill)):
    key = hill[i]
    j = i-1
    while j >= 0 and hill[j] < key:
        hill[j+1] = hill[j]
        j -= 1
    hill[j+1] = key

for i in range(3):
    print(hill[i])