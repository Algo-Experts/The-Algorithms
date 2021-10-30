# https://www.acmicpc.net/problem/1987

# 문제요약
# 상하좌우로 이동한다. 새로 이동한 칸은 알파벳이 달라야한다.
# 말이 지날수 있는 최대 칸수를 구하라

# 입력
# 첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

# 출력
# 첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

# 예제 입력 1 
# 2 4
# CAAB
# ADCB
# 예제 출력 1 
# 3
# 예제 입력 2 
# 3 6
# HFDFFB
# AJHGDH
# DGAGEH
# 예제 출력 2 
# 6
# 예제 입력 3 
# 5 5
# IEFCJ
# FHFKC
# FFALF
# HFGCF
# HMCHH
# 예제 출력 3 
# 10

# 문제풀이
# 최대길이를 구하는 것으로 DFS가 유리함
# 재귀함수 사용
# 백트래킹
# 계속 bfs만 풀다가 dfs풀려니 어려웠다.

import sys

R,C = map(int, sys.stdin.readline().split())
# map을 lambda로 이용해서 쓸수 있다는걸 알았음.
A = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip())) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [0]*26
visited[A[0][0]] = 1
cnt = 1

def dfs(a,b,c) :
    global cnt
    cnt = max(c,cnt) # 큰값으로 변경하기

    for i in range(4) :
        x = a + dx[i]            
        y = b + dy[i]
        if 0 <= x < R and 0 <= y < C and visited[A[x][y]] == 0:
            visited[A[x][y]] = 1 # 체크함
            dfs(x,y,c+1) # 재귀
            visited[A[x][y]] = 0 # 백트래킹 되돌림

dfs(0,0,1)
print(cnt)



