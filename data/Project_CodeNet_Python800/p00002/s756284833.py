import math

while True:
    try:
        line = input().split(" ")
        print(int(math.log10(int(line[0])+int(line[1])))+1)
    except:
        break