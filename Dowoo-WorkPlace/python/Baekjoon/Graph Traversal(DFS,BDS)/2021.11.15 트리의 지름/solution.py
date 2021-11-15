# https://www.acmicpc.net/problem/1967

# 문제요약
# 그장 길게 늘어나는 경우를 두 노드 사이의 경로의 길이를 트리의 지름이라고 함

# 입력
# 파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

# 출력
# 첫째 줄에 트리의 지름을 출력한다.

# 예제 입력 1 
# 12
# 1 2 3
# 1 3 2
# 2 4 5
# 3 5 11
# 3 6 9
# 4 7 1
# 4 8 7
# 5 9 15
# 5 10 4
# 6 11 6
# 6 12 10
# 예제 출력 1 
# 45

# 문제풀이

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
g = [[] for _ in range(N)]

# 노트연결
for i in range(N-1) :
    x,y,w =  map(int, input().split())
    g[x-1].append([w, y-1])
    g[y-1].append([w, x-1])

def bfs(x,mode) :
    q = deque()
    q.append(x)
    c = [-1] * N
    c[x] = 0

    while q:
        x = q.popleft()
        for w,nx in g[x] :
            if c[nx] == -1:
                c[nx] = c[x] + w
                q.append(nx)
    if mode == 1:
        return c.index(max(c)) # c가 가장 긴 곳은 찾아서 위치를 리턴
    else:
        return max(c) # 길이 리턴

print(bfs(bfs(0, 1), 2))

