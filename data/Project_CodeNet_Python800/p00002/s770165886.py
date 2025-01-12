# 何行あるかわからない入力をまとめて処理する
import sys
line = sys.stdin.readlines()
#print(line)
for i in line:
    # map関数は配列の型を一括変換するのに便利
    b = list(map(int, i.split(" ")))
    c = 1
    d = b[0] + b[1]
    while(d >= 10):
        c += 1
        d = d / 10
    print(c)

