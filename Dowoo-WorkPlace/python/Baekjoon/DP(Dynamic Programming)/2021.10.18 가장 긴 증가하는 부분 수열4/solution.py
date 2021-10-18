# https://www.acmicpc.net/problem/14002

# 문제요약
# 가장 긴 증가하는 부분 수열 길이랑 숫자 출력하기

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

# 예제 입력 1 
# 6
# 10 20 10 30 20 50
# 예제 출력 1 
# 4
# 10 20 30 50

# 문제풀이
# 접근까지 다했는데 숫자열을 출력할때 한번에 해결해보고 싶었다.
# 찾아본결과 길이 따로 숫자열 따로 처한것을 확인함
# 숏코딩 참고하니 나와같은 생각을 한 분을 발견하고 원하는 대로 풀 수 있었다.

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[x] for x in arr]

for i in range(N) :
    for j in range(i) :
        if arr[j] < arr[i] :
            if len(dp[i]) < len(dp[j])+1 : # 이 조건이 있어야 최장길이를 구할 수 있다.
                dp[i] = dp[j] + [arr[i]] 


r = max(dp, key=len) # 큰수중 키는 len으로 한다. 결과로 [10,20,30,50] 이런식으로 나옴
print(len(r))
print(*r) # *이걸 쓰면 배열이 풀려서 출력된다

