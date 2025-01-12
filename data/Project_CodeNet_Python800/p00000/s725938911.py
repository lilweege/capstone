#
# AIZU ONLINE JUDGE: QQ
# cf. http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0000&lang=jp
#

qq = [str(x) + "x" + str(y) + "=" + str(x * y) for x in range(1,10) for y in range(1,10)]
for q in qq:
    print q