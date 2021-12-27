# https://www.acmicpc.net/problem/1032

# 문제요약
# 검색결과가 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지 출력하는 문제이다
# 패턴에는 .과 ?만 넣을 수 있고 가능하면 ?는 적게 써야한다

# 입력
# 첫째 줄에 파일 이름의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에는 파일 이름이 주어진다. N은 50보다 작거나 같은 자연수이고 파일 이름의 길이는 모두 같고 길이는 최대 50이다. 파일이름은 알파벳 소문자와 '.' 로만 이루어져 있다.

# 출력
# 첫째 줄에 패턴을 출력하면 된다.

# 예제 입력 1 
# 3
# config.sys
# config.inf
# configures
# 예제 출력 1 
# config????
# 예제 입력 2 
# 2
# contest.txt
# context.txt
# 예제 출력 2 
# conte?t.txt
# 예제 입력 3 
# 3
# c.user.mike.programs
# c.user.nike.programs
# c.user.rice.programs
# 예제 출력 3 
# c.user.?i?e.programs
# 예제 입력 4 
# 4
# a
# a
# b
# b
# 예제 출력 4 
# ?
# 예제 입력 5 
# 1
# onlyonefile
# 예제 출력 5 
# onlyonefile

# 문제풀이
N = int(input()) 
a = list(input()) # 처음에 받는 파일 이름명

for i in range(N-1) : # 그 다음부터
    b = list(input())
    for j in range(len(a)) :
        if a[j] != b[j] : # 다를경우엔 처음 받은 이름을 변경시켜줌
            a[j] ='?'
print(*a,sep="")
