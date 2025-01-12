height = [0 for i in range(10)]
sort_height = [0 for i in range(10)]

#set
for i in range(10):
    height[i] = int(input())

#sort
for i in range(10):
    for j in range(10):
        if height[i] >= sort_height[j]:
            #?????????
            for k in range(9, j, -1):
                sort_height[k] = sort_height[k-1] 

            sort_height[j] = height[i]
            break
        
for i in range(3):
    print(sort_height[i])