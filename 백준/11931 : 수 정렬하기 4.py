n = int(sys.stdin.readline())
arr = [int(isys.stdin.readline()) for _ in range(n)]

arr.sort(reverse=True)

for a in arr:
    print(a)
