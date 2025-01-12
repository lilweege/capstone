import math

digit = []
while True:
    try:
        a,b =raw_input().split()
        c = int(a)+int(b)
        digit.append(int(math.log10(c) + 1))
    except:
        break
for i in range(0,len(digit)):
    print digit[i]