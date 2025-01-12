import sys

li = []
for line in sys.stdin:
   li.append(int(line))
   if len(li) == 10:
      break

li.sort(reverse=True)
li = li[0:3]
for i in li:
   print(i)