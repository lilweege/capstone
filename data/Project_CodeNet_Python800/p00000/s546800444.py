i=1
j=1
while True:
    if j==10:
        j=1
        i+=1
    if i==10:
        break
    ans=i*j
    print str(i)+"x"+str(j)+"="+str(ans)
    j+=1