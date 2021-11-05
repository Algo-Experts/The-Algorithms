# https://www.acmicpc.net/problem/1260

# 문제요약
# DFS와 BFS로 탐색한 결과를 출력하는 프로그램을 작성

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1 
# 1 2 4 3
# 1 2 3 4
# 예제 입력 2 
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1
# 예제 출력 2 
# 3 1 2 5 4
# 3 1 4 2 5
# 예제 입력 3 
# 1000 1 1000
# 999 1000
# 예제 출력 3 
# 1000 999
# 1000 999

# 문제풀이
# 처음 접한 유형이므로 찾아봄!
# 아직 이해 불가능 오늘 계속 찾아보고 이해해야 할 것 같음.. 
# DFS : 깊이 우선 탐색 - 보통 재귀
# 장점 - 현 경로상의 노드를 기억 적은 메모리사용 / BFS보다 빠름 
# 단점 - 해가 없는 경로를 탐색할 경우 단계가 끝날 때 까지 탐색 / 최단경로 보장이 없음

# BFS : 넓이 우선 탐색 - 보통 큐나 데크에 저장하면서 찾아감
# 장점 - 답이 되는 경로가 여러개인 경우에도 최단 경로 보장 / 최단 경로가 존재하면 깊이가 무한정 깊어도 답을 찾을 수 있음
# 단점 - 경로가 길경우 많은 기억공간 필요 / 해가 없을 경우 탐색은 실패 / 무한 그래프의 경우 해를 찾지도 못하고 끝남



import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  m1, m2 = map(int, input().split())
  graph[m1][m2] = graph[m2][m1] = 1 # 양방향 노드연결

def bfs(v): # 넓이 우선 탐색
  discoverd = [v] 
  q = deque() 
  q.append(v)

  while q:
    v = q.popleft()
    print(v, end=' ')

    for w in range(len(graph[v])):
      if graph[v][w] == 1 and (w not in discoverd):
        discoverd.append(w)
        q.append(w)

def dfs(v, discoverd=[]): # 깊이 우선 탐색
  discoverd.append(v)
  print(v, end=' ')

  for w in range(len(graph[v])):
    if graph[v][w] == 1 and (w not in discoverd):
      dfs(w, discoverd)

dfs(V)
print()
bfs(V)
