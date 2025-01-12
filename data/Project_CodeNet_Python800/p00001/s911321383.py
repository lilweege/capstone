inputList = []
while True:
    try:
        num = int(input())
    except EOFError:
        break
    inputList.append(num)

inputList.sort()
length = len(inputList)
for i in range(3):
    print(inputList[length - i - 1])