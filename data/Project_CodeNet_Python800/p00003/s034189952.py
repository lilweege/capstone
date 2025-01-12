import sys
for i in sys.stdin:
    try:
        sidelen = [int(j) for j in i.split(" ")]
        sidelen.sort(reverse=True)
        if(sidelen[0]**2 == sidelen[1]**2 + sidelen[2]**2):
            print("YES")
        else:
            print("NO")
    except:
        continue