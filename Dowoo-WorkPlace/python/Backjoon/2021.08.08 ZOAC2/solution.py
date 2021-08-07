# https://www.acmicpc.net/problem/18238

# 문제요약
# 회전판에 알파벳이 있고 최소로 맞춘다.

# 예제 입력 1 
# ZOAC
# 예제 출력 1 
# 26
# 예제 입력 2 
# LBOLVUEEPMOIENMG
# 예제 출력 2 
# 100

# 문제풀이 

string = list(input()) #리스트로 받는다

start = 'A'
count = 0 
for a in string:
    ok = abs(ord(start)-abs(ord(a))) #절대값으로 처리하여 이동

    if ok > 13 : #절반보다 클경우는 반대로 가는게 더 빠름.
        ok = 26-ok

    count += ok
    start = a

print(count)

    

