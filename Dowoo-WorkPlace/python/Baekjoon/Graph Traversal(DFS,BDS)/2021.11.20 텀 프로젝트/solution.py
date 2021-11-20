# https://www.acmicpc.net/problem/9466

# 문제요약
# 팀을 각각 선택할 수 있다
# 어느 팀 프로젝트 팀에도 속하지 않는 학생찾기

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다. 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)

# 출력
# 각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.

# 예제 입력 1 
# 2
# 7
# 3 1 3 7 3 4 6
# 8
# 1 2 3 4 5 6 7 8
# 예제 출력 1 
# 3
# 0

# 문제풀이
# dfs로 풀어야함

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

T = int(input())

def dfs(v): # 재귀함수
    global res
    visit[v] = 1 # 방문기록
    arr.append(v) # 탐색경로
    w = g[v]
    if visit[w] ==1 :
        if w in arr: # 탐색 경로에 다음 방문할 것이 존재하면 순환
            res += arr[arr.index(w):] # 사이클 되면 구간부터 팀을 이룸
        return
    else:
        dfs(w) # 탐색시작

for _ in range(T) :
    V = int(input()) # 학생수
    g = [0] + list(map(int, input().split())) # 0을 넣어 순서를 맞춤
    visit = [0] * (V+1)
    res = [] # 팀구성학생수
    for i in range(1, V+1) :
        if visit[i] == 0:
            arr = []
            dfs(i) 

    print(V-len(res))
