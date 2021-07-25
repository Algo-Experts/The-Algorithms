# https://www.acmicpc.net/problem/1715

# 문제요약
# 두묶음씩 골라서 계속 합쳐서 진행됨
# 10,20,40이 있다면 10과 20일 합치고 그 합과 40을 합치는 것 그러면 100이 나오게된다.
# n개의 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇번의 비교가 필요한지 구하는 프로그램을 작성하라.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다. 숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.

# 출력
# 첫째 줄에 최소 비교 횟수를 출력한다.

# 예제 입력 1 
# 3
# 10
# 20
# 40
# 예제 출력 1 
# 100

# 문제풀이
# https://littlefoxdiary.tistory.com/3 heapq 참고자료

# 문제에 정렬된 두 묶음의 카드가 있으므로 sort는 사용하지 않는다
# heapq문제임 이 함수를 알아야지 시간초과가 걸리지 않음.
 

import heapq

n = int(input())
heap = []
result = 0

for i in range(n):
    num = int(input())
    heapq.heappush(heap, num)

if len(heap) == 1:
    print(0)
else:
    while len(heap) > 1:
        temp1 = heapq.heappop(heap)
        temp2 = heapq.heappop(heap)
        result += temp1 + temp2
        heapq.heappush(heap, temp1 + temp2)

    print(result)