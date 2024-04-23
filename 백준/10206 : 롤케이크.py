N, M = map(int, input().split())
rolls = sorted(list(map(int, input().split())), key=lambda x:(x%10, x))

cnt = 0

for r in rolls:
    cut = (r - 1) // 10 

    local_count = cut if cut <= M else M
    cnt += local_count
    M -= local_count

    if r - local_count * 10 == 10:
        cnt += 1

    # print(cnt, M)
    

print(cnt)
