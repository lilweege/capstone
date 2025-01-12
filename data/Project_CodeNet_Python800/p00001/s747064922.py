
a = []

while True:
    try:
        n = int(input())
        a.append(n)
    except:
        break

print(max(a))
a.remove(max(a))
print(max(a))
a.remove(max(a))
print(max(a))
