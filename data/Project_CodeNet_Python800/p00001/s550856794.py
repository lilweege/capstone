import sys
ms =list(map(int, sys.stdin.read().rstrip('\n').split('\n')))
ms.sort()
ms.reverse()
for i in range(3):
    print(ms[i])