import sys
import math

ary=[]
ans=[]
for i in sys.stdin:
    ary.append(list(map(int,i.split())))
    ans.append(int(math.log10(sum(ary[-1]))+1))
print('\n'.join(map(str,ans)))