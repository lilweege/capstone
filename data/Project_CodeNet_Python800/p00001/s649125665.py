s = 10*[0]

for i in range(10):
    s[i] = input()

s.sort(reverse = True)

for i in range(3):
    print s[i]