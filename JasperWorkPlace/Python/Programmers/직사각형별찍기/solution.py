

# 입력값 받는 부분을 집중 해서 보자!! @@@@@
a, b = map(int, input().strip().split(' '))


answer = ""

for column in range(a):
    answer += "*"

print((answer + "\n") * b)
