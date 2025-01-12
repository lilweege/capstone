# -*- coding:utf-8 -*-
 
def main():
    while True:
        try:
            IN=input()
            if IN=="":
                raise EOFError
            else:
                val=IN.split(" ")
                a=int(val[0])+int(val[1])

                i=1
                flag=True
                while flag:
                    a=a/10
                    if a<1:
                        flag=False
                    else:
                        i+=1

            print(i)
        except EOFError:
            break
  
if __name__ == '__main__':
    main()