# https://www.acmicpc.net/problem/11497

# 문제요약
# 통나무를 세우고 그 차이의 최소로 하여 그 값들의 최대값을 구하는 것

# 입력
# 입력은 T개의 테스트 케이스로 이루어져 있다. 첫 줄에 T가 주어진다.

# 이어지는 각 줄마다 첫 줄에 통나무의 개수를 나타내는 정수 N(5 ≤ N ≤ 10,000), 둘째 줄에 각 통나무의 높이를 나타내는 정수 Li가 주어진다. (1 ≤ Li ≤ 100,000)

# 출력
# 각 테스트 케이스마다 한 줄에 주어진 통나무들로 만들 수 있는 최소 난이도를 출력하시오.

# 예제 입력 1 
# 3
# 7
# 13 10 12 11 10 11 12
# 5
# 2 4 5 7 9
# 8
# 6 6 6 6 6 6 6 6
# 예제 출력 1 
# 1
# 4
# 0

#문제풀이

#1. 숫자를 받는다.
import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    tree = list(map(int, sys.stdin.readline().split()))
    #2. 오름차순으로 변경. 
    tree.sort()
    #3. 통나무는 최소 5개 이기 떄문에 2부터 시작함. 2차이가 나는 이유는 
    # 맨 위에서 아래 두개까지 비교만 하면 되기 때문!
    result = 0
    for j in range(2, n):
        result = max(result, abs(tree[j] - tree[j - 2]))
    print(result)