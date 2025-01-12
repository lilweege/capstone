import sys

a = []
for line in sys.stdin:
    a.append(line)

for n in a:
    inl=n.split()
    num=int(inl[0])+int(inl[1])
    l=list(str(num))
    time=0
    for i in l:
        time+=1
    print time