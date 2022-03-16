n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
res = []


while arr1 and arr2:
    if arr1[0] < arr2[0]:
        res.append(arr1.pop(0))
    else:
        res.append(arr2.pop(0))

while arr1:
    res.append(arr1.pop(0))

while arr2:
    res.append(arr2.pop(0))

for r in res:
    print(r, end=' ')
