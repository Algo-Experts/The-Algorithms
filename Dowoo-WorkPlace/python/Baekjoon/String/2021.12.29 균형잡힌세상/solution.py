# https://www.acmicpc.net/problem/4949

# 문제요약
# (), [] 짝을 이뤄야함

# 입력
# 하나 또는 여러줄에 걸쳐서 문자열이 주어진다. 각 문자열은 영문 알파벳, 공백, 소괄호("( )") 대괄호("[ ]")등으로 이루어져 있으며, 길이는 100글자보다 작거나 같다.

# 입력의 종료조건으로 맨 마지막에 점 하나(".")가 들어온다.
# 출력
# 각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

# 예제 입력 1 
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .
# 예제 출력 1 
# yes
# yes
# no
# no
# no
# yes
# yes

# 문제풀이
# 괄호문제와 비슷하다
# 나올수 있는 경우의 수로 풀었지만
# 다른풀이도 딱히 떠오르지 않는다.

while True :
    a = input()
    temp = [] # 괄호 보관
    res = True # 결과값도출 괄호가 없더라도 true이므로 true시작

    if a =='.' : # . 나오면 끝
        break
    
    for i in a :
        if i == '(' or i == '[' : # 여는 괄호가 나오면 값넣어줌
            temp.append(i)
        elif i == ')' :
            if not temp or temp[-1] == '[' : # 넣은 마지막이 )일때 마지막이 다르면 불가능
                res = False
                break
            elif temp[-1] == '(' :
                temp.pop() # 정당하게 나왔다면 마지막에 들어간거 뺌
        elif i == ']' :
            if not temp or temp[-1] == '(' : # 위와 마찬가지임
                res = False
                break
            elif temp[-1] == '[' :
                temp.pop()
    if res == True and not temp :
        print('yes')
    else : 
        print('no')