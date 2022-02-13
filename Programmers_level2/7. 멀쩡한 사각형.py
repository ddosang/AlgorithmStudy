def maxDivisor(a, b):
    if b == 0:
        return a
    return maxDivisor(b, a%b)

def solution(w,h):
    if w < h:
        w, h = h, w
    maxD = maxDivisor(w, h)
    trash = (h / maxD) + (w / maxD) - 1
    return w*h - maxD * trash
