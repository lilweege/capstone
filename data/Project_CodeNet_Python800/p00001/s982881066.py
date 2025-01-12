def calc_mount_1(height_list):
    for i in range(len(height_list)):
        for i in range(len(height_list)-1):
            if height_list[i+1] < height_list[i]:
                tmp = height_list[i+1]
                height_list[i+1] = height_list[i]
                height_list[i] = tmp
            else:
                continue
    return height_list

N = 10
l = [input() for i in range(N)]
answer_array = calc_mount_1(l)
print "%d" % answer_array[-1]
print "%d" % answer_array[-2]
print "%d" % answer_array[-3]