# https://www.acmicpc.net/problem/16234

# 문제요약
# 두  나라의 인구가 L이상 R이하라면 국경선을 연다
# 모두 열렸으면 인구이동을 시작
# 인접한 칸만 이동 그리고 그 하루동안 연합
# 인구수는 연합의 입구수/칸수 소수점은 버림
# 연합 해체 국경선 닫음

# 입력
# 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

# 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

# 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

# 출력
# 인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

# 예제 입력 1 
# 2 20 50
# 50 30
# 20 40
# 예제 출력 1 
# 1

# 문제풀이
# bfs로 푼다
# 조건이 많으므로 생각해야함

import sys
from collections import deque
input = sys.stdin.readline
# 숫자 받기
N,L,R = map(int, input().split()) 
g = [list(map(int, input().split())) for _ in range(N)]
# 방향
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
cnt = 0

def bfs(a,b) :
    q = deque()
    q.append((a,b))
    temp = [] # 연합리스트
    temp.append([a,b])

    while q :     
        x1,y1 = q.popleft()
        for i in range(4) :
            x = x1 + dx[i]
            y = y1 + dy[i]
            # 이동하고 방문전
            if 0 <= x < N and 0 <= y < N and visit[x][y] == 0 :
                if L <= abs(g[x][y]-g[x1][y1]) <= R:
                    visit[x][y] = 1 # 방문처리
                    q.append((x,y))
                    temp.append([x,y])
    return temp # 연합값 리턴

while True :
    visit = [[0]*N for _ in range(N)]
    isTrue = False # 전체 다 돌면 바꿔서 끝내기 위함
    for i in range(N) :
        for j in range(N) :
            if visit[i][j] == 0: # 방문 안했으면 함수실행
                visit[i][j] = 1
                temp = bfs(i,j)

                if len(temp) > 1:  # 연합이면 인구이동
                    isTrue = True
                    num = sum([g[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        g[x][y] = num
    if not isTrue: # 인구 이동 없으면 끝냄
        break
    cnt += 1

print(cnt)
