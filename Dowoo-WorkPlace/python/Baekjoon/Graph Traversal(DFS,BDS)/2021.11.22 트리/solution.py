# https://www.acmicpc.net/problem/1068

# 문제요약
# 트리가 주어졌을 때, 노드를 지울경우 그때 노드의 갯수

# 입력
# 첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

# 출력
# 첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.

# 예제 입력 1 
# 5
# -1 0 0 1 1
# 2
# 예제 출력 1 
# 2
# 예제 입력 2 
# 5
# -1 0 0 1 1
# 1
# 예제 출력 2 
# 1

# 문제풀이
# dfs

import sys
input = sys.stdin.readline

n = int(input())
g = list(map(int, input().split()))
k = int(input())
cnt = 0

def dfs(num):
    g[num] = -2 # 삭제한다는 의미
    for i in range(len(g)): 
        if num == g[i]:
            dfs(i) # 부모노드 찾아 삭제시킴

dfs(k)
for i in range(len(g)):
    # -2가 아니면서 다른 노드의 부모노드도 아닌 원소를 찾으면 1씩 늘림
    if g[i] != -2 and i not in g: 
        cnt += 1
print(cnt)