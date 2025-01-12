import math

while True:
    try:
        line = input().split(" ")
        if(len(line) != 2):
            exit()
        a = int(line[0])
        b = int(line[1])
        print(int(math.log10(a+b))+1)
    except:
        break