import sys

arr = []
for i in sys.stdin:
    arr.append(int(i))

arr.sort()
arr.reverse()
for i in range(3):
    print(arr[i])