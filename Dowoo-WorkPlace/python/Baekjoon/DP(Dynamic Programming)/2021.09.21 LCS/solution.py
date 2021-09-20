# https://www.acmicpc.net/problem/9251

# 문제요약
# 두 수열이 주어졌을 때 가장 긴 수열을 구하라!

# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

# 출력
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

# 예제 입력 1 
# ACAYKP
# CAPCAK
# 예제 출력 1 
# 4

# 문제풀이
# .strip() 이거 때문인지 계속 틀리게 나옴.
# 고치고 나니 완료됨.
# 같은 문자가 나오면 1을 추가해주는 식으로 풀이해야함

import sys

A = sys.stdin.readline().strip().upper()
B = sys.stdin.readline().strip().upper()

# dp값에 0채움
dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]


for i in range(1,len(B)+1) :
    for j in range(1,len(A)+1) :
        if B[i-1] == A[j-1] :
            dp[i][j] = dp[i-1][j-1] +1 # 같은경우 +1값을 줌
        else : 
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            # 다를 경우 검색하는 이전문자 또는 확인하는 이전문자의 같은 문자중 큰수
            # 즉 이전과 같게 만드는 것! 

print(dp[-1][-1])