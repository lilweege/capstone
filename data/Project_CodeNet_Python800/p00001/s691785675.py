def get_input():
    while True:
        try:
            yield ''.join(raw_input().strip())
        except EOFError:
            break
height = list(get_input())
height = sorted(map(int,height),reverse=True)
print height[0]
print height[1]
print height[2]