li = []
for i in xrange(10):
    s = map(str, raw_input().split())
    li.append(int(s[-1]))
li.sort(reverse=True)
for i in xrange(3):
    print li[i]