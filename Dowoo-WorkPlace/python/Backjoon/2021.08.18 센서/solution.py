# https://www.acmicpc.net/problem/2212

# 문제요약
# N개의 센서가 있음
# K개의 집중국을 만들예정
# 집중국의 수신가능 영역의 길이를 가장 최단거리로 만들어라!

# 입력
# 첫째 줄에 센서의 개수 N(1 ≤ N ≤ 10,000), 둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)가 주어진다. 셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다. 각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하이다.

# 출력
# 첫째 줄에 문제에서 설명한 최대 K개의 집중국의 수신 가능 영역의 길이의 합의 최솟값을 출력한다.

# 예제 입력 1 
# 6
# 2
# 1 6 9 3 6 7
# 예제 출력 1 
# 5

# 문제풀이

#앞으로 sys써서 빠르게 할것.
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
maps = list(map(int, sys.stdin.readline().split()))
dis = []
result = 0

maps.sort() # 위치를 오름 차순으로 정렬

for i in range(1,len(maps)) :
    dis.append(maps[i] - maps[i-1]) # 거리의 차이를 구함

dis.sort() # 거리의 차이를 오름 차순으로 정렬

for i in range((len(dis)-K+1)) : # 거리의 갯수 -k+1 만큼만 더해준다
    result += dis[i]

print(result)


    
    

