'''
가장 큰 수
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다.
여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다.
▣ 입력설명
첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.
▣ 출력설명
가장 큰 수를 출력합니다.
▣ 입력예제 1
5276823 3
▣ 출력예제 1
7823
▣ 입력예제 2
9977252641 5
▣ 출력예제 2
99776
'''

#스택 관련 함수 구현.
def push(stack, element):
    stack.append(element)

def pop(stack):
    stack.pop()

def peek(stack):
    return stack[-1]

def empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False

#입력
n, m = input().split()
m = int(m)

stack = []
cnt = 0


for num in n:
    if empty(stack): #비어있을 때는 비교 없이 넣는다.
        push(stack, num)
    else:
        if int( peek(stack) ) >= int(num): #새로 넣는게 작으면 그냥 넣는다.
            # m개 제거 후에도 뒤에 숫자가 남아있으면 계속 들어가므로,
            # stack의 크기를 제한하는 조건을 붙인다.
            if len(stack) < len(n) - m:
                push(stack, num)
            else:
                break

        else: #새로 넣는게 크다면.
            while not empty(stack) and int(peek(stack)) < int(num):
                #스택에 들어있는 것 중 새로 넣으려는 것 보다 작은 것을
                if cnt < m:
                    pop(stack) #제거. 근데 m개 이상 제거는 안됨.
                else:
                    break

                cnt += 1

            if len(stack) < len(n) - m:
                push(stack, num)
            else:
                break

res = ""
for i in range(len(stack)):
    res += stack[i]

print(int(res))