#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def main():
    for lhs in range(1,9+1):
        for rhs in range(1,9+1):
            print("{}x{}={}".format(lhs, rhs, lhs*rhs))

if __name__ == "__main__": main()