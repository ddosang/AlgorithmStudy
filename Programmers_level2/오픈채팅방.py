# https://programmers.co.kr/learn/courses/30/lessons/42888

import re

def solution(record):
    answer = []
    table = {} # uid 를 key 로 하여 이름을 저장.
    organizedRecord = [] # uid, enter/leave 로그를 저장.
    
    
    # 처음에는 정규표현식을 써서 형식별로 문자열을 처리하려고 했는데
    # uidFormat = re.complie('uid[A-Za-z0-9]+')
    # nameFormat = re.compile('[A-Za-z0-9]+')
    
    for sentence in record:
        # info = nameFormat.findall(sentence)
        # 하고보니 그냥 split 하면... 되네..?
        # leave 인 경우 name 이 없으므로 name은 안쪽에서 처리했다.
        info = sentence.split(' ')
        behavior = info[0]
        uid = info[1]
        
        # 동작에 따라 처리.
        if behavior == 'Enter':
            name = info[2]
            table[uid] = name
            organizedRecord.append([uid, behavior])
        elif behavior == 'Leave':
            organizedRecord.append([uid, behavior])
        else:
            name = info[2]
            table[uid] = name

    
    # uid, behavior 순으로 저장해뒀으므로
    # uid, table[uid], behavior 를 찍어주면 됨.
    for (uid, behavior) in organizedRecord:
        behaviorString = "들어왔습니다." if behavior == 'Enter' else "나갔습니다."
        answer.append(table[uid]+"님이 "+behaviorString)
        

    return answer
