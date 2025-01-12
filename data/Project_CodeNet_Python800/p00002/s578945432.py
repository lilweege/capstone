# AOJ 0002 Digit Number
# Python3 2018.6.7 bal4u

while True:
    try:
        a = list(map(int, input().split()))
        print(len(str(a[0] + a[1])))
    except EOFError:
        break
