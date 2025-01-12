import sys
print('\n'.join(map(str, sorted([int(h.strip()) for h in sys.stdin], reverse=True)[:3])))