# https://www.acmicpc.net/problem/1012

# 배추흰지렁이가 있으면 해충으로 부터 보호한다
# 특정 배추에 배추흰지렁이가 있으면 인접한 배추로 이동 가능하고 보호한다
# 상화좌우로 이동한다.
# 최소 몇마리의 배추흰지렁이가 필요한가?

# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

# 출력
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

# 예제 입력 1 
# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5
# 예제 출력 1 
# 5
# 1
# 예제 입력 2 
# 1
# 5 3 6
# 0 2
# 1 2
# 2 2
# 3 2
# 4 2
# 4 0
# 예제 출력 2 
# 2

# 문제풀이
# 단지번호 붙이기와 비슷한 문제이다
# BFS로 풀어야함

import sys # 시간때문에 혹시 몰라서 씀
from collections import deque #BFS는 이제 이거 쓰기

T = int(sys.stdin.readline())
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(a,b) : 
    maps[a][b] = 0 # 0으로 바꿔줌
    q=deque()
    q.append((a,b))

    while q :     
        x1,y1 = q.popleft()
        for i in range(4) :
            x = x1 + dx[i]
            y = y1 + dy[i]

            if 0 <= x < M and 0<= y < N and maps[x][y] == 1:
                q.append((x,y))
                maps[x][y] = 0 # 0으로 변경


for _ in range(T) : # 테스트가 만큼
    M, N, K = map(int, sys.stdin.readline().split())
    maps = [[0]*(N) for _ in range(M)] # 범위 꼭 잘 정하기! 이거 때문에 틀렸음 ㅠ
    cnt = 0

    for _ in range(K) :
        X, Y = map(int, sys.stdin.readline().split())
        maps[X][Y] = 1 # 배추있는 곳은 1로 바꿔줌
    
    for i in range(M) :
        for j in range(N) :
            if maps[i][j] == 1 : # 배추있으면 메소드 실행!
                bfs(i,j) 
                cnt +=1
             
    print(cnt)
    

    