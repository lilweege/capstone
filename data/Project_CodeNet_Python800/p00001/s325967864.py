a = []
for i in range(10):
    a.append(input())
a1_list = [int(i) for i in a]
a1_list.sort()
for i in range(3):
    print(a1_list[9-i])