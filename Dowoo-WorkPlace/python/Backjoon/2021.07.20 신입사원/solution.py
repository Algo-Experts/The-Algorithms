# https://www.acmicpc.net/problem/1946

# 어렵고.. 시간초과도 걸리고 ㅠㅠ

# 문제요약
# 신입사원을 뽑는데 최고를 뽑고자함.
# 순위가 주어지는데 다른 지원자보다 성적이든 면접이든 하나라도 더 높아야함!

# 입력
# 첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

# 출력
# 각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 2
# 5
# 3 2
# 1 4
# 4 1
# 2 3
# 5 5
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1
# 예제 출력 1 
# 4

#문제풀이

#1.속도때문에 readline써야함!
import sys

T = int(sys.stdin.readline())

# 2. 시험에 따른 반복문 돌림!
for _ in range(T):
    N = int(sys.stdin.readline())
    record = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] #순위를 리스트에 넣음.
    record.sort() #정렬!

    minrecord = record[0][1] # 시험 1위 기준으로 면접순위를 비교함.
    count = 1 #1등은 통과니까 +1

    for i in range(1, N): # 보다 낮은 순위면 카운터를 늘려주고 그 값을 기준값으로 바꿔줌
        if record[i][1] < minrecord:
            count += 1
            minrecord = record[i][1]

    print(count)

