a_list = []
for i in range(10):
    while True:
        a = input()
        a = int(a)
        if 0<=a and a<=10000:break
    a_list.append(a)

for i in range(3):
    print(max(a_list))
    a_list.remove(max(a_list))
