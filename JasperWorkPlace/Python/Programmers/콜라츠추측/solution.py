#  문제 설명
# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
def solution(num):
    answer = 0
    if num == 1:
        return 0

    while True:
        num = num/2

        if num % 2 == 0:
            answer += 1
        else:
            (num*3)+1
            answer += 1

        if num == 1:
            return answer

        elif answer == 500:

            return -1

    return answer
