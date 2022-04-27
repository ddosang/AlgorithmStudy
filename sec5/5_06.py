n, m = map(int, input().split())
illness = list(map(int, input().split()))

illness = list(enumerate(illness)) # 중복 값이 있을 수 있어서 enumerate 로 사용.
mth = illness[m]
count = 0
while illness and (mth in illness):
    ordered = illness.pop(0)
    if illness and ordered[1] < max(list(map(lambda x: x[1], illness))):
    # if any(ordered[1] < ill[1] for ill in illness):  # 강의 방법.... any!!!
        illness.append(ordered)
    else:
        count += 1
        if ordered == mth:
            break

    print(illness)
print(count)
