# https://www.acmicpc.net/problem/5639

# 문제요약
# 왼쪽 서브트리는 노드의 키보다 작다
# 오른쪽 서브트리는 노드의 키보다 크다
# 이진 검색 트리를 전위 순회한 결과가 주어졌을 때
# 이 트리를 후위 순회한 결과를 구하라

# 입력
# 트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

# 출력
# 입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 50
# 30
# 24
# 5
# 28
# 45
# 98
# 52
# 60
# 예제 출력 1 
# 5
# 28
# 24
# 45
# 30
# 60
# 52
# 98
# 50

# 문제풀이
# 그래프문제가 아닌거같음
# 트리문제?

import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

g = []
while True : # 몇개 받으라는게 없기 때문에 try사용  
    try : 
        g.append(int(input()))
    except :
        break # 문제생기면 끝내라 

def sol(s,e) :
    if s>e:
        return
    div = e+1

    for i in range(s+1,e+1) :
        if g[s] < g[i] :
            div = i
            break

    sol(s+1,div-1) # 왼쪽 순환
    sol(div, e) # 오른쪽 순환
    print(g[s])

sol(0,len(g)-1)
