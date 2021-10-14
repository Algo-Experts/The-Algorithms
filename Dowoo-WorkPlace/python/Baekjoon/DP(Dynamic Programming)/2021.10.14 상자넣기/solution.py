# https://www.acmicpc.net/problem/1965

# 문제요약
# 상자를 점점 더 큰상자에 넣는것 
# 최대 상자의 갯수

# 입력
# 파일의 첫 번째 줄은 상자의 개수 n (1 ≤ n ≤ 1000)을 나타낸다. 두 번째 줄에는 각 상자의 크기가 순서대로 주어진다. 상자의 크기는 1,000을 넘지 않는 자연수이다.

# 출력
# 첫째 줄에 한 줄에 넣을 수 있는 최대의 상자 개수를 출력한다.

# 예제 입력 1 
# 8
# 1 6 2 5 7 3 5 6
# 예제 출력 1 
# 5

# 문제풀이
# 오랜만에 쉬운 문제가 나왔다..
# 쉽게 말하면 결국 증가하는 함수를 찾는것

import sys
N = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
dp = [1]*N

for i in range(N) :
    for j in range(i) : # 내 순서까지 돌림
        if box[j] < box[i] : # 나보다 작으면 
            dp[i] = max(dp[i],dp[j]+1) # dp[j]+1 한것과 지금 내 수랑 비교해서 큰수!
            print(dp)
        
print(max(dp))