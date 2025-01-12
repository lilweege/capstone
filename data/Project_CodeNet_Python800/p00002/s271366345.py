while 1:
  try:
    a,b=map(int,raw_input().split())
    print len("%d"%(a+b))
  except:break