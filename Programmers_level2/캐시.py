# https://programmers.co.kr/learn/courses/30/lessons/17680
def solution(cacheSize, cities):
    time = 0
    cache = []

    for city in cities:
        city = city.lower()
        # 처음에 이 경우를 생각을 안했다.
        # caccheSize 가 0 이면 miss 만 일어남.
        if cacheSize == 0:
            time += 5
            
        # 아니라면
        else:
            # hit
            if city in cache:
                # LRU 이기 때문에 그냥 삭제했다가 다시 넣었음.
                cache.remove(city)
                cache.append(city)
                time += 1
            # miss
            else:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(city)
                time += 5

    return time
