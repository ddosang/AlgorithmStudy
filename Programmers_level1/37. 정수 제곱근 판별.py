import math

def solution(n):
    square = math.sqrt(n)
    if square == int(square):
        return math.pow(square + 1, 2)
    return -1
