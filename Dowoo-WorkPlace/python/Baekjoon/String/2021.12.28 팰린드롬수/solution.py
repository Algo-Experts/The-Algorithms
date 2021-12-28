# https://www.acmicpc.net/problem/1259

# 문제요약
# 앞에서 뒤에서 읽어도 똑같다면 팰린드롬이라고 한다.
# 팰린드롬 수를 찾는 것

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 1 이상 99999 이하의 정수가 주어진다. 입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.

# 출력
# 각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.

# 예제 입력 1 
# 121
# 1231
# 12421
# 0
# 예제 출력 1 
# yes
# no
# yes

while True :
    a=input()
    if a == '0' : # 0일경우 끝
        break
    # 역순도 같을경우 yes 안될경우 no
    print("yes" if a == a[::-1] else "no") 


