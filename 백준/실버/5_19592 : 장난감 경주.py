T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split()) # 자동차 수 / 거리 / 부스터 제한 속도
    velocity = list(map(int, input().split()))
    # 첫 1초 부스터 Z <= Y, 그 이후는 velocity[N-1] (나 N번) 로 X m 를 가야함.
    V = velocity.pop() # 내 속도

    fastest_time = X / max(velocity)
    # 가장 빠른 차의 시간보다 빨리 가야하는데, 
    # 부스터로 가지 않는 거리는 정해져있으므로 빼준다.
    X -= (fastest_time - 1) * V 
    
    # 공동 우승은 안되니까 같으면 안되고, time 이 정수가 아닐수도 있으므로 1을 더해서 내림
    booster_dist = int(X + 1)
  
    # 원래 속도보다 낮다면 부스터 필요 없음. 0
    if booster_dist <= V:
        ans = 0
    # 제한 속도보다 낮다면 부스터로 이길 수 있음.
    elif booster_dist <= Y:
        ans = booster_dist
    # 이길 수 없음
    else:
        ans = -1

    print(ans)
