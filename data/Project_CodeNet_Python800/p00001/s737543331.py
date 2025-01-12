f, s, t = 3,2,1
for i in range(10):
    z = int(input())
    if z >= f:
        f,s,t = z, f, s;
    elif z>=s:
        s,t = z,s;
    elif z>=t:
        t = z
print(f);print(s);print(t)