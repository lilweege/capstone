moutain = [0 for i in range(10)]
for i in range(10):
    moutain[i] = int(raw_input())
moutain.sort(reverse=True)
for i in range(3):
    print moutain[i]
