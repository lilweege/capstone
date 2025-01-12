import sys

def main():

    inputs = sys.stdin.readlines()
    for item in inputs:
        print(len(str(sum(tuple(map(int, item.split()))))))
    
main()