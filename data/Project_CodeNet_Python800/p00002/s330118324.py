#Digit Number

while True:
    try:
        i, n = input(). split()
        m = str(int(i) + int(n))
        print(len(m))
    except:
        break