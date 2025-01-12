N=10
A=[int(input()) for i in range(N)]
A.sort(reverse=True)
for i in range(3):
    print(A[i])