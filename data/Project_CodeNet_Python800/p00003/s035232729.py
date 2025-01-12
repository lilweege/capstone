for i in range(int(input())):
    n = [int(i) for i in input().split(" ")]
    n.sort()
    print("YES" if n[0] * n[0] + n[1] * n[1] == n[2] * n[2] else "NO")