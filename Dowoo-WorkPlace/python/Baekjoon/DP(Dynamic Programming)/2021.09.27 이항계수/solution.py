# https://www.acmicpc.net/problem/11051

# 문제요약
# 이항계수를 구하는 것

# 입력
# 첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 1,000, 0 ≤ \(K\) ≤ \(N\))

# 출력
 
# \(\binom{N}{K}\)를 10,007로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 5 2
# 예제 출력 1 
# 10

# 문제풀이
# 이항계수가 무엇인지 몰라서 찾아봤다
# nCk 이렇게 표시하기도 한다고 한다.
# 예전에 다리놓기에서 풀었던게 생각나서 그 방식대로 먼저 풀어보았다.
# mCn = m!/(m-n)!n!을 알고 있다면 쉽게 가능하다!
# 파스칼의 삼각형과도 같다고 한다! 이것은 dp식으로 풀때 필요하다!

# 1번 풀이는 예전에 풀었던것과 같이 공식을 대입한 경우다
# 이때는 math를 사용하였다.
# 속도가 빠르게 나온것을 확인함

import sys
import math

N, K = map(int, sys.stdin.readline().split())

result = math.factorial(N) // (math.factorial(K) * math.factorial(N-K))
print(result % 10007)


# 2번 풀이는 dp식으로 풀어보았다.

import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[1]*(i+1) for i in range(N+1)] #파스칼 삼각형으로 생각하면 층을 만드는 작업

for i in range(2,N+1) :
    for j in range(1,i) : #범위는 맨 앞과 뒤를 제외하도록 한다.
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])%10007 # 이전값의 왼쪽위 오른쪽 위의 값의 합

print(dp[N][K])



