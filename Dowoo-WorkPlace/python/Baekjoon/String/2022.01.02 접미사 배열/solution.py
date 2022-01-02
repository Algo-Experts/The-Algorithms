# https://www.acmicpc.net/problem/11656

# 문제요약
# 앞에서부터 하나씩 제외함
# 사전순으로 출력

# 입력
# 첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

# 출력
# 첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# baekjoon
# 예제 출력 1 
# aekjoon
# baekjoon
# ekjoon
# joon
# kjoon
# n
# on
# oon

# 문제풀이

S = input()
a = []

for i in range(len(S)) : # 값 넣어주고
    a.append(S[i:])

a.sort() # 정렬

for i in range(len(S)) : # 출력
    print(a[i])

# 한줄코딩!
S = input()
print(*sorted(S[i:] for i in range(len(S))))