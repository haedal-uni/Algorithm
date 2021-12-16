answer = []
def solution(array, commands):
    for i in range(len(commands)) :
            a = commands[i][0]
            b = commands[i][1]
            c = commands[i][2]
            answer.append(sorted(array[a-1:b])[c-1])
    return answer
