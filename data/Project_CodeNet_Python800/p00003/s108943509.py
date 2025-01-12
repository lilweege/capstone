data = []
try:
    while True:
        data.append(raw_input())

except EOFError:
    pass

n = int(data[0])
if n <= 1000:
    for i in range(1, n+1):
        x, y, z = data[i].split()
        x, y, z = int(x), int(y), int(z)
        if x <= 1000 and y <= 1000 and z <= 1000:
            if (z * 0.8 == x and z * 0.6 == y
                or z * 0.8 == y and z * 0.6 == x
                or y * 0.8 == x and y * 0.6 == z
                or y * 0.8 == z and y * 0.6 == x
                or x * 0.8 == z and x * 0.6 == y
                or x * 0.8 == y and x * 0.6 == z):
                print "YES"
            else:
                print "NO"