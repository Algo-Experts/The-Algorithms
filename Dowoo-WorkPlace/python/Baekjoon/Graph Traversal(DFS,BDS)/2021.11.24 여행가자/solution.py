# https://www.acmicpc.net/problem/1976

# 문제요약
# 도시와 연결된 길이 있다
# 여행계획이 있을 경우 가능한지 판별하라

# 입력
# 첫 줄에 도시의 수 N이 주어진다. N은 200이하이다. 둘째 줄에 여행 계획에 속한 도시들의 수 M이 주어진다. M은 1000이하이다. 다음 N개의 줄에는 N개의 정수가 주어진다. i번째 줄의 j번째 수는 i번 도시와 j번 도시의 연결 정보를 의미한다. 1이면 연결된 것이고 0이면 연결이 되지 않은 것이다. A와 B가 연결되었으면 B와 A도 연결되어 있다. 마지막 줄에는 여행 계획이 주어진다. 도시의 번호는 1부터 N까지 차례대로 매겨져 있다.

# 출력
# 첫 줄에 가능하면 YES 불가능하면 NO를 출력한다.

# 예제 입력 1 
# 3
# 3
# 0 1 0
# 1 0 1
# 0 1 0
# 1 2 3
# 예제 출력 1 
# YES

# 문제풀이
# union - find 조합을 해야한다

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = int(input())

g = [ i for i in range(N+1)] # 노드설정 

def find(a): # 부모노드찾기
    if a == g[a] : # 본인이면 본인 반환
        return a
    p = find(g[a])
    g[a] = p # 부모노드 찾기
    return g[a]

def union(a,b) : # a와 b 합치기
    a = find(a)
    b = find(b)

    if a==b: # 순환이 발생하므로 스탑
        return
    
    if a<b : # 상위 루트로
        g[b] = a 
    else :
        g[a] = b

for i in range(1,N+1) : # 연결되어 있는 정보
    city = list(map(int, input().split()))
    for j in range(1, len(city)+1):
        if city[j-1] == 1: # 연결되어있으면
            union(i,j) # 두 도시 연결

tour = list(map(int, input().split())) # 여행계획
res = set([find(i) for i in tour]) # 노드찾기

print('NO' if len(res) != 1 else "YES" ) # 결과앖



