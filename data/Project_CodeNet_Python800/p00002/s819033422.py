import math

while 1:
  try:
    a,b=map(int, input().split())
    print(len(format(a+b)))

  except:
    break
