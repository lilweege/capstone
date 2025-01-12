def __main():

    mountains = []
    numOfMoun = 10
 
    for c in range(numOfMoun):
        mountains.insert(c,int(input()))
        
    sorted_mounts = sorted(mountains,reverse=True)
    for k in range(3):
        print(sorted_mounts[k])

__main()

