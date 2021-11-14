# https://www.acmicpc.net/problem/9019

# 문제요약
# D는 n을 두배로 바꿈 9999보다 크면 10000으로 나눈 나머지
# S는 n-1 0이면 9999가 저장됨
# L은 n을 각 자리수를 왼편으로 회전
# R은 n을 각 자리수를 오른편으로 회전

# 입력
# 프로그램 입력은 T 개의 테스트 케이스로 구성된다. 테스트 케이스 개수 T 는 입력의 첫 줄에 주어진다. 각 테스트 케이스로는 두 개의 정수 A와 B(A ≠ B)가 공백으로 분리되어 차례로 주어지는데 A는 레지스터의 초기 값을 나타내고 B는 최종 값을 나타낸다. A 와 B는 모두 0 이상 10,000 미만이다.

# 출력
# A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열을 출력한다. 가능한 명령어 나열이 여러가지면, 아무거나 출력한다.

# 예제 입력 1 
# 3
# 1234 3412
# 1000 1
# 1 16
# 예제 출력 1 
# LL
# L
# DDDD

# 문제풀이
import sys
from collections import deque
input = sys.stdin.readline

T = int(input()) # 테스트 갯수

def bfs() :
    q=deque()
    q.append([a,""])
    while q:
        num, res = q.popleft()
        # DSLN에 대한 방법
        dn = (2*num) % 10000
        sn = num - 1 if num != 0 else 9999
        ln = int(num % 1000 * 10 + num / 1000)
        rn = int(num % 10 * 1000 + num // 10)

        if dn == b: return res + "D"
        elif arr[dn] == 0:
            arr[dn] = 1
            q.append([dn, res + "D"])

        if sn == b: return res + "S"
        elif arr[sn] == 0:
            arr[sn] = 1
            q.append([sn, res + "S"])
        
        if ln == b: return res + "L"
        elif arr[ln] == 0:
            arr[ln] = 1
            q.append([ln, res + "L"])
        
        if rn == b: return res + "R"
        elif arr[rn] == 0:
            arr[rn] = 1
            q.append([rn, res + "R"])


for i in range(T):
    a,b = map(int, input().split())
    arr = [0 for i in range(10000)]
    print(bfs())
    
