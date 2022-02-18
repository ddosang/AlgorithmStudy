from functools import reduce

def solution(arr):
    return reduce(lambda x, y: x + y, arr) / len(arr)
