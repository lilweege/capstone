def main():
    for i in range(1, 10):
        for j in range(1, 10):
            ans = i * j
            s = str(i) + 'x' + str(j) + '=' + str(ans)
            print(s)

main()