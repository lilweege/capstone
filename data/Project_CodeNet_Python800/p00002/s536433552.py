import math

while True:
    try:
        line = input().split(" ")
        a = int(line[0])
        b = int(line[1])
        print(int(math.log10(a+b))+1)
    except:
        break