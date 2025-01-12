rank = [0] * 4
for _ in range(10):
    rank[0] = int(input())
    rank.sort()
for r in reversed(rank[1:]):
    print(r)