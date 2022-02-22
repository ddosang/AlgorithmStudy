import math

def solution(brown, yellow):
    answer = []
    j = 1

    for i in range(1, int(math.sqrt(yellow)) + 1):
        if yellow % i == 0: # yellow 의 약수에
            row = col = j = 1
            while row * col < brown + yellow:
                # 위아래 양옆으로 한칸씩 더해가면서 넓이를 계산해 해본다.
                row = (i + 2 * j) 
                col = ((yellow / i) + 2 * j)
                j += 1
                
            if row * col == brown + yellow:
                return [row, col] if row > col else [col, row]
    
    return answer
