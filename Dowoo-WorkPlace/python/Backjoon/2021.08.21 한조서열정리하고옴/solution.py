# https://www.acmicpc.net/problem/14659

# 문제요약
# 산봉오리에 한명의 활잡이가 있다
# 산봉오리가 높은곳에서 낮은곳으로 사격 가능
# 오로지 앞쪽으로만 진행됨

# 입력
# 첫째 줄에 봉우리의 수 겸 활잡이의 수 N이 주어진다. (1 ≤ N ≤ 30,000) 둘째 줄에 N개 봉우리의 높이가 왼쪽 봉우리부터 순서대로 주어진다. (1 ≤ 높이 ≤ 100,000) 각각 봉우리의 높이는 중복 없이 유일하다.

# 출력
# 최고의 활잡이가 처치할 수 있는 적의 최대 숫자를 출력한다.

# 예제 입력 1 
# 7
# 6 4 10 2 5 7 11
# 예제 출력 1 
# 3

# 문제풀이
import sys

N = int(sys.stdin.readline())
top = list(map(int,sys.stdin.readline().split()))
result = 0
count = 0
best = 0

for i in range(len(top)) :
    if best < top[i] : # 산봉오리가 커질경우 카운트 0 최고높이 교체
        count = 0       
        best = top[i] 
    else : # 그렇지 않을경우 카운트 +1
        count += 1

    result = max(result, count) #베스트 카운트 찾기
print(result)


