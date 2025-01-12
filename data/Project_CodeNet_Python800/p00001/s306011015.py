list1=[]
for i in range(10):
    list1.append(int(input()))
list1=sorted(list1)
list1.reverse()
for i in range(3):
    print(list1[i])