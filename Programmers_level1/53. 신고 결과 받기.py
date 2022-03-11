def solution(id_list, report, k):
    answer = []
    count_dict = {}
    mail_dict = {}
    reporter_dict = {}
    
    report = list(set(report))
    
    for user_id in id_list:
        count_dict[user_id] = 0
        mail_dict[user_id] = 0
        reporter_dict[user_id] = []
        
        
    for r in report:
        [reporter, bad_guy] = r.split(' ')
        count_dict[bad_guy] += 1
        reporter_dict[bad_guy] += [reporter]
    
    
    for bad_guy in count_dict:
        if count_dict[bad_guy] >= k:
            for reporter in reporter_dict[bad_guy]:
                mail_dict[reporter] += 1
            
    for user_id in id_list:
        answer.append(mail_dict[user_id])
    
    return answer
