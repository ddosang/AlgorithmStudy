import sys
readl = sys.stdin.readline

def alphabetToInt(c):
    return ord(c) - ord('A') + 1

def intToAlphabet(num):
    return chr(num + ord('A') - 1)

def checkMagicStar():
    global lines, star
    for i in range(6):
        sum = 0
        for dot in lines[i]:
            sum += star[dot[0]][dot[1]]
        if sum != 26:
            return False
    return True

            

def DFS(level, idx):
    global min_str


    if level == x_cnt:
        if checkMagicStar():
            for i in range(5):
                for j in range(9):
                    if type(star[i][j]) == type(1):
                        print(intToAlphabet(star[i][j]), end='')
                    else:
                        print(star[i][j], end='')
                print()
            exit(0)
        return
    
    # 처음 x 자리부터 알파벳을 전부 넣어보고,
    # 합이 26이 되는지를 체크
    for i in range(1, 13):
        if ch[i] == 0:
            ch[i] = 1
            star[xarr[idx][0]][xarr[idx][1]] = i
            DFS(level + 1, idx + 1)
            star[xarr[idx][0]][xarr[idx][1]] = 'x'
            ch[i] = 0


#            (0, 4)
# (1, 1) (1, 3) (1, 5), (1, 7)
#    (2, 2)         (2, 6)
# (3, 1) (3, 3), (3, 5), (3, 7)  
#            (4, 4)

# (0, 4) 기준 왼쪽 대각선 1, 오른쪽 대각선 2
# (1, 1) 대각선 3, (1, 1) 가로 4, (1, 7) 대각선 5
# (3, 1) 가로 6

    
first = [(0, 4), (1, 3), (2, 2), (3, 1)]
second = [(0, 4), (1, 5), (2, 6), (3, 7)]
third = [(1, 1), (1, 3), (1, 5), (1, 7)]
fourth = [(3, 1), (3, 3), (3, 5), (3, 7)]
fifth = [(1, 7), (2, 6), (3, 5), (4, 4)]
sixth = [(3, 1), (3, 3), (3, 5), (3, 7)]
lines = [first] + [second] + [third] + [fourth] + [fifth] + [sixth]


star = [[alphabetToInt(c) if c != 'x' and c != '.' else c for c in readl().strip()] for _ in range(5)]

# x 자리를 가지고 있음.
xarr = []

ch = [0] * 13
x_cnt = 0
for i in range(5):
    for j in range(9):
        if type(star[i][j]) == type(1):
            ch[star[i][j]] = 1

        if star[i][j] == 'x':
            xarr.append((i, j))
            x_cnt += 1 


min_str = 'Z' * x_cnt

DFS(0, 0)