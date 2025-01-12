def calculate_digit_num(num):
    z = num / 10
    if z == 0:
        return 1
    else:
        return 1 + calculate_digit_num(z)

while True:
    try:
        num_list = [int(num) for num in raw_input().split(' ')]
        print calculate_digit_num(sum(num_list))
    except:
        break
