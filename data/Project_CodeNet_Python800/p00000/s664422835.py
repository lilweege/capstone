# coding: utf-8

import codecs
import sys

sys.stdout = codecs.getwriter("shift_jis")(sys.stdout) # ??????
sys.stdin = codecs.getreader("shift_jis")(sys.stdin) # ??\???

# ??\??¬?????????print??????????????´?????? print(u'?????????') ??¨??????
# ??\??¬?????????input??? input(u'?????????') ??§OK
# ??°?¢???????????????????????????´??????6,7???????????????????????¢??????

for i in range(1,10):
	for j in range(1,10):
		k = i * j
		print("{0}x{1}={2}".format(i , j , k))