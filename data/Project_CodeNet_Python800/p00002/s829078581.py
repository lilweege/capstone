while True:
  try:
    x, y = map(int, input().split())
    print(len(str(x+y)))
  except EOFError:
    break