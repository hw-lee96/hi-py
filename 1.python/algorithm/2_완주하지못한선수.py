# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(p, c):
    p_dict = {}
    answer = ''

    for pp in p:
        if p_dict.get(pp) == None:
            p_dict[pp] = 1
        else:
            p_dict[pp] += 1

    for cc in c:
        try:
            if cc in p_dict:
                p_dict[cc] -= 1
        except:
            answer = cc
            break
        
    if answer != '' : return answer

    for (pp, cnt) in p_dict.items():
        if cnt > 0 :
            answer = pp
            break

    return answer

import collections
def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion) # (1), (2)
    return list(answer.keys())[0] # (3)

print(solution2(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))