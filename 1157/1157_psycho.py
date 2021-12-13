# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이
# 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.



# my code (미완성)

from sys import stdin

input_word = stdin.readline()  # input이랑 같은 역할 단, import를 해줘야 한다.
upper_word = input_word.upper()  # 대문자로 변환
set_word = set(upper_word)  # 문자 겹치는 거 방지

list = {} # count 기록 하기 위한 딕셔너리

for i in set_word:
    first_word = i
    word_count = upper_word.count(first_word)  # 들어온 값을 세어준다.
    list[first_word] = word_count  # 딕셔너리에 갯수 파악한것 넣어주기

del list['\n']
print(set_word)
print(list)



# Best code

str_input = input().upper()
count_list = [0] * 26
for char in str_input:
    idx = ord(char) - ord('A')
    count_list[idx] += 1
count = 0
for n in count_list:
    if n == max(count_list):
        count += 1
if count > 1:
    print('?')
else:
    for i in range(len(count_list)):
        if count_list[i] == max(count_list):
            print(chr(i + ord('A')))