li = sorted([int(input()) for i in range(10)], reverse=True)
print("\n".join(map(str, li[:3])))