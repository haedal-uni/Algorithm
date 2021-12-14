# My code (정답)
input()
num = map(int, input().split())
a=[]
for i in num :
    a.append(i)

result = max(a) * min(a)
if result <= 2 :
    result * result
print(result)




# Best code
input()
*a,=map(int,input().split())
print(max(a)*min(a))