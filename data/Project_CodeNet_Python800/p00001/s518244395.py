import sys
mt_heights = map(int, sys.stdin.readlines())
mt_heights.sort(reverse=True)
for height in mt_heights[:3]:
    print height