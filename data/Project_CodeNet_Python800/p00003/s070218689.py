#coing:utf-8


def distance(a,b):

    dst = pow(a,2) + pow(b,2)

    return dst

def isTriangle(lines):

    idxList = [[0,1,2],[1,0,2],[2,0,1]]
    flag = False
    for i in idxList:
        if not flag and pow(lines[i[0]],2) == distance(lines[i[1]], lines[i[2]]):
            flag = True

    return flag

if __name__ == '__main__':

    num = int(input())

    results = []

    for i in range(num):
        lines = [int(item) for item in input().split(" ")]
        results.append(isTriangle(lines))

    for r in results:
        if r:
            print("YES")
        else :
            print("NO")