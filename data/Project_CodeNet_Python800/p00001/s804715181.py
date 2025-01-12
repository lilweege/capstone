array=[int(input()) for i in range(10)]
array.sort()
num = len(array)
for i in range(num-1,num-4,-1):
    print(array[i]) 