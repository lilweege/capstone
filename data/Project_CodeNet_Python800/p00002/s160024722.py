lst = []
for i in range(200):
    try:
        lst.append(input())
    except EOFError:
        break

print(*[len(str(sum([int(num) for num in string.split(' ')]))) for string in lst], sep='\n')