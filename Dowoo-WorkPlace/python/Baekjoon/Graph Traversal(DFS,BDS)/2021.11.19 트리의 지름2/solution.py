# https://www.acmicpc.net/problem/1167

# 문제요약
# 트리의 긴 지름을 구하라

# 입력
# 트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. 정점 번호는 1부터 V까지 매겨져 있다.

# 먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

# 출력
# 첫째 줄에 트리의 지름을 출력한다.

# 예제 입력 1 
# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1
# 예제 출력 1 
# 11

# 문제풀이

import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
g = [[] for _ in range(V+1)]

for _ in range(V):
    a = list(map(int, input().split()))
    for i in range(1, len(a)-1, 2) :
        g[a[0]].append((a[i],a[i+1]))

def bfs(a) :
    visit = [-1] * (V+1)
    q = deque()
    q.append(a)
    visit[a] = 0
    m = [0,0]

    while q:
        old = q.popleft()
        for new in g[old] :
            if visit[new[0]] == -1 :
                visit[new[0]] = visit[old] + new[1]
                q.append(new[0])

                if m[0]<visit[new[0]] :
                    m[0] = visit[new[0]]
                    m[1] = new[0]
    return m

value, node = bfs(1)
res, node2  = bfs(node)
print(res)