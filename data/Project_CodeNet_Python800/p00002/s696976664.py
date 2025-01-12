import sys
try:
    while True:
        a,b= map(int, input().split())
        sum1=a+b
        sum1s=str(sum1)
        kata_sum1s=len(sum1s)
        keta=int(kata_sum1s)
        print(str(keta))
except EOFError:
    pass

