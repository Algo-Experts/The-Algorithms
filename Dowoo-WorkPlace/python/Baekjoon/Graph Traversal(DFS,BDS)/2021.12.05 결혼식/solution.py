# https://www.acmicpc.net/problem/5567

# 문제요약
# 친구와 친구의 친구를 초대함
# 초대할 사람의 수를 구하라 

# 입력
# 첫째 줄에 상근이의 동기의 수 n (2 ≤ n ≤ 500)이 주어진다. 둘째 줄에는 리스트의 길이 m (1 ≤ m ≤ 10000)이 주어진다. 다음 줄부터 m개 줄에는 친구 관계 ai bi가 주어진다. (1 ≤ ai < bi ≤ n) ai와 bi가 친구라는 뜻이며, bi와 ai도 친구관계이다. 

# 출력
# 첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다.

# 예제 입력 1 
# 6
# 5
# 1 2
# 1 3
# 3 4
# 2 3
# 4 5
# 예제 출력 1 
# 3
# 예제 입력 2 
# 6
# 5
# 2 3
# 3 4
# 4 5
# 5 6
# 2 5
# 예제 출력 2 
# 0

# 문제풀이
# 어려운 문제는 아니었음

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]

for _ in range(m): # 노드 서로 연결시켜줌
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

check = [0]*(n+1) # 몇번째인지 까지 체크하기위함
check[1] = 1

def bfs(a):
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        for n in g[x]:
            if check[n] == 0:
                check[n] = check[x]+1 # 몇번째에 이어진건지 체크
                q.append(n)
    
bfs(1)
res = sum([1 for t in check if 2 <= t <= 3]) # 2는 내친구 3은 친구의 친구
print(res)