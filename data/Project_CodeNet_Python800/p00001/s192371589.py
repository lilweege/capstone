mt = list()
for i in range(10):
    mt.append(int(raw_input()))

mt = sorted(mt,reverse=True)
for i in range(3):
    print mt[i]