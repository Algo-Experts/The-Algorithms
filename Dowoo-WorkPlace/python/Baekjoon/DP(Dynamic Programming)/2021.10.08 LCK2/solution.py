# https://www.acmicpc.net/problem/9252

# 문제요약 
# 두 문자열이 주어졌을때 가장 긴것을 찾는 문제

# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

# 출력
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

# LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.

# 예제 입력 1 
# ACAYKP
# CAPCAK
# 예제 출력 1 
# 4
# ACAK

# 문제풀이
# LCS문제와 다른점이 있다면 길이도 찾고 문장도 찾아야함
# max를 써서 해보려고 했으나 불가능! 고민끝에 그냥 if문 사용

import sys
A= sys.stdin.readline().strip()
B= sys.stdin.readline().strip()
lA = len(A)
lB = len(B)
dp = [[""]*(lA+1) for _ in range(lB+1)]


for i in range(1,lB+1) :
    for j in range(1,lA+1) :
        if B[i-1] == A[j-1] :
            dp[i][j] = dp[i-1][j-1] + A[j-1] # 같을경우 값을 더해줌!
        else :
            if len(dp[i][j-1]) < len(dp[i-1][j]) : # 큰 값을 넣기위함
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i][j-1]


print(len(dp[-1][-1]))
print(dp[-1][-1])