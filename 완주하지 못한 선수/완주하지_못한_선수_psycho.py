#  remove는 리스트를 전부 탐색하는 것이어서 시간 복잡도가 오래걸린다고 한다.

# my code
def solution(participant, completion):
    # 통과 ( 방법 조금 참고 )
    participant.sort()
    completion.sort()
    completion.append("0")
    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer

    # 효율성 문제 발생
    for i in completion:
        participant.remove(i)
    answer = participant[0]
    return answer

# best code
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
