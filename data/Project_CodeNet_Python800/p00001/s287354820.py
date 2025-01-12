if __name__=="__main__":
    dataset = []
    for i in range(10):
        a = int(input())
        dataset.append(a)
    for j in range(3):
        print(max(dataset))
        dataset.remove(max(dataset))