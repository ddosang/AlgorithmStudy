from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque(enumerate(priorities))
    
    while True: # 계속 해야하니까.. 이거 안주고 n번만 돌려서 답이 안됐었음..
        n = queue.popleft()
        for q in queue:
            if q[1] > n[1]:
                queue.append(n)
                break
        else:
            answer += 1
            if n[0] == location:
                return answer
    
    return 0
