def get_input():
    while True:
        try:
            yield ''.join(raw_input())
        except EOFError:
            break

if __name__ == '__main__':
    a = list(get_input())

for n in a:
    inl=n.split()
    num=int(inl[0])+int(inl[1])
    l=list(str(num))
    time=0
    for i in l:
        time+=1
    print time