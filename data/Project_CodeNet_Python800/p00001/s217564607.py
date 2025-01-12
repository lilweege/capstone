# coding: utf-8
# Here your code !
array = []
for i in range(10):
 line = int(input())
 array += [line]

result = sorted(array)[::-1]

print(result[0])
print(result[1])
print(result[2])