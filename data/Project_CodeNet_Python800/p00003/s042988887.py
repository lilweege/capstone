import sys

raw_input()

for line in sys.stdin.readlines():
    a, b, c = map(int, line.strip().split())
    input_list = [a, b, c]
    input_list.sort()
    if input_list[2] ** 2 ==  input_list[0] ** 2 + input_list[1] ** 2:
    	print 'YES'
    else:
    	print 'NO'