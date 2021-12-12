# https://www.acmicpc.net/problem/2675

# 문제요약
# 문자열을 받고 N번 반복해서 출력하기

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

# 예제 입력 1 
# 2
# 3 ABC
# 5 /HTP
# 예제 출력 1 
# AAABBBCCC
# /////HHHHHTTTTTPPPPP

# 문제풀이
T = int(input())
for _ in range(T) :
    R,S=  input().split()
    res = ""
    for i in S :
        res += int(R)*i
    print(res)
