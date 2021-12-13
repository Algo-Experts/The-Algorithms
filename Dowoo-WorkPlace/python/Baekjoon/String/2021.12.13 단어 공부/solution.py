# https://www.acmicpc.net/problem/1157

# 문제요약
# 가장 많이 사용된 알파벳을 찾아내기

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 예제 입력 1 
# Mississipi
# 예제 출력 1 
# ?
# 예제 입력 2 
# zZa
# 예제 출력 2 
# Z
# 예제 입력 3 
# z
# 예제 출력 3 
# Z
# 예제 입력 4 
# baaa
# 예제 출력 4 
# A

# 문제풀이
s = input().upper()
s_l = list(set(s)) # set을 사용하여 중복제거 문자열에 많이 쓰인다고함
cnt = [s.count(i) for i in s_l] 
print("?" if cnt.count(max(cnt))>1 else s_l[cnt.index(max(cnt))])