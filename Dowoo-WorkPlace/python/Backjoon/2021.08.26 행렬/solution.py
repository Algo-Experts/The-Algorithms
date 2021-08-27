# https://www.acmicpc.net/problem/1080

# 문제요약
# 0과 1로만 이우어진 행렬 A / B가 있는데 
# 3x3크기의 부분 행렬에 있는 원소를 뒤집는다

# 입력
# 첫째 줄에 행렬의 크기 N M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 행렬 A가 주어지고, 그 다음줄부터 N개의 줄에는 행렬 B가 주어진다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다. 만약 A를 B로 바꿀 수 없다면 -1을 출력한다.

# 예제 입력 1 
# 3 4
# 0000
# 0010
# 0000
# 1001
# 1011
# 1001
# 예제 출력 1 
# 2

# 문제풀이

# 값을 받음
N, M = map(int, input().split())
A = []
result = []
count = 0

#값을 넣어줌
for i in range(N) :
    A.append(list(map(int, input())))

for i in range(N) :
    result.append(list(map(int, input())))

# 체크하는 함수
def change(x,y):
    for i in range(x,x+3): 
        for j in range(y,y+3) : # 3x3일때
            A[i][j] = 1 - A[i][j] # 1-0=1 / 1-1=0 즉 바뀜

for  i in range(N-2) :
    for j in range(M-2):
        if A[i][j] != result[i][j]: # 다를경우 체크하는 함수 실행 후 카운트+1
            change(i,j)
            count +=1

if A == result:
    print(count)
else :
    print(-1)