listal=[]
while True:
    try:
        listal.append(input())
    except EOFError:
        break
tyon=[]
for i in listal:
    lista=i.split()
    tyon.append(len(str(int(lista[0])+int(lista[1]))))
for i in tyon:
    print(i)

