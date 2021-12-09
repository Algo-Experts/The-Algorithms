# https://www.acmicpc.net/problem/8958

# 문제요약
# OX가 주어지는데 연속으로 맞을 경우 +1씩 추가점수

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

# 출력
# 각 테스트 케이스마다 점수를 출력한다.

# 예제 입력 1 
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
# 예제 출력 1 
# 10
# 9
# 7
# 55
# 30

# 문제풀이

T = int(input())

for i in range(T) :
    a = list(map(str, input()))
    cnt = 1
    sum = 0 
    for j in a :
        if j == "O" :
            sum += cnt
            cnt += 1
        else :
            cnt = 1
    print(sum)

T = int(input())