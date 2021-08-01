#https://www.acmicpc.net/problem/19941

#문제요약
#식탁의 길이 , 햄버거를 선택할 수 있는 거리 , 사람과 햄버거의 위치가 주어졌을 때, 햄버거를 먹을 수 있는 사람의 최대 수를 구하는 것

# 입력
# 첫 줄에 두 정수 과 가 있다. 그리고 다음 줄에 사람과 햄버거의 위치가 문자 P(사람)와 H(햄버거)로 이루어지는 길이 인 문자열로 주어진다.

# 출력
# 첫 줄에 햄버거를 먹을 수 있는 최대 사람 수를 나타낸다.

# 제한
# 예제 입력 1 
# 20 1
# HHPHPPHHPPHPPPHPHPHP
# 예제 출력 1 
# 8
# 예제 입력 2 
# 20 2
# HHHHHPPPPPHPHPHPHHHP
# 예제 출력 2 
# 7

#문제풀이

#값을 받는다.
n, k = map(int, input().split())
arr = list(input())
cnt = 0

for i in range(n) :
    if arr[i] == 'P' : #사람이 나올경우  반복문을 돌려서 k범위에 앞에서 부터 하나씩 찾고 나오면 바꿔준다.
        for j in range(i-k,i+k+1):
            if 0 <= j < n and arr[j] == 'H' : # k의 범위가 초과될 수 있으므로 범위를 잡아준다.
                arr[j] = 'X'
                cnt += 1
                break

print(cnt)




