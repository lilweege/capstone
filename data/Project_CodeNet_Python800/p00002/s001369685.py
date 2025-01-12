from sys import stdin
for line in stdin:
    print(len(str(sum(map(int, line.split())))))

