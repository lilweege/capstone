# coding:utf-8
mountlist = []
for _ in range(10):
    height = int(input())
    mountlist.append(height)
mountlist.sort()
mountlist.reverse()
[print(x) for x in mountlist[:3]]