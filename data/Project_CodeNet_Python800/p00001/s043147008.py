lists = []
for x in range (0, 10):
    num = int(input())
    lists.append(num)
    
results = sorted(lists, reverse = True)

print(results[0])
print(results[1])
print(results[2])