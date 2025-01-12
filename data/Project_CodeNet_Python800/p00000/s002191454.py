M = 9
N = 9

def main():
    for i in range(1,M+1,1):
        for j in range(1,N+1,1):
            mult = i * j
            print(str(i) + "x" + str(j) + "=" + str(i * j))
main()
