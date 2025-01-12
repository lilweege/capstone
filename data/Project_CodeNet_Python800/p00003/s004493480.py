n = int(raw_input())
for i in range(n):
    num = map(int, raw_input().split())
    num.sort(reverse=True)
    if num[0]**2 == num[1]**2 + num[2]**2:
        print "YES"
    else:
        print "NO"
