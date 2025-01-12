data_set=[]
for i in range(0,10):
        data_set.append(input())
top=sorted(data_set,reverse=True)
for i in range(0,3):
        print(top[i])