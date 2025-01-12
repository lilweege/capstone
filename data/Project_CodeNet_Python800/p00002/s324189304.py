import sys
array = []
for inp in sys.stdin.readlines():
    array.append(inp.split())
for i in range(len(array)):
    a =int(array[i][0]) + int(array[i][1])
    print(len(str(a)))