# https://www.acmicpc.net/problem/2644

# 문제요약
# 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하라

# 입력
# 사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.

# 각 사람의 부모는 최대 한 명만 주어진다.

# 출력
# 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

# 예제 입력 1 
# 9
# 7 3
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6
# 예제 출력 1 
# 3
# 예제 입력 2 
# 9
# 8 6
# 7
# 1 2
# 1 3
# 2 7
# 2 8
# 2 9
# 4 5
# 4 6
# 예제 출력 2 
# -1

# 문제풀이
# BFS DFS 상관없지만 BFS로 계산

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
S,E = map(int, input().split())
M = int(input())
g = [[] for _ in range(N+1)]
r = [0 for _ in range(N+1)]
for _ in range(M) :
    x,y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def bfs(a) :
    q = deque()
    q.append(a)
    v = [0 for _ in range(N+1)]
    v[a] = 1

    while q:
        b = q.popleft()
        for i in g[b] :
            if v[i] == 0 :
                v[i] = 1
                r[i] =r[b] + 1
                q.append(i)
bfs(S)

print(r[E] if r[E] != 0 else -1)
                
    

    