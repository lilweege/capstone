# Compatible with Python3
# -*- coding: utf-8 -*-
[print(i) for i in sorted([input() for j in range(10)], key=int, reverse=True)[:3]]