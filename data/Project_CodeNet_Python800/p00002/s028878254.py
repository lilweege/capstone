# -*- utf-8 -*-

while True:
    try:
        inp = raw_input()
        i = map(int, inp.split())
        a = i[0]
        b = i[1]
    
        s = a + b
    except:
        break
    
    ans = 0
    
    while s >= 1:
        s /= 10
        ans += 1
    
    print ans