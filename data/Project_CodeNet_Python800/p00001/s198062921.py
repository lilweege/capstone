mountains = [int(input()) for _ in range(10)]

for height in sorted(mountains)[-3:][::-1]:
    print(height)