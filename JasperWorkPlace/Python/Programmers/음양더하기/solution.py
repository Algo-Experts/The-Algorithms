# 짧은 문제!

# 어떤 정수들이 있다.
# 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes 와 이 정수들의 부호를 차례대로 담은
# boolean 배열 signs 가 매개 변수로 주어짐
#  실제 정수들의 합을 구하여 return

# boolean 함수가 [true,false,true] 일때, [+,-,+] 가 되는 것을 알 수 있다.

# 풀이 단계
#  1. 배열의 합을 담은 정수 하나를 생성 a
#  2. 반복문을 사용해서 true 일때 a 에 absolutes 를 더해주고
#  3. false 일때 a 에 absolutes 를 빼준다 !


def solution(absolutes, signs):
    #  1 단계
    a = 0

    for i in range(len(signs)):
        if(signs[i] == True):
            # 2 단계
            a += absolutes[i]
        else:
            # 3 단계
            a -= absolutes[i]

    return a
