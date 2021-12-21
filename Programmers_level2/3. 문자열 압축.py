# https://programmers.co.kr/learn/challenges
def solution(s):
    answer = 0
    length = len(s)
    min_length = len(s)

    count = 0
    # 반 이상이 되면 같은 갯수만큼 끊을 수 없으니까 반까지만.
    for j in range(1, int(length / 2) + 1):
        temp_length = length
        # j개만큼 끊어서
        for k in range(0, length - j + 1, j):
            # 현재꺼랑 뒤에꺼랑 같으면 축약 가능.
            if s[k:k + j] == s[k + j:k + 2 * j]:
                # 축약 하면 해당 글자수만큼 길이가 줄어듬.
                count += 1
                temp_length -= j
                # 근데 처음 축약하는 경우는 앞에 숫자가 붙으니까 1 늘어남.
                if count == 1:
                    temp_length += 1
                # 1이 아닌 경우는 그냥 줄어든다고만 생각했는데,
                # 10 100 1000 되면 10a 이렇게 합쳐지니까.. 한자리 더 느는거였네
                # 깔끔하게 풀려면 정규표현식 써서 다시 풀자... 어쩔수없다..
                elif count == 9:
                    temp_length += 1
                elif count == 99:
                    temp_length += 1
                elif count == 999:
                    temp_length += 1
                    
            # 문자열이 반복되지 않으면 count 초기화
            else:
                count = 0
#         print(j, temp_length)
        if min_length > temp_length:
            min_length = temp_length

    return min_length
