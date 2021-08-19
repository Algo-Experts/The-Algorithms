# https://www.acmicpc.net/problem/15904

# 문제요약 
# 단축해서 UCPC가 나와야함

# 입력
# 첫 번째 줄에 알파벳 대소문자, 공백으로 구성된 문자열이 주어진다. 문자열의 길이는 최대 1,000자이다. 문자열의 맨 앞과 맨 끝에 공백이 있는 경우는 없고, 공백이 연속해서 2번 이상 주어지는 경우도 없다.

# 출력
# 첫 번째 줄에 입력으로 주어진 문자열을 적절히 축약해 "UCPC"로 만들 수 있으면 "I love UCPC"를 출력하고, 만들 수 없으면 "I hate UCPC"를 출력한다.

# 예제 입력 1 
# Union of Computer Programming Contest club contest
# 예제 출력 1 
# I love UCPC
# 예제 입력 2 
# University Computer Programming
# 예제 출력 2 
# I hate UCPC

# 문제풀이
N = input()
ans = "UCPC"
count = 0

# 하나씩 찾고 4개일경우 출력한다.
for i in N:
    if i == ans[count]:
        count +=1
        if count == 4:
            break

if count == 4:
    print("I love UCPC")
else :
    print("I hate UCPC")


# 풀이보던중 배워야할 풀이
# re를 사용하여 매치시킴! like느낌
import re
print("I love UCPC" if re.match(".*U.*C.*P.*C.*", input()) else "I hate UCPC")