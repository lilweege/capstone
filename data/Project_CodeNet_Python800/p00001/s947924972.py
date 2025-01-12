d = [int(input()) for _ in range(10)]
d.sort(reverse=True)
[print(x) for x in d[:3]]