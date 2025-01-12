lst = []
for i in range(10):
    lst.append(int(input()))
for j in range(3):
    print max(lst)
    lst.remove(max(lst))