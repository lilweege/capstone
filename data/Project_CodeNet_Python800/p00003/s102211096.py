for _ in[0]*int(input()):
 a,b,c=sorted(map(int,input().split()))
 print(['NO','YES'][a*a+b*b==c*c])
