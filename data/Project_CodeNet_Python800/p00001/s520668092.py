mt = list()
n = 10

for i in range(n):
    mt.append(int(input()))
mt.sort(reverse=True)
for j in range(3):
    print(mt[j])