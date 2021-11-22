def solution(new_id):
    answer = []

    # step 1
    new_id = new_id.lower()

    # print(answer)

    # step 2
    for i in range(len(new_id)):
        c = new_id[i]
        if c.isdecimal() or c.isalpha() or c == "-" or c == "_" or c == ".":
            answer.append(c)

    # print(answer)

    # step 3
    start = len(answer) - 1
    for i in range(start, 0, -1):
        if answer[i] == "." and answer[i - 1] == ".":
            answer.pop(i)

    # print(answer)


    # step 4
    if len(answer) > 1:
        if answer[0] == ".":
            answer.pop(0)
        if answer[-1] == ".":
            answer.pop()
    elif len(answer) == 1:
        if answer[0] == ".":
            answer.pop()

    # print(answer)

    # step 5
    if len(answer) == 0:
        answer.append("a")

    # print(answer)

    # step 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == ".":
            answer.pop()

    # print(answer)

    # step 7
    last_c = answer[-1]
    while len(answer) < 3:
        answer += last_c

    # print(answer)

    answer = ''.join(str(c) for c in answer)
    return answer


