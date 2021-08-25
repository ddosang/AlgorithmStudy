# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
#sys.stdin = open("input.txt", "rt")


t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())

    array = input().split()
    array = list(map(int, array))

    arr = array[s-1:e]
    arr.sort()
    print("#", i+1, sep="", end=' ')
    print(arr[k-1])



