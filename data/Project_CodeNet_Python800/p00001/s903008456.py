import sys

def qsort(seq):
    if seq == []:
        return seq
    return qsort([x for x in seq[1:] if x < seq[0]]) + seq[0:1] + qsort([x for x in seq[1:] if x >= seq[0]])

data_set = []

for i in range(0, 10):
    data_set.append(int(input()))

rank = qsort(data_set)

for i in range(0,3):
    print(rank.pop(-1))