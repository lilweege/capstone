while True:
  try:
    a,b = list(map(int,input().split()))
    print(len(str(a+b)))
  except EOFError:
    break
