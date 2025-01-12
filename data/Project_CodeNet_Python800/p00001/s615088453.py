
def main():
    arr = []
    for i in range(0,10):
       arr.append(input()) 
    arr.sort()
    arr.reverse()
    for i in range(0,3):
        print arr[i]

if __name__ == '__main__':
    main()