n, m = input().split()
m = int(m)

nums = list(map(int, str(n)))
answer = ""

stack = []

count = 0
for num in nums:
    # 지금 들어간 것보다 작은걸 다 제거한다.
    # 근데 그럼 전부 다 없어지잖아..? -> m 이라는 길이가 유지는 될 때 까지.
    while stack and m > 0 and stack[-1] < num:
        stack.pop()
        m -= 1

    # 스택에 넣고.
    stack.append(num)

if m != 0:
    stack = stack[:-m]

answer = ''.join(map(str, stack))
print(answer)

# 5276823 3
# 9977252641 5
