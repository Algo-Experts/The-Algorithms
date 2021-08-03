# https://www.acmicpc.net/submit/1343/31754782

# 문제요약
# XXXX는 AAAA로 XX는 BB로 바꿔라!

# 입력
# 첫째 줄에 보드판이 주어진다. 보드판의 크기는 최대 500이다.

# 출력
# 첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 만약 덮을 수 없으면 -1을 출력한다.

# 예제 입력 1 
# XXXXXX
# 예제 출력 1 
# AAAABB
# 예제 입력 2 
# XX.XX
# 예제 출력 2 
# BB.BB
# 예제 입력 3 
# XXXX....XXX.....XX
# 예제 출력 3 
# -1
# 예제 입력 4 
# X
# 예제 출력 4 
# -1
# 예제 입력 5 
# XX.XXXXXXXXXX..XXXXXXXX...XXXXXX
# 예제 출력 5 
# BB.AAAAAAAABB..AAAAAAAA...AAAABB

# 문제풀이

# 문자를 받고
s = input()
result = s.replace('XXXX','AAAA').replace('XX','BB') # replace를 통해 문자열 교체!

# X가 있을경우 -1출력!
if 'X' in result :
    print(-1)
else :
    print(result) # 아닐경우 바꾼결과값 출력