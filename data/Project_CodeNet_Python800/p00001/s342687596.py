inp = [int(input()) for i in range(10)]
m1, m2, m3 = 0, 0, 0
for h in inp:
    if(h > m1):
        m3 = m2
        m2 = m1
        m1 = h
    elif(h > m2):
        m3 = m2
        m2 = h
    elif(h > m3):
        m3 = h
print(m1)
print(m2)
print(m3)