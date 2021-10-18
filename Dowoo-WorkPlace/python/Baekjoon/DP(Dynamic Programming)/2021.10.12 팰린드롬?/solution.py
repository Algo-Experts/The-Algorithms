# https://www.acmicpc.net/problem/10942

# 문제요약
# 팰린드롬이란 짝수개일때 반으로 좌우가 같은경우
# 홀수가개일때 중앙값을 기준으로 좌우가 같아야한다.
# S~N까지 주어질경우 맞으면 1 아니면 0을 출력

# 입력
# 첫째 줄에 수열의 크기 N (1 ≤ N ≤ 2,000)이 주어진다.
# 둘째 줄에는 홍준이가 칠판에 적은 수 N개가 순서대로 주어진다. 칠판에 적은 수는 100,000보다 작거나 같은 자연수이다.
# 셋째 줄에는 홍준이가 한 질문의 개수 M (1 ≤ M ≤ 1,000,000)이 주어진다.
# 넷째 줄부터 M개의 줄에는 홍준이가 명우에게 한 질문 S와 E가 한 줄에 하나씩 주어진다.

# 출력
# 총 M개의 줄에 걸쳐 홍준이의 질문에 대한 명우의 답을 입력으로 주어진 순서에 따라서 출력한다. 팰린드롬인 경우에는 1, 아닌 경우에는 0을 출력한다.

# 예제 입력 1 
# 7
# 1 2 1 3 1 2 1
# 4
# 1 3
# 2 5
# 3 3
# 5 7
# 예제 출력 1 
# 1
# 0
# 1
# 1

# 문제풀이

import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp=[[0]* N for _ in range(N)]

for i in range(N) : # i는 길이라고 보면됨
    for S in range(N-i) :
        E = S + i # S는 시작 E는 끝
        
        if S == E : #시작과 끝이 같음 즉 길이가 1일경우 
            dp[S][E] = 1 
        
        elif arr[S] == arr[E] : # 양끝의 숫자가 같은경우
            if S+1 == E: # 길이가 2일경우
                dp[S][E] = 1
            elif dp[S+1][E-1] == 1: # 길이가 3이상이면서 같으면
                dp[S][E] = 1

M = int(sys.stdin.readline())

for i in range(M) : # 결과값 출력
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])

