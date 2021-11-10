# https://www.acmicpc.net/problem/1389

# 문제요약
# 임의의 두 사람이 최소 몇 단계만에 이어질 수 있는지 계산하는 게임
# 케빈 베이컨의 수가 가장 작은 사람을 구하라

# 입력
# 첫째 줄에 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)이 주어진다. 둘째 줄부터 M개의 줄에는 친구 관계가 주어진다. 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다. A와 B가 친구이면, B와 A도 친구이며, A와 B가 같은 경우는 없다. 친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다. 또, 모든 사람은 친구 관계로 연결되어져 있다. 사람의 번호는 1부터 N까지이며, 두 사람이 같은 번호를 갖는 경우는 없다.

# 출력
# 첫째 줄에 BOJ의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력한다. 그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력한다.

# 예제 입력 1 
# 5 5
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2
# 예제 출력 1 
# 3

# 문제풀이
# 최소를 구해야하므로 BFS로 풀어본다.
# 어려운 문제는 아니었으나 index값을 찾아서 보여주는 점에서
# 결과값을 찾는데 시간을 투자했다.

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
g = [[]for _ in range(N+1)]
res = []

for _ in range(M) :
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(a) :
    v = [0] * (N+1) # 방문 
    num = [0] * (N+1) # 몇번째
    q = deque()
    v[a] = 1
    q.append(a)
    while q: 
        x = q.popleft()
        for i in g[x] :
            if v[i] == 0 :
                num[i] = num[x]+1 # +1씩 해줌
                v[i] = 1
                q.append(i)
    return sum(num)

for i in range(1, N+1) :
    res.append(bfs(i))

print(res.index(min(res))+1) # 몇 번째인지 알아야 하기 떄문에 인덱스 값을 알아야하고 거기에 +1





