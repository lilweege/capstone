a = [(int)(input()) for i in range(10)]
for i in range(3):
    print(max(a))
    a.remove(max(a))