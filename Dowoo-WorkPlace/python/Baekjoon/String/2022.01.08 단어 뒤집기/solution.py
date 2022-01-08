# https://www.acmicpc.net/problem/9093

# 문제요약
# 단어를 뒤집어서 출력 단 순서는 그대로

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 단어와 단어 사이에는 공백이 하나 있다.

# 출력
# 각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.

# 예제 입력 1 
# 2
# I am happy today
# We want to win the first prize
# 예제 출력 1 
# I ma yppah yadot
# eW tnaw ot niw eht tsrif ezirp

# 문제요약
# 리스트 내에서 반전시켜서 출력!

T = int(input())

for _ in range(T) :
    S = list(map(str, input().split()))
    for i in range(len(S)) :
        S[i] = S[i][::-1]
    print(*S)


# lambda를 활용한 방법 
T = int(input())

for _ in range(T) :
    S = list(map(lambda x:x[::-1], input().split()))
    print(*S)