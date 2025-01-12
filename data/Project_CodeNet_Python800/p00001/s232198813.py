ls = []
while True:
    try:
        n = int(raw_input())
    except EOFError:
        break

    ls.append(n)

ls.sort(reverse=True)
print ls[0]
print ls[1]
print ls[2]