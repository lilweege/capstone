# -*- coding:utf-8 -*-

def main():
    List=[]

    for i in range(10):
        a=int(input())
        List.append(a)

    List.sort(reverse=True)
    print(List[0])
    print(List[1])
    print(List[2])
        
 
if __name__ == '__main__':
    main()