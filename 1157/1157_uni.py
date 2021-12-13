# My code
word = input().lower()

def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l" ,"m" ,"n",
                      "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    max_occurrence = 0 # 최고로 많이 나왔던 횟수
    max_alphabet = alphabet_array[0] # 최고로 많이 나왔던 알파벳

    for alphabet in alphabet_array :
        occurrence = 0 # 초기 0으로 설정

        for char in string : # 문자열의 문자가
            if char == alphabet : # input으로 받은 값과 alphabet_array 비교
                occurrence +=1 # 1 증가

        if occurrence > max_occurrence :
            max_occurrence = occurrence
            max_alphabet = alphabet
        elif occurrence == max_occurrence : # 빈도 수 == 최대 빈도수
            max_alphabet="?" # 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력

    return max_alphabet

result = find_max_occurred_alphabet(word)
print(result.upper())




# Best code
n = input()
n = n.upper()
alpa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for i in alpa:
    result.append(n.count(i))
if result.count(max(result)) > 1:
    print("?")
else:
    print(alpa[result.index(max(result))])