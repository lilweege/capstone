while True:
  try:
    data_set = map(int, raw_input().split())
  except EOFError:
    break
  count = 0
  a = data_set[0]
  b = data_set[1]
  sum = a + b
  while sum > 0:
    sum /= 10
    count += 1
  print count