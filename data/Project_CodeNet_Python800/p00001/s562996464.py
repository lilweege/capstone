# coding: utf-8
#Problem Name: List of Top 3 Hills
#ID: tabris
#Mail: t123037@kaiyodai.ac.jp

height = [0 for _ in range(10)]
for i in range(10):
    height[i] = int(raw_input())

top3 = sorted(height)[:6:-1]
for h in top3:
    print h

'''
sample input
1819
2003
876
2840
1723
1673
3776
2848
1592
922
'''