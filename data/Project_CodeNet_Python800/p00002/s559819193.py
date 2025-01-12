num_list = []
while True:
    try:
        num_list.append(input().split())
    except EOFError:
        break

for i in num_list:
    if i != []:
        ans = len(str(int(i[0]) + int(i[1])))
        print(ans)
