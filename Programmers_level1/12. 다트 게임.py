from functools import reduce

def solution(dartResult):
    answer = 0
    
    calculates = {'S': 1, 'D': 2, 'T': 3};
    sum = 0
    temp = []
    previous = ''
    c = ''
    

    for i in range(len(dartResult)):
        # 10 처럼 두자리 숫자가 들어올 때를 대비해서 이전 것을 저장.
        previous = c
        c = dartResult[i]
        
        # 숫자가 들어오면 일단 넣는다.
        if c.isdecimal():
            # 근데 두자리 수 인 경우 1, 10 이렇게 두번 들어가므로
            # 앞의 것을 하나 pop 하고 넣는다.
            if previous.isdecimal():
                temp.pop()
                c = previous + c # 두자리 수로 만든다.
            temp.append(int(c))
        
        # 알파벳이라면 앞에 들어간 숫자에 알파벳에 따라 제곱해준다.
        # 알파벳에 따른 숫자는 딕셔너리로 저장해둠.
        elif c.isalpha():
            temp[len(temp)-1] **= calculates[c]
            
        # #이라면 이전 점수만큼 잃어야 하므로 이전 것에 * -1
        elif c == '#':
            temp[len(temp)-1] *= -1
        
        # * 이라면 이전 두개만큼 영향을 미치는데,
        # 배열에 아직 숫자가 2개가 없는 경우는 파이썬의.. 멋진 인덱싱에 의해 *2가 두번 일어나므로,
        # if else 문으로 경우를 나누었다.
        elif c == "*":
            if len(temp) >= 2:
                temp[len(temp)-1] *= 2
                temp[len(temp)-2] *= 2
            else:
                temp[0] *= 2
    
    
    # temp를 sum 함수로 sum 변수에 합침.
    # from functools import reduce 필수.
    def sum(a, b):
        return a + b
    sum = reduce(sum, temp)
    
    return sum
