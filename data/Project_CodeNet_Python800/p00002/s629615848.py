import sys

num_of_data = 1
while True:
    if num_of_data > 200:
        break

    try:
        a, b = input().split()
         
    except EOFError:
        sys.exit()
        
    a = int(a)
    b = int(b)
    if a >= 0 and a <= 1000000000:
        if b >= 0 and b <= 1000000000:     
            num_of_data += 1
            sum = a+b
            cnt = 1
            while True:
                if sum < 10:
                    break
                sum /= 10
                cnt += 1
            print(cnt)
