# https://www.acmicpc.net/problem/11655

# 문제요약
# 알파벳을 13글자씩 밀어서 암호화

# 입력
# 첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.

# 출력
# 첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.

# 예제 입력 1 
# Baekjoon Online Judge
# 예제 출력 1 
# Onrxwbba Bayvar Whqtr
# 예제 입력 2 
# One is 1
# 예제 출력 2 
# Bar vf 1

# 문제풀이
# 아스키코드의 방법도 있지만
# 다른방법으로 풀이를 해보았다

s = input()
a = 'abcdefghijklmnopqrstuvwxyz' # 알파벳나열

res = '' 

for i in s :
    if i.islower() : # 소문자일경우
        n = (a.index(i) + 13) % 26 # 인덱스 +13 후 나눈 나머지
        res += a[n]
    elif i.isupper() : # 대문자일경우
        i = i.lower() # 소문자로 변경후
        n = (a.index(i) + 13) % 26
        res += a[n].upper() # 다시 대문자로 변경
    else :
        res += i # 알파벳 아니면 그대로 
        
print(res)
