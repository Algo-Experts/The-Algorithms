# https://www.acmicpc.net/problem/2458

# 문제요약
# 키비교한 결과값이 주어질때 자신의 키가 몇번째인지 알수 있는 학생들은 모두 몇명인가?

# 입력
# 첫째 줄에 학생들의 수 N (2 ≤ N ≤ 500)과 두 학생 키를 비교한 횟수 M (0 ≤ M ≤ N(N-1)/2)이 주어진다. 다음 M개의 각 줄에는 두 학생의 키를 비교한 결과를 나타내는 두 양의 정수 a와 b가 주어진다. 이는 번호가 a인 학생이 번호가 b인 학생보다 키가 작은 것을 의미한다. 

# 출력
# 자신이 키가 몇 번째인지 알 수 있는 학생이 모두 몇 명인지를 출력한다. 

# 예제 입력 1 
# 6 6
# 1 5
# 3 4
# 5 4
# 4 2
# 4 6
# 5 2
# 예제 출력 1 
# 1
# 예제 입력 2 
# 6 7
# 1 3
# 1 5
# 3 4
# 5 4
# 4 2
# 4 6
# 5 2
# 예제 출력 2 
# 2
# 예제 입력 3 
# 6 3
# 1 2
# 2 3
# 4 5
# 예제 출력 3 
# 0

# 문제풀이
# 처음에 어떻게 풀어야할지 막막했다 
# 플로이드 마셜 구현문제라고한다
# 플로이드 마셜이란 모든 노드에 대한 모든 노드의 최단거리를 구하는 알고리즘이다

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
g = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    p, c = map(int, input().split())
    g[p-1][c-1] =1 # 값넣어줌

# 플로이드 와샬 알고리즘 - 이동가능한 경로를 모두 구한다.
for i in range(N): # 경로로 or문의 가장 상위단계여야함 
    for row in range(N):
        for col in range(N):
            if g[row][i] + g[i][col]  == 2:
                g[row][col] =1 

cnt =[0 for i in range(N)]
for i in range(N):
    for j in range(N): # i에서 j로 이동할 수 있드면 값을 증가시켜준다 
        if g[i][j] ==1:
            cnt[i] +=1
            cnt[j] +=1

print(cnt.count(N-1))