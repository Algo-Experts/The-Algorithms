# https://www.acmicpc.net/problem/2812

# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

# 둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

# 출력
# 입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.

# 예제 입력 1 
# 4 2
# 1924
# 예제 출력 1 
# 94
# 예제 입력 2 
# 7 3
# 1231234
# 예제 출력 2 
# 3234
# 예제 입력 3 
# 10 4
# 4177252841
# 예제 출력 3 
# 775841

# 문제풀이
# 앞에서 부터 가장 큰 수를 찾되 길이는 유지가 되어야함

import sys

N, K = map(int, sys.stdin.readline().split())
S = list(sys.stdin.readline().strip())
T = []
TN = K

for i in range(N):
    # 지울수 있는 숫자가 있을 경우 큰수가 앞으로 두는것!
    while K > 0 and T and T[-1] < S[i]: 
        del T[-1]
        K -= 1
    T.append(S[i])
    print(T)

# 리스트를 문자열로
print(''.join(T[:N - TN]))

