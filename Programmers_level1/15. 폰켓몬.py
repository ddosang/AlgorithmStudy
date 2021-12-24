def solution(nums):
    # 뽑을 수 있는 포켓몬 수 저장
    pokemon_count = len(nums) / 2
    # 포켓몬 종류만 남김!
    pokemon = list(set(nums))
    
    # 뽑을 수 있는 포켓몬 수보다 포켓몬 종류가 많으면
    # 다 다른 포켓몬을 뽑으면 되니까 뽑을 수 있는 포켓몬 수가 종류 최대.
    # 아니면 있는 포켓몬 종류를 다 뽑는게 최대.
    if (len(pokemon) >= pokemon_count):
        return pokemon_count
    else:
        return len(pokemon)
