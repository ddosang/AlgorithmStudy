'''
후위표기식 만들기
중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있으면 중위표기식입니다.
후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식입니다.
예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면 (3+5)*2 이면 35+2* 로 바꾸어야 합니다.
※ 후위 표기식이 이해가 안되면 구글링으로 공부해보는 것도 좋습니다.
▣ 입력설명
첫 줄에 중위표기식이 주어진다. 길이는 100을 넘지 않는다.
식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
▣ 출력설명
후위표기식을 출력한다.
▣ 입력예제 1
3+5*2/(7-2)
▣ 출력예제 1
352*72-/+
▣ 입력예제 2
3*(5+2)-9
▣ 출력예제 2
352+*9-
'''


str = list(map(str, input()))
stack = []
res = ''
proirty = 0

def prior(ch):
    if ch == "+" or ch == "-":
        priority = 1
    elif ch == "*" or ch == "/":
        priority = 2
    elif ch == "(":
        priority = 3
    elif ch == ")":
        priority = 0

    return priority


for i in range(len(str)):

    if 48 <= ord(str[i]) <= 57: #숫자라면
        res += str[i]

    else:
        # top 보다 우선순위가 같거나 낮은게 들어오면
        # 들어온 것과 순위가 같거나 높은 것을 pop.
        # 대신 여는 괄호 전까지만 pop.
        if prior(stack[-1]) >= prior(str[i]):
            while stack and str[i] != "(" and prior(str[i]) <= prior(stack[-1]) :
                res += stack.pop()

        #닫는 괄호가 들어오면 여는 괄호 pop
        if str[i] ==')' and stack[-1] =='(':
            stack.pop()
        else: #()이 아닌 상황엔 스택에 push
            stack.append(str[i])

while stack:
    res += stack.pop()

print(res)



#강의방법

for x in str:
    if x.isdecimal():
        res += x
    else:
        if x=="(":
            stack.append(x)
        elif x =="*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
            # */보다 순위가 같거나 높은건 */니까.
                res += stack.pop()
            stack.append(x)
        elif x=="+" or x =="-":
            while stack and (stack[-1] != "("): #전부 다 빼면 되는데 (는 빼면 안됨.
                res += stack.pop()
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop() #( 도 빼버리기.
