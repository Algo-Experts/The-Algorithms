# https://www.acmicpc.net/problem/1963

# 문제요약
# 입력은 항상 4자리
# 소수 a>b로 바꾸는데 항상 소수를 유지해야한다
# 숫자 1개만 바꿀 수 있다

# 입력
# 첫 줄에 test case의 수 T가 주어진다. 다음 T줄에 걸쳐 각 줄에 1쌍씩 네 자리 소수가 주어진다.

# 출력
# 각 test case에 대해 두 소수 사이의 변환에 필요한 최소 회수를 출력한다. 불가능한 경우 Impossible을 출력한다.

# 예제 입력 1 
# 3
# 1033 8179
# 1373 8017
# 1033 1033
# 예제 출력 1 
# 6
# 7
# 0

# 문제풀이
# 소수를 어떻게 구해야 하나 싶었음
# 아라토스테네스의 체 사용 

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

g = [True for i in range(10001)]
# 에라토스테네스의 체(제급근 범위까지 조사)
for i in range(2,101):
    # 소수인 상태에서 소수의 배수를 체크함
    if g[i] :
        j= i*2
        while j < 10001 :
            g[j] = False
            j+=i

def bfs() :
    q = deque()
    q.append((a,0))
    visit = [0 for i in range(10000)]
    visit[a] = 1
    while q :
        num, cnt = q.popleft()
        if num == b : # 같은면 카운트 반환
            return cnt
        if num < 1000: # 1000넘으면 패스
            continue
        for i in[1,10,100,1000] : # 각 자리 넣어가며 소수인 것을 찾는다
            n = num - num % (i*10) // i*i
            for j in range(10):
                if visit[n] == 0 and g[n] :
                    visit[n] = 1
                    q.append((n, cnt+1))
                n += i

for i in range(t) :
    a,b = map(int,input().split())
    res = bfs()
    print(res if res != None else "Impossible")