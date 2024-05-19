subjects = input()
n = int(input())
subject_candidates = [input() for i in range(n)]


subjects = list(subjects)
subject_candidates = list(map(lambda x: list(x), subject_candidates))

for index, subject in enumerate(subject_candidates):
    local_arr = []
    for sub in subject:
        if (sub in subjects) and not (sub in local_arr): 
            # 필수 과목에 있으면서 안나온 과목을 넣음.
            local_arr.append(sub)

    if subjects == local_arr:
        print("#" + str(index + 1) + " YES")
    else:
        print("#" + str(index + 1) + " NO")


# 240519 복습
import copy
import sys
input = sys.stdin.readline

order = list(input())
N = int(input())
arr = list(input() for _ in range(N))

order.pop()
for i, a in enumerate(arr):
    queue = copy.deepcopy(order)
    for c in a:
        if c in queue and c == queue[0]:
            queue.pop(0)

            if len(queue) == 0:
                print("#" + str(i + 1) + " YES", )
                break
    else:
        print("#" + str(i + 1) + " NO", )
