# https://www.acmicpc.net/problem/11724

# 방향없는 그래프가 주어졌을 때 연결요소의 갯수를 구하는것

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# 예제 입력 1 
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 예제 출력 1 
# 2
# 예제 입력 2 
# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3
# 예제 출력 2 
# 1

# 문제풀이
# 덩어리가 몇개인지 찾는 문제임
# 뭘로 풀어도 상관은 없으나 DFS로 풀어버림
# 속도 때문에 sys랑 deque사용해야함

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
g = [[] for _ in range(N+1)]
visit = [0]*(N+1) #방문한거 체크
cnt = 0

for _ in range(M) : # 입력된거 추가함
    a,b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

def bfs(v): 
    q = deque()
    q.append(v)

    while(q):
        x = q.popleft()
        for i in g[x]: # 순번대로
            if visit[i] == 0: # 방문 안했을경우
                q.append(i)
                visit[i] = 1


for i in range(1,N+1) :
    if visit[i] == 0 : # 방문없을경우
        bfs(i) # 메소드실행
        cnt += 1 # 횟수 1추가

print(cnt)
