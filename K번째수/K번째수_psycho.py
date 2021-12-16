# my code
def solution(array, commands):
    answer = []

    # 차근차근 확인해 가면서 푼 풀이
    for i in commands:
        first = array[(i[0]-1):i[1]]
        second = sorted(first)
        third = second[i[2]-1]
        answer.append(third)
        print("first = ", first)
        print("second = ", second)
        print("third = ", third)
    print(answer)
    # return answer

    # 불필요한 부분 줄인 코드
    for i in commands:
        answer.append((sorted(array[(i[0]-1):i[1]]))[i[2]-1])
    print(answer)
    # return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])


# best code
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
