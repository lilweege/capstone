while True:
    try:
        inputNums = list(map(int, input().split()))
        print(len(str(inputNums[0] + inputNums[1])))
    except:
        break