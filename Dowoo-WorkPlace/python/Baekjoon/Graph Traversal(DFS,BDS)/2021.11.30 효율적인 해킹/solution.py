# https://www.acmicpc.net/problem/1325

# 문제요약
# 여러대의 컴퓨터를 해킹하는데
# 신뢰하는 관계가 주어질경우 한번에 가장 많은 컴퓨터를 해킹할 수 있는 번호를 출력

# 입력
# 첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

# 출력
# 첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

# 예제 입력 1 
# 5 4
# 3 1
# 3 2
# 4 3
# 5 3
# 예제 출력 1 
# 1 2

# 문제풀이

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for i in range(n + 1)]
# 서로 연결시켜줌
for i in range(m):
    a, b = map(int, input().split())
    g[b].append(a)

res = [] # 결과값저장
max_cnt = 0

def bfs(a):
    q = deque()
    q.append(a)
    visit = [0] * (n+1)
    visit[a] = 1
    cnt = 1
    while q:
        a1 = q.popleft()
        for i in g[a1]:
            if visit[i] == 0:
                visit[i] = 1
                cnt += 1
                q.append(i)
    return cnt # 갯수 리턴

for i in range(1, n+1):
    tmp = bfs(i)
    if max_cnt == tmp:
        res.append(i) # 최대값이랑 같은 경우도 저장
    if max_cnt < tmp:
        max_cnt = tmp # 최대값으로 저장
        res.append(i)

print(*res)