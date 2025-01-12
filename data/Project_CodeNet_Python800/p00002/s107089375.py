def solve():
    from sys import stdin
    input_lines = stdin
    
    from math import log10
    
    for line in input_lines:
        a, b = map(int, line.split())
        
        if (a == 0 and b == 0):
            break
        
        print(int(log10(a + b)) + 1)

solve()
