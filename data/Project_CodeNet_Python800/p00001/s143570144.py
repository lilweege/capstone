#List of Top 3 Hills

set = []
a = 9
for i in range(10):
    n = int(input())
    set.append(n)
set.sort()
while a >= 7:
    print(set[a])
    a -= 1