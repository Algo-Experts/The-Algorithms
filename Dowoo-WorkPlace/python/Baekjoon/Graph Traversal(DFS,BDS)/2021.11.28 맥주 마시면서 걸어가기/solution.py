# https://www.acmicpc.net/problem/9205

# 문제요약
# 50m마다 맥주를 마시고 20개가 한계
# 편의점을 들리면 빈병 버리고 새 맥주 살수있음
# 편의점 나선 직후에도 50m가기전에 맥주 한명 마셔야함

# 입력
# 첫째 줄에 테스트 케이스의 개수 t가 주어진다. (t ≤ 50)

# 각 테스트 케이스의 첫째 줄에는 맥주를 파는 편의점의 개수 n이 주어진다. (0 ≤ n ≤ 100).

# 다음 n+2개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표가 주어진다. 각 좌표는 두 정수 x와 y로 이루어져 있다. (두 값 모두 미터, -32768 ≤ x, y ≤ 32767)

# 송도는 직사각형 모양으로 생긴 도시이다. 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이 이다. (맨해튼 거리)

# 출력
# 각 테스트 케이스에 대해서 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 "happy", 중간에 맥주가 바닥나서 더 이동할 수 없으면 "sad"를 출력한다. 

# 예제 입력 1 
# 2
# 2
# 0 0
# 1000 0
# 1000 1000
# 2000 1000
# 2
# 0 0
# 1000 0
# 2000 1000
# 2000 2000
# 예제 출력 1 
# happy
# sad

# 문제풀이
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs() :
    q = deque([s])
    visit = set()
    while q:
        x, y = q.popleft()
        if abs(x-e[0]) + abs(y-e[1]) <= 1000 :
            return print("happy")
        
        for i in range(n) :
            if i not in visit :
                nx, ny = c[i]
                if abs(x-nx) + abs(y-ny) <= 1000 :
                    q.append([nx,ny])
                    visit.add(i)
    return print("sad")

for _ in range(T) :
    n = int(input())
    s = [int(i) for i in input().split()]
    c = [[int(i) for i in input().split()] for _ in range(n)]
    e = [int(i) for i in input().split()]
    bfs()