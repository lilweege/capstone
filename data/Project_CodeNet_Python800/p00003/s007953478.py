n =  int(input())
for i in range(n):
    tri_list = list(map(int,input().split(" ")))
    #tri_list = input().split(" ")
    tri_list.sort()
    a = int(tri_list[2]) ** 2
    b = int(tri_list[0]) ** 2 + int(tri_list[1]) ** 2
    if a == b:
        print("YES")
    else:
        print("NO")
