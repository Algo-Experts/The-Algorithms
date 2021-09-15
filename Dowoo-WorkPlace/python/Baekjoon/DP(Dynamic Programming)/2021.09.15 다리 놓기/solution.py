# https://www.acmicpc.net/problem/1010

# 문제요약 
# 서쪽의 N개의 사이트와 동쪽의 M개의 사이트가 있다
# 다리를 최대한 많이 짓고 겹칠 수 없다.

# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.

# 출력
# 각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력한다.

# 예제 입력 1 
# 3
# 2 2
# 1 5
# 13 29

# 문제풀이
# 다리끼리 서로 겹쳐질수 없다고 하여  다리가 교차하면 안된다고 생각함.
# 처음에 DP문제라서 DP로 풀어볼려고함.

# 풀면 풀수록 DP문제가 아닌것 같은 느낌.
# 맨 처음 교차 안된다고 생각해서 계속 틀림

# 확인해보니 교차가능 및 공식을 대입함
# 기본개념 3! = 3x2x1 이고
# mCn = M!/(m-n)!n!을 알고 있다면 쉽게 가능하다!

import sys
import math # 불러와야 factorial 사용가능

T = int(sys.stdin.readline())

for _ in range(T) :
    N,M = map(int, sys.stdin.readline().split()) 
    result = math.factorial(M) // (math.factorial(N) * math.factorial(M-N)) # 공식대입
    print(result)    