def solution(participant, completion):
    
    # ������ �̸�, �������� ����
    Hash = {}
    
    for i in completion :
        if i in Hash :
            Hash[i] += 1
        else :
            Hash[i] = 1
    
    for j in participant :
        if j in Hash :
            if Hash[j] == 0 :
                answer = j
                break
            else :
                Hash[j] -= 1
        else :
            answer = j
            break
    
    return answer