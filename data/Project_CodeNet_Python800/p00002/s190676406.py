while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    arr = map((lambda x: int(x)), line.split())
    print len(str(arr[0]+arr[1]))