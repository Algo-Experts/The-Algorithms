# https://www.acmicpc.net/problem/10798

# 문제요약
# 세로로 읽고 글자가 없을 경우 그 다음줄을 읽는다

# 입력
# 총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다. 주어지는 글자는 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나이다. 각 줄의 시작과 마지막에 빈칸은 없다.

# 출력
# 영석이가 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다. 

# 예제 입력 1 
# ABCDE
# abcde
# 01234
# FGHIJ
# fghij
# 예제 출력 1 
# Aa0FfBb1GgCc2HhDd3IiEe4Jj
# 예제 입력 2 
# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx
# 예제 출력 2 
# Aa0aPAf985Bz1EhCz2W3D1gkD6x

# 문제풀이
# 문자열 문제에서 가장 많이 생각하게 한 문제
# 생각보다 어려웠다
# 길이가 딱 정해지지 않은점에서 신경써야했다


a = [] # 단어
l = [] # 길이
res = '' # 출력

for i in range(5) :
    s = input()
    a.append(s) # 단어추가
    l.append(len(s)) # 길이추가

for i in range(max(l)) : # 최대길이로 돌림 0번째 시작
    for j in range(5) : # 5줄이므로
        if i < l[j] : # 즉 해당 길이 까지만!
            res += a[j][i] # res에 더해준다
print(res)