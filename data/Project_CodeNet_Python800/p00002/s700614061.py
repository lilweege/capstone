while 1:
    try:
        sum = input()
        sum_list = sum.split()
        print(len(str(int(sum_list[0]) + int(sum_list[1]))))
    except EOFError:
        break
    
