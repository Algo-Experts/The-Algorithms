# https://www.acmicpc.net/problem/7562

# 문제요약
# 나이트는 몇번 움직이면 이 칸으로 이동가능한가

# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

# 예제 입력 1 
# 3
# 8
# 0 0
# 7 0
# 100
# 0 0
# 30 50
# 10
# 1 1
# 1 1
# 예제 출력 1 
# 5
# 28
# 0

# 문제풀이
# 최소를 알아야 하기 떄문에 BFS로 푼다
# dp에서도 비슷한 문제있었는데 이걸 풀생각하면 끔찍함
# 그래프는 확실히 한번 이해만 하면 거의 비슷해서 알겠음

import sys
from collections import deque
input = sys.stdin.readline #input을 다시 정의내림

def bfs(s1,s2,e1,e2) :
    q = deque()
    q.append((s1,s2))
    v[s1][s2] = 1 # 방문함

    while q :     
        x1,y1 = q.popleft()

        if x1 == e1 and y1 ==e2 : # 도착했으면 끝!
            print(v[e1][e2]-1)
            return

        for i in range(8) :
            x = x1 + dx[i]
            y = y1 + dy[i]

            if 0 <= x <N and 0<= y < N and v[x][y] == 0: 
                q.append((x,y))
                v[x][y] = v[x1][y1]+1 # 이전값에 +1함


T = int(input())
# 8방향으로 흩어짐
dx = [-1, -2, -2, -1, 1, 2, 2, 1] 
dy = [2, 1, -1, -2, -2, -1, 1, 2]

for _ in range(T) :
    N = int(input())
    s1,s2 = map(int, input().split()) # 시작점
    e1,e2 = map(int, input().split()) # 끝점
    v=[[0]*N for _ in range(N)] #방문기록
    bfs(s1,s2,e1,e2)


