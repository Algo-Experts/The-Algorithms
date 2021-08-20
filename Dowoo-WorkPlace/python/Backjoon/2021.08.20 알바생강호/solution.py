# https://www.acmicpc.net/problem/1758

# 문제요약
# 주고자 했던 tip-(등수-1)을 한 후
# 팁의 최대값을 구하기

# 입력
# 첫째 줄에 스타박스 앞에 서 있는 사람의 수 N이 주어진다. N은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 총 N개의 줄에 각 사람이 주려고 하는 팁이 주어진다. 팁은 100,000보다 작거나 같은 자연수이다.

# 출력
# 강호가 받을 수 있는 팁의 최댓값을 출력한다.

# 예제 입력 1 
# 4
# 3
# 3
# 3
# 3
# 예제 출력 1 
# 6

#문제풀이

#앞으로 sys를 사용하자!
import sys

N = int(sys.stdin.readline())
tips = []
sum = 0

for _ in range(N) :
    tips.append(int(sys.stdin.readline()))

#최대값을 벌어야 하기 때문에 역순으로 조정
tips.sort(reverse=True)

for i in range(len(tips)) :
    if tips[i]-i >0 :
        sum += tips[i] -i

print(sum)