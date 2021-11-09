# https://www.acmicpc.net/problem/1707

# 문제요약
# 그래프의 정점의 집합을 둘로 분할하여,
# 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을때,
# 그래프를 특별히 이분 그래피라고 함
# 판별하라!

# 입력
# 입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다. 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다. 

# 출력
# K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

# 제한
# 2 ≤ K ≤ 5
# 1 ≤ V ≤ 20,000
# 1 ≤ E ≤ 200,000
# 예제 입력 1 
# 2
# 3 2
# 1 3
# 2 3
# 4 4
# 1 2
# 2 3
# 3 4
# 4 2
# 예제 출력 1 
# YES
# NO

# 문제풀이
# BFS로 문제풀이
# 그래프가 만들어지는지 확인

import sys
from collections import deque
input = sys.stdin.readline
K = int(input())

def bfs(a) :
    vi[a] = 1 # 방문
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        for i in g[x] : # 존재할경우 
            if vi[i] == 0 : 
                vi[i] = -vi[x]
                q.append(i)
            else:
                if vi[i] == vi[x] : # 같으면
                    return 0
    return 1

for _ in range(K) :
    V, E = map(int, input().split())
    res = 1 # 결과값저장 0 실패 1성공
    g = [[] for _ in range(V+1)] # 그래프
    vi  = [0 for i in range(V+1)] # 방문
    for _ in range(E) : # 서로연결시켜줌
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    for i in range(1, V+1) : # 1번은 1번이므로!
        if vi[i] == 0 : #방문 0이면
            if not bfs(i) : # 포함 안되면
                res = 0 # 실패
                break
    print("YES" if res==1 else "NO") 





