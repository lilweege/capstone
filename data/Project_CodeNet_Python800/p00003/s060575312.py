n = int(input())

i = 0
while (i < n):
    L = map(int, raw_input().split())
    L.sort(reverse = True)

    if (pow(L[0], 2) == pow(L[1], 2) + pow(L[2], 2)):
        print "YES"
    else:
        print "NO"

    i += 1