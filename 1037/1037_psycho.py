# 문제
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다.
# 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.
# -> N >= 50, N = 자연수
# 2 <= 약수 <= 1,000,000

# 출력
# 첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.
# -> 32비트로 변환?

# my code (미완성 -> 추가 수정 후 완성(모험가꺼 참고함))
from sys import stdin

input_word = int(stdin.readline())  # input이랑 같은 역할 단, import를 해줘야 한다.
aliquot_list = list(map(int, stdin.readline().split()))
aliquot_list.sort()
if input_word <= 1:
    print(aliquot_list[0] * aliquot_list[0])
else:
    print(aliquot_list[0] * aliquot_list[-1])


# Best code
input()
n = sorted(map(int, input().split()))
print(n[-1]*n[0])