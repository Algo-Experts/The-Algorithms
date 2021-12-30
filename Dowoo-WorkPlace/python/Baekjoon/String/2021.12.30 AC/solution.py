# https://www.acmicpc.net/problem/5430

# 문제요약
# 정수배열에 연산을 하기 위해 만든 언어 
# R - 뒤집가 D - 버리기가 있음
# 결과값 구하기

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

# 각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

# 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

# 다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)

# 전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

# 출력
# 각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.

# 예제 입력 1 
# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []
# 예제 출력 1 
# [2,1]
# error
# [1,2,3,5,8]
# error

# 문제풀이
# 하나씩 빼고 바꾸고 하는것도 하나의 방법이나
# 앞뒤로 빼야할 숫자를 구하고 마지막에 빼는 방법을 택함
# 이전에 이와 비슷한 문제를 풀어본 기억이 있음

t=int(input()) 

for i in range(t) :
    p = input()
    n = int(input())
    a = input()[1:-1].split(',') # 양끝 [] 제거

    p.replace('RR', '') # rr은 결국 제자리이므로 제거

    r,f,b = 0,0,0 # 리버스, 앞, 뒤 제외할 숫자
    
    for j in p : 
        if j == 'R' : # R이면 리버스 
            r += 1
        else : # D면 
            if r % 2 == 0 : # 그대로
                f += 1 # 앞 문자 제거
            else : # 홀수이므로 리버스 됬을때
                b += 1 # 뒷 문자 제거
    
    if f + b <= n : # 초과하면 더 많이 삭제된거기 때문에 에러
        a = a[f:n-b] # a 범위는 f~n-b까지 앞과 뒤를 자른상태
        if r % 2 == 1 : # 리버스 된 상태면 
            print('['+','.join(a[::-1])+']')
        else :
            print('['+','.join(a)+']')
    else :
        print('error')
    
    