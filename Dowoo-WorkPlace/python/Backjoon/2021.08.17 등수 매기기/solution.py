# https://www.acmicpc.net/problem/2012

# 문제요약
# 예상등수가 A 실제등수가 B이다 실제 등수는 모르고 예상 등수만 알고 있는데 
# 예상등수가 빗나갈경우 불만도가 증가한다. 불만도를 최소인 값을 구하라

# 입력
# 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 500,000) 둘째 줄부터 N개의 줄에 걸쳐 각 사람의 예상 등수가 순서대로 주어진다. 예상 등수는 500,000 이하의 자연수이다.

# 출력
# 첫째 줄에 불만도의 합을 최소로 할 때, 그 불만도를 출력한다.

# 예제 입력 1 
# 5
# 1
# 5
# 3
# 1
# 2
# 예제 출력 1 
# 3


#문제풀이

#시간초과가 계속 걸려서 sys사용
import sys

N = int(sys.stdin.readline())
arr = []
result = 0

for i in range(N) :
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in range(N):
    result += abs((i+1)-arr[i]) # 값의 차이만 구하면된다.

print(result)