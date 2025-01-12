order=[]
for number in range(10):
    hight=int(input())
    order.append(hight)
for j in range(9):
    for i in range(9):
        if order[i] < order[i+1]:
            a = order[i]
            b = order[i+1]
            order[i] = b
            order[i+1] = a
for i in range(3):
    print(order[i])