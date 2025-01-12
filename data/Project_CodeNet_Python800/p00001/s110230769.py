inputNum = []

for i in range(0, 10):
  inputNum.append(int(raw_input()))

inputNum.sort(reverse=True)

for i in range(0, 3):
  print inputNum[i]