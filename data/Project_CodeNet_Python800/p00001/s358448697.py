# your code goes here
import sys

a=[]
for line in sys.stdin:
  line.rstrip('rn')
  tmp=line.split(" ")
  a.append(int(tmp[-1]))

a.sort(reverse=True)
y=0
for i in a:
  if y==3:
    break
  if i>=0 and i<=10000:
    print(i)
    y=y+1