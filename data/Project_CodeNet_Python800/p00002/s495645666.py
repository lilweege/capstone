while True:
    try:
        nums = map(int, raw_input().split(' '))
        
        ans = nums[0]+nums[1]
        
        x = 0
        while True:
            if (10**x -1) < ans < 10**(x+1):
                print x+1
                break
            else:
                x = x+1
    except EOFError:
        break 