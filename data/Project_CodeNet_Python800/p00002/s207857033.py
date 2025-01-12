def digits(x):
    i=0
    while (x>0):
        x/=10
        i+=1
    return i

while True:
    try:
        line=raw_input()
        (a,b)=line.split()
        (a,b)=map(int,(a,b))
        print digits(a+b)
    except EOFError: break