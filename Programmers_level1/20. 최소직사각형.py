def solution(sizes):
    answer = 0
    new = []
    
    # 가로 세로 중 큰쪽은 큰쪽끼리 작은 쪽은 작은 쪽끼리 비교
    for x, y in sizes:
        if x > y:
            x, y = y, x
        new.append([x, y])
    
    new.sort()
    width = new[-1][0]
    new.sort(key = lambda x: x[1])
    height = new[-1][1]
    
    return width * height
