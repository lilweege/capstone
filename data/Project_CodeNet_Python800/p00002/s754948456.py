import sys

def main():
    for input_line in sys.stdin:
        num1 = int(input_line.split(' ')[0])
        num2 = int(input_line.split(' ')[1])
        
        sum = str(num1 + num2)
        
        count = 0
        for num in sum:
            count += 1
        else:
            print(count)
    
if __name__ == '__main__':
    main()