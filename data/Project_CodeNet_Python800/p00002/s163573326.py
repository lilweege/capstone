while True:
    try:
        a, b = raw_input().strip().split(" ")
        print len(str(int(a) + int(b)))
    except:
        break;