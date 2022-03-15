t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    print("#", i+1, sep="", end=" ")
    print(sorted(arr[s-1:e])[k-1])
