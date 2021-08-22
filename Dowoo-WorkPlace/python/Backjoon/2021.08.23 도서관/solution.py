# https://www.acmicpc.net/problem/1461

# 도서관에 책을 둔다 책권수와 들고갈 수 있는 최대 권수를 받음
# + - 거리를 받고 마지막은 돌아오지 않는다.
# 최소거리수는?

# 입력
# 첫째 줄에 책의 개수 N과, 세준이가 한 번에 들 수 있는 책의 개수 M이 주어진다. 둘째 줄에는 책의 위치가 주어진다. N은 10,000보다 작거나 같은 자연수이고, M은 10,000보다 작거나 같다. 책의 위치는 0이 아니며, 그 절댓값이 10,000보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

# 예제 입력 1 
# 7 2
# -37 2 -6 -39 -29 11 -28
# 예제 출력 1 
# 131

import sys

N, M = map(int, sys.stdin.readline().split())
book = list(map(int, sys.stdin.readline().split()))
A = [] # 마이너스 보관
B = [] # 플러스 보관
result = [] # 결과

for i in range(N) :
    if book[i] < 0 :
        A.append(book[i]) # 마이너스 보관
    else :
        B.append(book[i]) # 플러스 보관

A.sort() # 마이너스는 오름차순으로
B.sort(reverse=True) # 플러스는 내림차순으로
        
for i in range(0,len(A),M) : # M 거리만큼!
    result.append(abs(A[i])) 

for i in range(0,len(B),M) : # M 거리만큼!
    result.append(abs(B[i]))

print((sum(result)*2)-max(result)) #결과값에 2배 해주고 최고값을 -1 해준다!
