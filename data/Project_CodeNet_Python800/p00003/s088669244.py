def judge(lists):
    lists.sort()
    if lists[0] ** 2 + lists[1] ** 2 - lists[2] ** 2:
        return False
    else:
        return True


def run():
    N = int(input())
    for _ in range(N):
        if judge([int(x) for x in input().split()]):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    run()
