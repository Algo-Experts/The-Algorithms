# https://www.acmicpc.net/problem/10610

# 문제요약
# 30배수가 되는 가장 큰수를 만들고 싶어함

# 입력
# N을 입력받는다. N는 최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

# 출력
# 미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.

# 예제 입력 1 
# 30
# 예제 출력 1 
# 30
# 예제 입력 2 
# 102
# 예제 출력 2 
# 210
# 예제 입력 3 
# 2931
# 예제 출력 3 
# -1
# 예제 입력 4 
# 80875542
# 예제 출력 4 
# 88755420

# 문제풀이

# 맨 처음 순열로 풀이를 했는데 메모리초과가 걸렸다
# 답은 될 수 있지만 너무나 많은 조합으로 시간초과가 되는 것이다.
from itertools import permutations as per

N = list(input())
N.sort(reverse=True)
res=[]
if N[-1] != '0' :
    print(-1)
else :
    a = list(list(map(''.join,per(N))))
    for i in a :
        if int(i) % 30 == 0 :
            res.append(i)
    print(max(res))

# 해답은 수학적인 지식이 있어야 했다
# 30배수는 끝자리가 0이어야하고
# 각 자리수의 합이 3배여야한다

N = list(input())
N.sort(reverse=True)

if N[-1] == '0' and sum(map(int,N)) % 3 == 0 :
    print(''.join(N))
else : 
    print(-1)

# if문 한줄쓰기
print(''.join(N) if N[-1] == '0' and sum(map(int,N)) % 3 == 0 else -1)




