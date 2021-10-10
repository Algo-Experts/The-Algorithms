# https://www.acmicpc.net/problem/11066

# 문제요약
# 소설을 각각 파일로 나눔
# 합칠때마다 비용이 있다. 40 30 30 50일 경우
# 1,2번을 합치면 70이고 3,4을 합치면 80이다.
# 이 둘을 합치면 150이다.
# 전체금액은 70+80+150이 나오는데 금액의 최소값을 구하라!

# 입력
# 프로그램은 표준 입력에서 입력 데이터를 받는다. 프로그램의 입력은 T개의 테스트 데이터로 이루어져 있는데, T는 입력의 맨 첫 줄에 주어진다.각 테스트 데이터는 두 개의 행으로 주어지는데, 첫 행에는 소설을 구성하는 장의 수를 나타내는 양의 정수 K (3 ≤ K ≤ 500)가 주어진다. 두 번째 행에는 1장부터 K장까지 수록한 파일의 크기를 나타내는 양의 정수 K개가 주어진다. 파일의 크기는 10,000을 초과하지 않는다.

# 출력
# 프로그램은 표준 출력에 출력한다. 각 테스트 데이터마다 정확히 한 행에 출력하는데, 모든 장을 합치는데 필요한 최소비용을 출력한다.

# 예제 입력 1 
# 2
# 4
# 40 30 30 50
# 15
# 1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
# 예제 출력 1 
# 300
# 864

# 문제풀이
# 처음에 쉬운줄 알았는데 너무나도 어려운 문제였다.
# 중요한건 소설이기 때문에 인접한 파일만 합칠 수 있다.
# 해설을 다시 봐도 어렵다...

import sys 

input = sys.stdin.readline 

for _ in range(int(input())):
    N = int(input())
    files = list(map(int, input().split()))    
    dp = [[0]*N for _ in range(N)]

    # dp[i][j] : i번째부터 j번째 장까지 합쳤을 때의 단순 합계
    for i in range(N-1): 
        dp[i][i+1] = files[i] + files[i+1]
        for j in range(i+2, N):
            dp[i][j] = dp[i][j-1]  + files[j] 

    # dp[i][j] : i번째부터 j번째 장까지 합쳤을 때 가능한 누적 비용의 최소값
    # (i~k까지 더한 비용의 최솟값) + (k+1~j까지 더한 비용의 최솟값)들의 최소값을 순차적으로 dp에 더하기
    for unit in range(2, N): 
        for i in range(N-unit): # (0, 2) (1, 3) (2, 4) ... | (0, 3) (1, 4) (2, 5) ... 
            j = i+unit # i번째부터 j번째 장까지의 누적 비용
            additional = []
            for k in range(i, j):
                additional.append(dp[i][k]+dp[k+1][j])
            dp[i][j] += min(additional)

    print(dp[0][N-1]) # 0~N-1번째 장까지의 누적 비용의 최소값

    