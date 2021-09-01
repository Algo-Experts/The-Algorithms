# https://www.acmicpc.net/problem/1003

# 문제요약 
# 피보나치문제임 
# 앞에 숫자와 뒤에 숫자를 출력!

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

# 출력
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

# 예제 입력 1 
# 3
# 0
# 1
# 3
# 예제 출력 1 
# 1 0
# 0 1
# 1 2

# 문제풀이

import sys

# 함수 만들어줌
def fibo(k) :
    z = [1,0,1,1] # 0번
    o = [0,1,1,2] # 1번

    for i in range(4,k+1) :
        z.append(z[i-1]+z[i-2])
        o.append(o[i-1]+o[i-2])
        
    print("%d %d" %(z[k],o[k])) #두가지 모두 출력


# 숫자받아줌
N = int(sys.stdin.readline())

for i in range(N) :
    k = int(sys.stdin.readline()) # 숫자을 받음
    fibo(k) # 함수실행



