# https://www.acmicpc.net/problem/2096

# 문제요약
# 3xn줄이 나옴
# 위에 3개중 아무거나 하나 택함
# 가장 아래줄에 위치할 경우 끝남
# 최대값과 최소값을 구하라

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

# 출력
# 첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

# 예제 입력 1 
# 3
# 1 2 3
# 4 5 6
# 4 9 0
# 예제 출력 1 
# 18 6


# 문제풀이
# 처음 답1과같이 이렇게 풀었는데 메모리 문제로 답이 안됨!ㅠ
# 답2와 같이 해야 풀림

# 답1
import sys

N = int(sys.stdin.readline())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dpMax = [[0]*3 for _ in range(N)]
dpMin = [[0]*3 for _ in range(N)]

for i in range(3) :
    dpMax[0][i] = map[0][i]
    dpMin[0][i] = map[0][i]

for i in range(1,N) :
    for j in range(3) :
        if j == 0 :
            dpMax[i][j] = map[i][j]+ max(dpMin[i-1][j],dpMax[i-1][j+1])
            dpMin[i][j] = map[i][j]+ min(dpMin[i-1][j],dpMin[i-1][j+1])
        elif j == 1 :
            dpMax[i][j] = map[i][j]+ max(dpMax[i-1][j],dpMax[i-1][j-1],dpMax[i-1][j+1])
            dpMin[i][j] = map[i][j]+ min(dpMin[i-1][j],dpMin[i-1][j-1],dpMin[i-1][j+1])
        else:
            dpMax[i][j] = map[i][j]+ max(dpMax[i-1][j],dpMax[i-1][j-1])
            dpMin[i][j] = map[i][j]+ min(dpMin[i-1][j],dpMin[i-1][j-1])

print(max(dpMax[-1]), min(dpMin[-1]))

# 답2
import sys

N = int(sys.stdin.readline())
dpMax = [[0]*3 for _ in range(2)] # 0 이전기록 1은 현재 값
dpMin = [[0]*3 for _ in range(2)] # 0 이전기록 1은 현재 값

for i in range(N) : 
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(3) :
        if j == 0 : # 1번은 위에 처음 중간
            dpMax[1][j] = arr[j]+ max(dpMax[0][j],dpMax[0][j+1]) 
            dpMin[1][j] = arr[j]+ min(dpMin[0][j],dpMin[0][j+1])
        elif j == 1 : # 2번은 위에 세 숫자 모두
            dpMax[1][j] = arr[j]+ max(dpMax[0][j],dpMax[0][j-1],dpMax[0][j+1])
            dpMin[1][j] = arr[j]+ min(dpMin[0][j],dpMin[0][j-1],dpMin[0][j+1])
        else: # 3번은 위에 중간 맨끝
            dpMax[1][j] = arr[j]+ max(dpMax[0][j],dpMax[0][j-1])
            dpMin[1][j] = arr[j]+ min(dpMin[0][j],dpMin[0][j-1])
    
    for j in range(3) : # 해당하는 값 넣어줌
        dpMax[0][j] = dpMax[1][j]
        dpMin[0][j] = dpMin[1][j]
    

print(max(dpMax[1]), min(dpMin[1]))




