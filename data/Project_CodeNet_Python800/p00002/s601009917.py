
A = []
B = []
s = True
while(s):
    try:
        a,b = map(int, input().split())
    except:
        break
    A.append(a)
    B.append(b)

for i in range(len(A)):
    sum = A[i] + B[i]
    digits = 1
    while(sum//10 != 0):
        digits += 1
        sum //= 10
    print(str(digits))

