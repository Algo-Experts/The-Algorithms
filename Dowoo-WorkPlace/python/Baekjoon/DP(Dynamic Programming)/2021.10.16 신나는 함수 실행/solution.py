# https://www.acmicpc.net/problem/9184

# 문제요약
# 재귀함수 w(a,b,c)가 있는데 식이 너무 길어서 오래걸림
# 출력프로그램을 다시 만들기!

# 입력
# 입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

# 출력
# 입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

# 제한
# -50 ≤ a, b, c ≤ 50
# 예제 입력 1 
# 1 1 1
# 2 2 2
# 10 4 6
# 50 50 50
# -1 7 18
# -1 -1 -1
# 예제 출력 1 
# w(1, 1, 1) = 2
# w(2, 2, 2) = 4
# w(10, 4, 6) = 523
# w(50, 50, 50) = 1048576
# w(-1, 7, 18) = 1

# 문제풀이
# 재귀함수를 dp에 저장해서 푸는 방법이다!
# 범위가 정해져 있기 때문에 그 값을 저장해서 쓰는것!
# 어찌보면 이런 문제가 쉬운 문제임.
# 답을 다 알려줌

import sys

def w(a,b,c) :
    # 문제에 있는 내용들
    if a<=0 or b<=0 or c<=0 :
        return 1

    if a > 20 or b > 20 or c > 20 : 
        return w(20, 20, 20) 

    # 값이 있을 경우 그 값을 리턴
    if dp[a][b][c] : 
        return dp[a][b][c] 

    # 문제에 있는 내용들
    if a<b<c : 
        dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a, b-1, c)
        return dp[a][b][c] 

    dp[a][b][c] = w(a-1, b, c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1) 
    return dp[a][b][c] 

# 20이상이면 20으로 만들기 때문에 20까지
dp = [[[0]*(21) for _ in range(21)] for _ in range(21)] 

while True :
    a,b,c = map(int, sys.stdin.readline().split())
    
    if a == b == c == -1 : # 이 값이 주어질 경우 스톱
        break

    print("w(%d, %d, %d) = %d" %(a, b, c, w(a, b, c)))