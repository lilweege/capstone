mol=[]
for i in range(10):
    mol.append(int(input()))

mol.sort(key=None,reverse=True)
for i in range(3):
    print(mol[i])