array = []
for _ in range(10):
    array.append(int(input()))

sorted_array = sorted(array,reverse=True)
for i in range(3):
    print(sorted_array[i])