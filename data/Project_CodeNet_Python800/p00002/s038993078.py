import sys

a = []
answer_array = []
for line in sys.stdin:
    a.append(map(int, line.strip().split()))
    #except StopIteration:
        #break

for i in range(len(a)):
    sum_up = a[i][0] + a[i][1]

    answer = len(str(sum_up))

    answer_array.append(answer)

for j in range(len(answer_array)):
    print answer_array[j]