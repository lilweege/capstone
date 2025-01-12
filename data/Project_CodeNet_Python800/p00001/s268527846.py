def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


array = []
for _ in range(10):
    array.append(int(input()))

sorted_array = quicksort(array)
for i in range(3):
    print(sorted_array[9-i])