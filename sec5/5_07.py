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
