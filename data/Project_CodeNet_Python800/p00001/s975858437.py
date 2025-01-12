h=[int(input()) for i in range(10)]
h.sort(reverse=True)
[print(i) for i in h[:3]]