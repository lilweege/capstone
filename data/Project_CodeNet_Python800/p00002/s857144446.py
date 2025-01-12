# -*- coding: utf-8 -*-
while True:
    try:
        x = [int(i) for i in raw_input().split(" ")]
        print len(str(x[0]+x[1]))
    except Exception:
        break