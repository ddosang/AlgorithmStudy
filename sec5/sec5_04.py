'''
후위식 연산
후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.
▣ 입력설명
첫 줄에 후위연산식이 주어집니다. 연산식의 길이는 50을 넘지 않습니다.
식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
▣ 출력설명
연산한 결과를 출력합니다.
▣ 입력예제 1
352+*9-
▣ 출력예제 1
12
'''


def calculate(cal, a, b):
    if cal == "+":
        return a+b
    elif cal == "-":
        return a-b
    elif cal == "*":
        return a*b
    elif cal == "/":
        return a/b


str = list(map(str, input()))
stack = []
res = ''
proirty = 0


for i in range(len(str)):
    stack.append(str[i])
    if 48 > ord(str[i]) or ord(str[i]) > 57: #숫자가 아니라면
        cal = stack.pop()
        b, a = stack.pop(), stack.pop() #숫자 숫자 연산자를 뽑아서
        a, b = int(a), int(b)

        res = calculate(cal, a, b)
        stack.append(res) #연산을 하고 다시 stack에 넣는다.

    print(stack)

print(stack.pop())
