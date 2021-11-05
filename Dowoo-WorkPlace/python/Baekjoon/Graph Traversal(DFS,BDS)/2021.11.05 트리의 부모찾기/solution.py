# https://www.acmicpc.net/problem/11725

# 문제요약
# 루트 없는 트리가 주어짐
# 트리의 루트를 1이라고 가정했을 때, 각 노드의 부모를 구하는 프로그램

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

# 예제 입력 1 
# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7
# 예제 출력 1 
# 4
# 6
# 1
# 3
# 1
# 4
# 예제 입력 2 
# 12
# 1 2
# 1 3
# 2 4
# 3 5
# 3 6
# 4 7
# 4 8
# 5 9
# 5 10
# 6 11
# 6 12
# 예제 출력 2 
# 1
# 1
# 2
# 3
# 3
# 4
# 4
# 5
# 5
# 6
# 6

# 문제풀이
# DFS BFS 무엇으로 풀어도 무관하나
# DFS가 더 나은 방법이라고 생각함(끝을 알면 되는 것이기 때문)
# 어려운 문제는 아니었음

import sys
sys.setrecursionlimit(10 ** 9) # 제한

N=int(sys.stdin.readline())
t=[[] for _ in range(N+1)]
for _ in range(N-1): # 해당하는 노드 서로서로 연결
    a,b=map(int,sys.stdin.readline().split())
    t[a].append(b)
    t[b].append(a)

p=[0 for _ in range(N+1)] # 부모 저장

def DFS(a): # 부모노드찾기
    for i in t[a]:
        if p[i]==0:
           p[i]=a
           DFS(i)
 
DFS(1)
for i in range(2,N+1): # 출력
    print(p[i])