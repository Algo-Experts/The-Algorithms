# https://www.acmicpc.net/problem/5014

# 문제요약
# 학원가는 엘베 최단거리 찾기

# 입력
# 첫째 줄에 F, S, G, U, D가 주어진다. (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 건물은 1층부터 시작하고, 가장 높은 층은 F층이다.

# 출력
# 첫째 줄에 강호가 S층에서 G층으로 가기 위해 눌러야 하는 버튼의 수의 최솟값을 출력한다. 만약, 엘리베이터로 이동할 수 없을 때는 "use the stairs"를 출력한다.

# 예제 입력 1 
# 10 1 10 2 1
# 예제 출력 1 
# 6
# 예제 입력 2 
# 100 2 1 1 0
# 예제 출력 2 
# use the stairs

# 문제풀이

import sys
from collections import deque
input = sys.stdin.readline

F,S,G,U,D = map(int, input().split())
arr = [-1] * F # 총 층수
dire = [U,-D] # 업다운 방향
arr[S-1] = 0 # 시작층 0으로 바꿔줌

def bfs(i):
    q = deque()
    q.append(i)
    visit = [0] * F
    visit[i] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dire[i]
            if 0 <= nx < F and visit[nx] == 0:
                q.append(nx)
                arr[nx] = arr[x] + 1
                visit[nx] = 1

bfs(S-1) # 시작층에서 시작
print(arr[G-1] if arr[G-1] != -1 else "use the stairs")

