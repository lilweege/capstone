def main():
    mountain=[]
    for i in range(10):
        num=int(input())
        mountain.append(num)
    mountain=sorted(mountain)
    mountain=mountain[::-1]
    for i in range(3):
        print(mountain[i])

if __name__=='__main__':
    main()