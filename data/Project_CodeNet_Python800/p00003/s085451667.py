n = int(raw_input())

for i in range(0, n):
    edge = map(int, raw_input().split(" "))
    edge.sort()
    if edge[2]*edge[2] == edge[0]*edge[0]+edge[1]*edge[1]: print "YES"
    else: print "NO"