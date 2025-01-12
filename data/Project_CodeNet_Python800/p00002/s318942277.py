# -*-coding:utf-8-*-

def get_input():
    
    while True:
        try:
            yield "".join(input())
        except EOFError:
            break
                     
if __name__=="__main__":
    array = list(get_input())
    for i in range(len(array)):
        
        temp = array[i].split()
        
        a = int(temp[0])
        b = int(temp[1])
                        
        ans = a + b
        
        print(len(str(ans)))