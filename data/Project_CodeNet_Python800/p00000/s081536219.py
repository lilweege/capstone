a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9]

if __name__ == "__main__":
    for x in a:
        for y in b:
            print(x,end="")
            print("x",end="")
            print(y,end="")
            print("=",end="")
            print(x*y)
else:
    pass

