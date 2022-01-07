# https://www.acmicpc.net/problem/10820

# 문제요약
# 소문자,대문자,숫자,공백의 개수를 구하라

# 입력
# 첫째 줄부터 N번째 줄까지 문자열이 주어진다. (1 ≤ N ≤ 100) 문자열의 길이는 100을 넘지 않는다.

# 출력
# 첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.

# 예제 입력 1 
# This is String
# SPACE    1    SPACE
#  S a M p L e I n P u T     
# 0L1A2S3T4L5I6N7E8
# 예제 출력 1 
# 10 2 0 2
# 0 10 1 8
# 5 6 0 16
# 0 8 9 0

# 문제풀이
# 숫자랑 공백을 어떻게 해야할까 고민하다가
# islower와 isupper 와 같은 메소드가 있을것 같아
# 찾아본 결과 있었다. 
# 정해진 숫자가 없으므로
# try, except를 사용한다

while True :
    try : 
        a = input()
        l,u,n,s = 0,0,0,0 # 소,대,숫자,공백

        for i in a :
            if i.islower() :
                l += 1
            elif i.isupper() :
                u += 1
            elif i.isdigit() :
                n += 1
            elif i.isspace() :
                s += 1
        print(l, u, n, s)
    except :
        break

 

    
