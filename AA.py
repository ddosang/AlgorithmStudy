import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
seq = list(map(int, input().split()))
original = []


#맨 뒤 수는 더 큰 애가 없으니까 그냥 배열에 넣고
#그 다음 수는 맨 뒤 수보다 앞이면 0 뒤면 1
#그 다음 수는 자기보다 큰 두 수보다 뒤면 2 하나 앞이면 1 맨 앞이면 0
# ...
#결국 역수열은 해당 수보다 작은 수를 다 지운 수열에서 해당 수의 index를 나타낸 것이 됨.
for i in range(n-1, -1, -1):
    original.insert(seq[i], i+1)

for x in original:
    print(x, end=' ')