# https://www.acmicpc.net/problem/1932

# 문제요약
# 정수 삼각형이 주어지는데
# 값이 아래로 더해진다 최대값을 구하라!

# 입력
# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

# 출력
# 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

# 예제 입력 1 
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
# 예제 출력 1 
# 30

# 문제풀이
# 이제 dp의 개념과 풀이 방법을 알것같음!
# 우선 규칙을 찾아야함 
# 양 끝사이드는 계속 바로 위 양끝 사이드만 더해짐
# 중간은 둘중에 가장 큰값이 더해짐

import sys

N = int(sys.stdin.readline())
arr = [] 

for _ in range(N) :
    arr.append(list(map(int, sys.stdin.readline().split())))


for i in range(1,N) : # 두번째 줄부터 시작
    for j in range(i+1) : # i줄에는 i개의 숫자가 있어야 하므로 +1
        if j == 0 : # 좌
            arr[i][0] += arr[i-1][0]
        elif j == i : # 우
            arr[i][j] += arr[i-1][j-1]
        else : # 중간 숫자들 위에 숫자중 큰수가 더해짐
            arr [i][j] += max(arr[i-1][j-1],arr[i-1][j])

# 아래 값중에 가장 큰 값을 출력!
print(max(arr[N-1]))

