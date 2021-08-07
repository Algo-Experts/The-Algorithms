# https://www.acmicpc.net/problem/14469

# 문제요약
# 소가 온 순서대로 검사해서 들여보내지만 앞에 온 소가 있을경우 기다렸다가 들어간다.

#입력
# 첫 줄에 100 이하의 양의 정수 N이 주어진다. 다음 N줄에는 한 줄에 하나씩 소의 도착 시각과 검문 시간이 주어진다. 각각 1,000,000 이하의 양의 정수이다.

# 출력
# 모든 소가 농장에 입장하는 데 걸리는 최소 시간을 출력한다.

# 예제 입력 1 
# 3
# 2 1
# 8 3
# 5 7
# 예제 출력 1 
# 15

# 문제풀이

# 숫자를 받는다.
n = int(input())
arr = []
time = 0

for i in range(n) : 
    arr.append(list(map(int,input().split()))) # 이중배열로 저장되어있다

arr.sort() #배열의 앞부분 기준으로 오름차순

for i in arr:
    if i[0] > time : 
        time = i[0] + i[1] # 타임보다 클경우는 온 시간 + 걸리는 시간
    else : 
        time += i[1] # 타임보다 작거나 같은 경우는 타임에 걸리는 시간을 더해준다.

print(time)
