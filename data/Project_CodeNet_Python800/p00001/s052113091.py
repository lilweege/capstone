list=list()
for i in range(10):
    t=input()
    list.append(int(t))
list.sort(reverse=True)
for i in range(3):
    print(list[i])