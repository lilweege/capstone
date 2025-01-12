import sys

def solve():
    a = [int(input()) for i in range(10)]
    a.sort(reverse=True)
    print(*a[:3], sep='\n')
    
if __name__ == '__main__':
    solve()