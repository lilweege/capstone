def qsort(l):
    if l == []: return []
    else:
        pv = l[0]
        left = []
        right = []
        for i in range(1, len(l)):
            if l[i] > pv:
                left.append(l[i])
            else:
                right.append(l[i])
        left = qsort(left)
        right = qsort(right)
        left.append(pv)
        return left + right

def main():
    lst = []
    for i in range(0, 10):
        lst.append(int(raw_input()))

    lst = qsort(lst)
    for i in range(0, 3):
        print(lst[i])

main()