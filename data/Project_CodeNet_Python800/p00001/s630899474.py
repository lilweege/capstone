#coding:UTF-8
def LoT(List):
    List2=sorted(List)
    for i in range(3):
        print(List2[len(List)-1-i])
if __name__=="__main__":
    List=[]
    for i in range(10):
        List.append(int(input()))
    LoT(List)