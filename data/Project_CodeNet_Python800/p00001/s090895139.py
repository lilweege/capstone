mount_list = []

for i in range(10):
  mount_list.append(int(input()))

mount_list.sort(reverse = True)

for i in range(3):
  print(mount_list[i])
