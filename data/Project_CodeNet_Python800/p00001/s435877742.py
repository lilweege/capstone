l=[int(input()) for _ in range(10)]
[print(x) for x in sorted(l, reverse=True)[:3]]